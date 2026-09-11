import { useState } from "react";
import LearningHub from "./LearningHub";

const API_BASE_URL = 'http://localhost:8001';

function App() {
  const [currentPage, setCurrentPage] = useState("roadmap");

  // ======================================================
  // ROADMAP STATES
  // ======================================================

  const [userId] = useState("1");
  const [careerId] = useState("1");

  const [roadmap, setRoadmap] = useState(null);

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const [progress, setProgress] = useState({});
  const [progressLoading, setProgressLoading] = useState(false);

  // ======================================================
  // QUIZ STATES
  // ======================================================

  const [quizOpen, setQuizOpen] = useState(false);
  const [quizSkill, setQuizSkill] = useState(null);
  const [quizQuestions, setQuizQuestions] = useState([]);
  const [quizAnswers, setQuizAnswers] = useState({});
  const [quizResult, setQuizResult] = useState(null);
  const [quizLoading, setQuizLoading] = useState(false);
  const [quizSubmitting, setQuizSubmitting] = useState(false);

  // ======================================================
  // GENERATE ROADMAP
  // ======================================================

  async function generateRoadmap() {
    if (!userId || !careerId) {
      setError("Please enter both User ID and Career ID.");
      return;
    }

    try {
      setLoading(true);
      setError("");
      setRoadmap(null);

      const response = await fetch(
        `${API_BASE_URL}/roadmap/generate`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            user_id: Number(userId),
            career_id: Number(careerId),
          }),
        }
      );

      if (!response.ok) {
        const errorData =
          await response.json().catch(() => null);

        throw new Error(
          errorData?.detail ||
            "Failed to generate roadmap."
        );
      }

      const data = await response.json();

      setRoadmap(data);

      await loadProgress(Number(userId));
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  // ======================================================
  // LOAD PROGRESS
  // ======================================================

  async function loadProgress(id) {
    try {
      setProgressLoading(true);

      const response = await fetch(
        `${API_BASE_URL}/progress/${id}`
      );

      if (!response.ok) {
        return;
      }

      const data = await response.json();

      const progressMap = {};

      data.forEach((item) => {
        progressMap[item.skill_id] = {
          percentage:
            Number(item.progress_percentage) || 0,
          completed:
            item.completed === true ||
            Number(item.progress_percentage) >= 100,
        };
      });

      setProgress(progressMap);
    } catch (err) {
      console.error(
        "Progress loading error:",
        err
      );
    } finally {
      setProgressLoading(false);
    }
  }

  // ======================================================
  // UPDATE SKILL PROGRESS
  // ======================================================

  async function updateSkillProgress(skillId) {
    if (!userId) {
      setError("Please enter a User ID first.");
      return;
    }

    const currentProgress =
      progress[skillId]?.percentage || 0;

    if (currentProgress >= 100) {
      return;
    }

    try {
      setError("");

      const nextProgress = Math.min(
        currentProgress + 25,
        100
      );

      const response = await fetch(
        `${API_BASE_URL}/progress/update?user_id=${Number(
          userId
        )}&skill_id=${skillId}&progress_percentage=${nextProgress}`,
        {
          method: "POST",
        }
      );

      if (!response.ok) {
        const errorData =
          await response.json().catch(() => null);

        throw new Error(
          errorData?.detail ||
            "Unable to update progress."
        );
      }

      setProgress((previous) => ({
        ...previous,
        [skillId]: {
          percentage: nextProgress,
          completed: nextProgress >= 100,
        },
      }));
    } catch (err) {
      setError(err.message);
    }
  }

  // ======================================================
  // OPEN LEARNING MATERIAL
  // ======================================================

  async function openLearningMaterial(skillName) {
    if (!skillName) {
      setError("Learning skill not found.");
      return;
    }

    // Open immediately so browser does not block popup
    const newTab = window.open("", "_blank");

    try {
      setError("");

      // First try exact skill search
      let response = await fetch(
        `${API_BASE_URL}/courses/skill/${encodeURIComponent(
          skillName
        )}`
      );

      let courses = [];

      if (response.ok) {
        courses = await response.json();
      }

      // If exact skill did not find anything,
      // try general search
      if (!Array.isArray(courses) || courses.length === 0) {
        response = await fetch(
          `${API_BASE_URL}/courses/search/${encodeURIComponent(
            skillName
          )}`
        );

        if (response.ok) {
          courses = await response.json();
        }
      }

      // Find first valid URL
      const course = Array.isArray(courses)
        ? courses.find(
            (item) =>
              item &&
              item.url &&
              item.url.trim() !== ""
          )
        : null;

      if (course?.url) {
        newTab.location.href = course.url;
        return;
      }

      if (newTab) {
        newTab.close();
      }

      setError(
        `No learning resource is available yet for "${skillName}".`
      );
    } catch (err) {
      console.error(
        "Learning resource error:",
        err
      );

      if (newTab) {
        newTab.close();
      }

      setError(
        `Unable to open learning material for "${skillName}".`
      );
    }
  }

  // ======================================================
  // OPEN QUIZ
  // ======================================================

  async function openQuiz(skillId, skillName) {
    if (!userId) {
      setError("Please enter a User ID first.");
      return;
    }

    try {
      setQuizLoading(true);
      setQuizOpen(true);
      setQuizSkill({
        id: skillId,
        name: skillName,
      });
      setQuizQuestions([]);
      setQuizAnswers({});
      setQuizResult(null);
      setError("");

      const response = await fetch(
        `${API_BASE_URL}/quiz/skill/${skillId}`
      );

      if (!response.ok) {
        const data =
          await response.json().catch(() => null);

        throw new Error(
          data?.detail ||
            "Quiz is not available for this skill yet."
        );
      }

      const data = await response.json();

      setQuizQuestions(data);
    } catch (err) {
      setQuizOpen(false);
      setError(err.message);
    } finally {
      setQuizLoading(false);
    }
  }

  // ======================================================
  // SELECT QUIZ ANSWER
  // ======================================================

  function selectQuizAnswer(questionId, answer) {
    setQuizAnswers((previous) => ({
      ...previous,
      [String(questionId)]: answer,
    }));
  }

  // ======================================================
  // SUBMIT QUIZ
  // ======================================================

  async function submitQuiz() {
    if (!quizSkill) {
      return;
    }

    if (quizQuestions.length === 0) {
      return;
    }

    const unanswered = quizQuestions.filter(
      (question) =>
        !quizAnswers[String(question.id)]
    );

    if (unanswered.length > 0) {
      setQuizResult({
        localError:
          "Please answer all questions before submitting.",
      });
      return;
    }

    try {
      setQuizSubmitting(true);
      setQuizResult(null);

      const response = await fetch(
        `${API_BASE_URL}/quiz/submit?user_id=${Number(
          userId
        )}&skill_id=${quizSkill.id}`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(quizAnswers),
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data?.detail ||
            "Unable to submit quiz."
        );
      }

      setQuizResult(data);

      // Backend marks progress 100 on pass.
      // Update frontend immediately too.
      if (data.passed) {
        setProgress((previous) => ({
          ...previous,
          [quizSkill.id]: {
            percentage: 100,
            completed: true,
          },
        }));
      }
    } catch (err) {
      setQuizResult({
        localError: err.message,
      });
    } finally {
      setQuizSubmitting(false);
    }
  }

  // ======================================================
  // RETRY QUIZ
  // ======================================================

  function retryQuiz() {
    setQuizAnswers({});
    setQuizResult(null);
  }

  // ======================================================
  // CLOSE QUIZ
  // ======================================================

  function closeQuiz() {
    setQuizOpen(false);
    setQuizSkill(null);
    setQuizQuestions([]);
    setQuizAnswers({});
    setQuizResult(null);
  }

  // ======================================================
  // NAVIGATION
  // ======================================================

  function showRoadmap() {
    setCurrentPage("roadmap");

    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  }

  function showLearningHub() {
    setCurrentPage("learning");

    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  }

  // ======================================================
  // RETURN
  // ======================================================

  return (
    <div style={styles.app}>

      {/* ==================================================
          NAVBAR
      ================================================== */}

      <nav style={styles.navbar}>

        <div style={styles.brandSection}>

          <img
            src="/skill-up-ai-logo.png"
            alt="Skill Up AI"
            style={styles.skillUpLogo}
          />

        </div>

        <div style={styles.navLinks}>

          <button
            onClick={showRoadmap}
            style={{
              ...styles.navButton,
              ...(currentPage === "roadmap"
                ? styles.activeNavButton
                : {}),
            }}
          >
            Roadmap
          </button>

          <button
            onClick={showLearningHub}
            style={{
              ...styles.navButton,
              ...(currentPage === "learning"
                ? styles.activeNavButton
                : {}),
            }}
          >
            Learning Hub
          </button>

          <a
            href="#about"
            style={styles.navLink}
            onClick={() =>
              setCurrentPage("roadmap")
            }
          >
            About
          </a>

          <div style={styles.profile}>
            P
          </div>

        </div>

      </nav>

      {/* ==================================================
          LEARNING HUB
      ================================================== */}

      {currentPage === "learning" ? (

        <LearningHub />

      ) : (

        <>

          {/* ==================================================
              HERO
          ================================================== */}

          <section style={styles.hero}>

            <div style={styles.heroContent}>

              <div style={styles.heroBadge}>
                🚀 AI-Powered Career Guidance
              </div>

              <h1 style={styles.heroTitle}>
                Build Your{" "}
                <span style={styles.gradientText}>
                  Future
                </span>
                <br />
                With Skill Up AI
              </h1>

              <p style={styles.heroText}>
                Get a personalized learning roadmap
                tailored to your selected career and
                track your progress step by step.
              </p>

              <button
                onClick={() => {
                  document
                    .getElementById("roadmap")
                    ?.scrollIntoView({
                      behavior: "smooth",
                    });
                }}
                style={styles.primaryButton}
              >
                Create My Roadmap →
              </button>

            </div>

          </section>

          {/* ==================================================
              ROADMAP
          ================================================== */}

          <section
            id="roadmap"
            style={styles.roadmapSection}
          >

            <div style={styles.sectionHeader}>

              <h2 style={styles.sectionTitle}>
                Personalized Learning Roadmap
              </h2>

              <p style={styles.sectionSubtitle}>
                Discover a personalized learning path designed
                to help you build the skills for your career.
              </p>

            </div>

            {/* GENERATE ROADMAP */}

            <div style={styles.generateCard}>
              <button
                onClick={generateRoadmap}
                disabled={loading}
                style={styles.generateButton}
              >
                {loading
                  ? "Generating..."
                  : "Generate My Roadmap →"}
              </button>
            </div>

            {/* ERROR */}

            {error && (
              <div style={styles.errorBox}>
                ⚠️ {error}
              </div>
            )}

            {/* PROGRESS LOADING */}

            {progressLoading && (
              <div style={styles.loadingText}>
                Loading progress...
              </div>
            )}

            {/* ==================================================
                ROADMAP RESULT
            ================================================== */}

            {roadmap && (

              <div style={styles.roadmapContainer}>

                <div style={styles.roadmapHeader}>

                  <div>

                    <div style={styles.smallLabel}>
                      YOUR PERSONALIZED PATH
                    </div>

                    <h2 style={styles.roadmapTitle}>
                      Learning Roadmap
                    </h2>

                    <p style={styles.roadmapDescription}>
                      Follow these skills in order to
                      prepare for your selected career.
                    </p>

                  </div>

                  <div style={styles.roadmapCount}>
                    {roadmap.items?.length || 0}

                    <span
                      style={
                        styles.roadmapCountLabel
                      }
                    >
                      {" "}Skills
                    </span>
                  </div>

                </div>

                {/* ROADMAP ITEMS */}

                <div style={styles.itemsContainer}>

                  {roadmap.items?.map(
                    (item, index) => {

                      const currentProgress =
                        progress[item.skill_id]
                          ?.percentage || 0;

                      const isCompleted =
                        currentProgress >= 100;

                      const skillName =
                        item.skill?.name ||
                        `Skill ${item.skill_id}`;

                      return (

                        <div
                          key={item.id || index}
                          style={styles.skillCard}
                        >

                          <div style={styles.number}>
                            {index + 1}
                          </div>

                          <div
                            style={styles.skillContent}
                          >

                            {/* SKILL TITLE */}

                            <div
                              style={
                                styles.skillTitleRow
                              }
                            >

                              <h3
                                style={
                                  styles.skillTitle
                                }
                              >
                                {skillName}
                              </h3>

                              <span
                                style={
                                  styles.linkIcon
                                }
                              >
                                🔗
                              </span>

                            </div>

                            <p
                              style={
                                styles.skillDescription
                              }
                            >
                              Learn {skillName} as part
                              of your personalized
                              career path.
                            </p>

                            {/* META */}

                            <div
                              style={
                                styles.metaRow
                              }
                            >

                              <span
                                style={{
                                  ...styles.priority,
                                  ...(item.priority ===
                                  "High"
                                    ? styles.highPriority
                                    : item.priority ===
                                      "Medium"
                                    ? styles.mediumPriority
                                    : styles.lowPriority),
                                }}
                              >
                                {item.priority}
                              </span>

                              <span
                                style={
                                  styles.duration
                                }
                              >
                                ⏱️{" "}
                                {item.estimated_weeks}{" "}
                                week
                                {item.estimated_weeks !==
                                1
                                  ? "s"
                                  : ""}
                              </span>

                            </div>

                            {/* PROGRESS HEADER */}

                            <div
                              style={
                                styles.progressHeader
                              }
                            >

                              <span>
                                Progress:
                              </span>

                              <strong>
                                {currentProgress}%
                              </strong>

                              {isCompleted && (
                                <span
                                  style={
                                    styles.completedText
                                  }
                                >
                                  ✓ Completed
                                </span>
                              )}

                            </div>

                            {/* PROGRESS BAR */}

                            <div
                              style={
                                styles.progressBarBackground
                              }
                            >

                              <div
                                style={{
                                  ...styles.progressBar,
                                  width: `${currentProgress}%`,
                                }}
                              />

                            </div>

                            {/* ==================================================
                                BUTTONS
                            ================================================== */}

                            <div
                              style={
                                styles.buttonRow
                              }
                            >

                              {/* START LEARNING

                                  IMPORTANT:
                                  This button ALWAYS stays available,
                                  even after 100%.
                              */}

                              <button
                                type="button"
                                onClick={() =>
                                  openLearningMaterial(
                                    skillName
                                  )
                                }
                                style={
                                  styles.startButton
                                }
                              >
                                📚 Start Learning →
                              </button>

                              {/* CONTINUE */}

                              <button
                                type="button"
                                onClick={() =>
                                  updateSkillProgress(
                                    item.skill_id
                                  )
                                }
                                disabled={
                                  currentProgress >=
                                  100
                                }
                                style={{
                                  ...styles.continueButton,
                                  ...(currentProgress >=
                                  100
                                    ? styles.completedButton
                                    : {}),
                                }}
                              >
                                {currentProgress >=
                                100
                                  ? "✓ Completed"
                                  : "Continue Learning +25%"}
                              </button>

                              {/* QUIZ */}

                              {currentProgress >=
                                100 && (

                                <button
                                  type="button"
                                  onClick={() =>
                                    openQuiz(
                                      item.skill_id,
                                      skillName
                                    )
                                  }
                                  style={
                                    styles.quizButton
                                  }
                                >
                                  🎯 Take Quiz
                                </button>

                              )}

                            </div>

                          </div>

                        </div>

                      );
                    }
                  )}

                </div>

              </div>

            )}

          </section>

          {/* ==================================================
              FEATURES
          ================================================== */}

          <section
            style={styles.featuresSection}
          >

            <div style={styles.sectionHeader}>

              <div style={styles.robotIcon}>
                🤖
              </div>

              <h2 style={styles.sectionTitle}>
                AI Personalized
              </h2>

              <p style={styles.featureText}>
                Get a learning path tailored to your
                selected career.
              </p>

            </div>

            <div style={styles.featuresGrid}>

              <div style={styles.featureCard}>

                <div style={styles.featureIcon}>
                  🎯
                </div>

                <h3>
                  Career Focused
                </h3>

                <p
                  style={
                    styles.featureCardText
                  }
                >
                  Learn the skills that matter for
                  your target career.
                </p>

              </div>

              <div style={styles.featureCard}>

                <div style={styles.featureIcon}>
                  📈
                </div>

                <h3>
                  Track Progress
                </h3>

                <p
                  style={
                    styles.featureCardText
                  }
                >
                  Monitor your learning journey and
                  complete each milestone.
                </p>

              </div>

              <div style={styles.featureCard}>

                <div style={styles.featureIcon}>
                  📚
                </div>

                <h3>
                  Learning Hub
                </h3>

                <p
                  style={
                    styles.featureCardText
                  }
                >
                  Explore courses and learning
                  resources for different skills.
                </p>

                <button
                  onClick={showLearningHub}
                  style={styles.smallButton}
                >
                  Explore Courses →
                </button>

              </div>

            </div>

          </section>

          {/* ==================================================
              ABOUT
          ================================================== */}

          <section
            id="about"
            style={styles.aboutSection}
          >

            <h2>
              Skill Up AI
            </h2>

            <p>
              Personalized learning. Smarter careers.
            </p>

            <p>
              © 2026 Skill Up AI
            </p>

          </section>

        </>

      )}

      {/* ==================================================
          QUIZ MODAL
      ================================================== */}

      {quizOpen && (

        <div style={styles.modalOverlay}>

          <div style={styles.quizModal}>

            <div style={styles.quizHeader}>

              <div>

                <div style={styles.smallLabel}>
                  SKILL ASSESSMENT
                </div>

                <h2 style={styles.quizTitle}>
                  🎯 {quizSkill?.name} Quiz
                </h2>

              </div>

              <button
                onClick={closeQuiz}
                style={styles.closeButton}
              >
                ✕
              </button>

            </div>

            {quizLoading ? (

              <div style={styles.quizLoading}>
                Loading quiz...
              </div>

            ) : quizResult?.localError ? (

              <div style={styles.quizError}>
                ⚠️ {quizResult.localError}
              </div>

            ) : quizResult ? (

              <div style={styles.resultBox}>

                <div style={styles.resultIcon}>
                  {quizResult.passed
                    ? "🎉"
                    : "📚"}
                </div>

                <h2>
                  {quizResult.passed
                    ? "Quiz Passed!"
                    : "Quiz Not Passed"}
                </h2>

                <p style={styles.scoreText}>
                  Score:{" "}
                  <strong>
                    {quizResult.score}
                  </strong>
                  {" / "}
                  {quizResult.total_questions}
                </p>

                <p style={styles.percentageText}>
                  {quizResult.percentage}%
                </p>

                <p>
                  {quizResult.passed
                    ? "Great job! This skill has been completed."
                    : "You need at least 60% to pass. Try again."}
                </p>

                <div style={styles.quizResultButtons}>

                  {!quizResult.passed && (
                    <button
                      onClick={retryQuiz}
                      style={styles.quizButton}
                    >
                      🔄 Retry Quiz
                    </button>
                  )}

                  <button
                    onClick={closeQuiz}
                    style={styles.startButton}
                  >
                    Close
                  </button>

                </div>

              </div>

            ) : (

              <>

                <div style={styles.quizInstructions}>
                  Answer all questions. You need
                  <strong> 60%</strong> or higher to pass.
                </div>

                <div>

                  {quizQuestions.map(
                    (question, index) => (

                      <div
                        key={question.id}
                        style={styles.questionCard}
                      >

                        <h3>
                          {index + 1}.{" "}
                          {question.question}
                        </h3>

                        <div
                          style={
                            styles.optionsContainer
                          }
                        >

                          {question.options.map(
                            (option, optionIndex) => {

                              const selected =
                                quizAnswers[
                                  String(question.id)
                                ] === option;

                              return (

                                <button
                                  key={optionIndex}
                                  type="button"
                                  onClick={() =>
                                    selectQuizAnswer(
                                      question.id,
                                      option
                                    )
                                  }
                                  style={{
                                    ...styles.optionButton,
                                    ...(selected
                                      ? styles.selectedOption
                                      : {}),
                                  }}
                                >

                                  <span
                                    style={
                                      styles.optionLetter
                                    }
                                  >
                                    {String.fromCharCode(
                                      65 + optionIndex
                                    )}
                                  </span>

                                  {option}

                                </button>

                              );

                            }
                          )}

                        </div>

                      </div>

                    )
                  )}

                </div>

                {quizQuestions.length > 0 && (

                  <button
                    onClick={submitQuiz}
                    disabled={quizSubmitting}
                    style={styles.submitQuizButton}
                  >
                    {quizSubmitting
                      ? "Submitting..."
                      : "Submit Quiz"}
                  </button>

                )}

              </>

            )}

          </div>

        </div>

      )}

    </div>
  );
}

// ======================================================
// STYLES
// ======================================================

const styles = {

  app: {
    minHeight: "100vh",
    background: "#f7f8fc",
    color: "#172033",
    fontFamily:
      "Arial, Helvetica, sans-serif",
  },

  // NAVBAR

  navbar: {
    position: "sticky",
    top: 0,
    zIndex: 100,
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    padding: "22px 8%",
    background: "rgba(255,255,255,0.97)",
    borderBottom:
      "1px solid #e5e7eb",
  },

  brandSection: {
    display: "flex",
    alignItems: "center",
    gap: "14px",
  },

  logo: {
    width: "54px",
    height: "54px",
    borderRadius: "16px",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    background:
      "linear-gradient(135deg,#7c3aed,#6d4aff)",
    color: "white",
    fontSize: "28px",
    fontWeight: "bold",
  },

  skillUpLogo: {
    width: "180px",
    height: "auto",
    objectFit: "contain",
    display: "block",
  },

  brandName: {
    fontSize: "22px",
    fontWeight: "500",
  },

  navLinks: {
    display: "flex",
    alignItems: "center",
    gap: "30px",
  },

  navButton: {
    border: "none",
    background: "transparent",
    cursor: "pointer",
    fontSize: "17px",
    color: "#667085",
    padding: "8px 4px",
  },

  activeNavButton: {
    color: "#6d4aff",
    fontWeight: "700",
  },

  navLink: {
    textDecoration: "none",
    color: "#667085",
    fontSize: "17px",
  },

  profile: {
    width: "38px",
    height: "38px",
    borderRadius: "50%",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    background: "#111827",
    color: "white",
    fontWeight: "bold",
  },

  // HERO

  hero: {
    padding: "100px 8% 110px",
    textAlign: "center",
    background:
      "linear-gradient(135deg, #e9d5ff 0%, #c4b5fd 45%, #a5b4fc 100%)",
    minHeight: "430px",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
  },

  heroContent: {
    maxWidth: "850px",
    margin: "auto",
  },

  heroBadge: {
    display: "inline-block",
    padding: "12px 22px",
    borderRadius: "30px",
    background: "#ffffff",
    color: "#5b21b6",
    fontWeight: "700",
    marginBottom: "25px",
    boxShadow: "0 8px 25px rgba(91,33,182,0.15)",
  },

  heroTitle: {
    fontSize: "52px",
    lineHeight: "1.15",
    margin: "0 0 25px",
    color: "#171126",
    fontWeight: "800",
    textShadow: "0 2px 10px rgba(255,255,255,0.35)",
  },

  gradientText: {
    color: "#5b21b6",
    fontWeight: "800",
  },

  heroText: {
    fontSize: "19px",
    lineHeight: "1.7",
    color: "#312e4b",
    maxWidth: "680px",
    margin: "auto auto 30px",
    fontWeight: "500",
  },

  primaryButton: {
    border: "none",
    borderRadius: "14px",
    padding: "16px 32px",
    background: "#6d28d9",
    color: "white",
    fontSize: "17px",
    fontWeight: "700",
    cursor: "pointer",
    boxShadow: "0 10px 25px rgba(91,33,182,0.25)",
    transition: "all 0.2s ease",
  },

  // SECTIONS

  roadmapSection: {
    padding: "70px 8%",
    maxWidth: "1200px",
    margin: "auto",
  },

  sectionHeader: {
    textAlign: "center",
    marginBottom: "35px",
  },

  sectionTitle: {
    fontSize: "32px",
    marginBottom: "12px",
  },

  sectionSubtitle: {
    color: "#667085",
    fontSize: "17px",
  },

  // GENERATE ROADMAP

  generateCard: {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    padding: "25px",
    background: "white",
    borderRadius: "18px",
    boxShadow:
      "0 5px 20px rgba(0,0,0,0.06)",
    marginBottom: "25px",
  },

  // FORM

  formCard: {
    display: "flex",
    alignItems: "end",
    gap: "18px",
    flexWrap: "wrap",
    padding: "25px",
    background: "white",
    borderRadius: "18px",
    boxShadow:
      "0 5px 20px rgba(0,0,0,0.06)",
    marginBottom: "25px",
  },

  inputGroup: {
    flex: 1,
    minWidth: "220px",
  },

  label: {
    display: "block",
    marginBottom: "8px",
    fontWeight: "600",
  },

  input: {
    width: "100%",
    boxSizing: "border-box",
    padding: "13px",
    borderRadius: "10px",
    border: "1px solid #d0d5dd",
    fontSize: "16px",
  },

  generateButton: {
    padding: "15px 30px",
    border: "none",
    borderRadius: "12px",
    background: "#6d28d9",
    color: "white",
    fontSize: "16px",
    fontWeight: "700",
    cursor: "pointer",
    boxShadow: "0 8px 20px rgba(109,40,217,0.22)",
  },

  errorBox: {
    padding: "15px 18px",
    borderRadius: "10px",
    background: "#fff0f0",
    color: "#b42318",
    marginBottom: "20px",
  },

  loadingText: {
    textAlign: "center",
    padding: "20px",
    color: "#667085",
  },

  // ROADMAP

  roadmapContainer: {
    marginTop: "35px",
  },

  roadmapHeader: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    padding: "30px",
    background: "white",
    borderRadius: "18px 18px 0 0",
  },

  smallLabel: {
    color: "#7047e8",
    fontSize: "12px",
    fontWeight: "bold",
    letterSpacing: "1px",
  },

  roadmapTitle: {
    fontSize: "30px",
    margin: "8px 0",
  },

  roadmapDescription: {
    color: "#667085",
  },

  roadmapCount: {
    fontSize: "30px",
    fontWeight: "bold",
    color: "#7047e8",
  },

  roadmapCountLabel: {
    fontSize: "14px",
  },

  itemsContainer: {
    display: "flex",
    flexDirection: "column",
    gap: "18px",
    paddingTop: "18px",
  },

  skillCard: {
    display: "flex",
    gap: "25px",
    padding: "30px",
    background: "white",
    borderRadius: "18px",
    boxShadow:
      "0 3px 15px rgba(0,0,0,0.05)",
  },

  number: {
    minWidth: "42px",
    height: "42px",
    borderRadius: "50%",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    background: "#f0ebff",
    color: "#7047e8",
    fontWeight: "bold",
  },

  skillContent: {
    flex: 1,
  },

  skillTitleRow: {
    display: "flex",
    alignItems: "center",
    gap: "10px",
  },

  skillTitle: {
    margin: 0,
    fontSize: "22px",
  },

  linkIcon: {
    fontSize: "18px",
  },

  skillDescription: {
    color: "#667085",
    fontSize: "16px",
    lineHeight: "1.6",
  },

  metaRow: {
    display: "flex",
    alignItems: "center",
    gap: "12px",
    margin: "15px 0",
  },

  priority: {
    padding: "8px 14px",
    borderRadius: "20px",
    fontWeight: "bold",
    fontSize: "13px",
  },

  highPriority: {
    background: "#fff0ed",
    color: "#d6452d",
  },

  mediumPriority: {
    background: "#f0ebff",
    color: "#7047e8",
  },

  lowPriority: {
    background: "#f2f0ff",
    color: "#7047e8",
  },

  duration: {
    color: "#475467",
  },

  progressHeader: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    marginBottom: "8px",
    color: "#475467",
  },

  completedText: {
    color: "#15803d",
    fontWeight: "bold",
  },

  progressBarBackground: {
    height: "10px",
    background: "#e5e7eb",
    borderRadius: "20px",
    overflow: "hidden",
  },

  progressBar: {
    height: "100%",
    background:
      "linear-gradient(90deg,#7047e8,#9b7aff)",
    borderRadius: "20px",
    transition: "width 0.3s ease",
  },

  // BUTTONS

  buttonRow: {
    display: "flex",
    gap: "12px",
    marginTop: "18px",
    flexWrap: "wrap",
  },

  startButton: {
    padding: "11px 16px",
    border: "none",
    borderRadius: "8px",
    background: "#7047e8",
    color: "white",
    cursor: "pointer",
    fontWeight: "bold",
  },

  continueButton: {
    padding: "11px 16px",
    border: "none",
    borderRadius: "8px",
    background: "#475467",
    color: "white",
    cursor: "pointer",
  },

  completedButton: {
    background: "#15803d",
    cursor: "not-allowed",
  },

  quizButton: {
    padding: "11px 18px",
    border: "none",
    borderRadius: "8px",
    background: "#ea580c",
    color: "white",
    cursor: "pointer",
    fontWeight: "bold",
  },

  // FEATURES

  featuresSection: {
    padding: "80px 8%",
    textAlign: "center",
    background: "#f5f6fa",
  },

  robotIcon: {
    fontSize: "35px",
  },

  featureText: {
    color: "#667085",
    fontSize: "18px",
  },

  featuresGrid: {
    maxWidth: "1000px",
    margin: "40px auto 0",
    display: "grid",
    gridTemplateColumns:
      "repeat(auto-fit,minmax(250px,1fr))",
    gap: "25px",
  },

  featureCard: {
    background: "white",
    padding: "30px",
    borderRadius: "18px",
    boxShadow:
      "0 4px 15px rgba(0,0,0,0.05)",
  },

  featureIcon: {
    fontSize: "35px",
    marginBottom: "15px",
  },

  featureCardText: {
    color: "#667085",
    lineHeight: "1.6",
  },

  smallButton: {
    marginTop: "10px",
    border: "none",
    background: "transparent",
    color: "#7047e8",
    fontWeight: "bold",
    cursor: "pointer",
  },

  // ABOUT

  aboutSection: {
    padding: "60px 8%",
    textAlign: "center",
    background: "#ffffff",
    color: "#667085",
  },

  // ======================================================
  // QUIZ MODAL
  // ======================================================

  modalOverlay: {
    position: "fixed",
    inset: 0,
    background: "rgba(15,23,42,0.65)",
    zIndex: 1000,
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    padding: "20px",
    overflowY: "auto",
  },

  quizModal: {
    width: "100%",
    maxWidth: "800px",
    maxHeight: "90vh",
    overflowY: "auto",
    background: "white",
    borderRadius: "20px",
    padding: "30px",
    boxSizing: "border-box",
    boxShadow:
      "0 25px 60px rgba(0,0,0,0.25)",
  },

  quizHeader: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "flex-start",
    marginBottom: "25px",
  },

  quizTitle: {
    margin: "8px 0 0",
    fontSize: "28px",
  },

  closeButton: {
    width: "38px",
    height: "38px",
    border: "none",
    borderRadius: "50%",
    background: "#f1f5f9",
    cursor: "pointer",
    fontSize: "18px",
  },

  quizLoading: {
    textAlign: "center",
    padding: "50px",
    color: "#667085",
  },

  quizError: {
    padding: "18px",
    background: "#fff0f0",
    color: "#b42318",
    borderRadius: "10px",
  },

  quizInstructions: {
    padding: "15px",
    background: "#f5f3ff",
    borderRadius: "10px",
    marginBottom: "20px",
    color: "#475467",
  },

  questionCard: {
    padding: "20px",
    marginBottom: "18px",
    border: "1px solid #e5e7eb",
    borderRadius: "14px",
  },

  optionsContainer: {
    display: "flex",
    flexDirection: "column",
    gap: "10px",
    marginTop: "15px",
  },

  optionButton: {
    width: "100%",
    textAlign: "left",
    padding: "13px 15px",
    border: "1px solid #d0d5dd",
    borderRadius: "10px",
    background: "white",
    cursor: "pointer",
    fontSize: "15px",
  },

  selectedOption: {
    border: "2px solid #7047e8",
    background: "#f5f3ff",
  },

  optionLetter: {
    display: "inline-flex",
    justifyContent: "center",
    alignItems: "center",
    width: "28px",
    height: "28px",
    borderRadius: "50%",
    background: "#ede9fe",
    color: "#7047e8",
    fontWeight: "bold",
    marginRight: "10px",
  },

  submitQuizButton: {
    width: "100%",
    padding: "15px",
    border: "none",
    borderRadius: "10px",
    background: "#7047e8",
    color: "white",
    fontSize: "16px",
    fontWeight: "bold",
    cursor: "pointer",
    marginTop: "10px",
  },

  resultBox: {
    textAlign: "center",
    padding: "30px",
  },

  resultIcon: {
    fontSize: "55px",
  },

  scoreText: {
    fontSize: "20px",
  },

  percentageText: {
    fontSize: "45px",
    fontWeight: "bold",
    color: "#7047e8",
    margin: "10px",
  },

  quizResultButtons: {
    display: "flex",
    justifyContent: "center",
    gap: "12px",
    marginTop: "25px",
    flexWrap: "wrap",
  },
};

export default App;