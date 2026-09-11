import { useEffect, useMemo, useState } from "react";

const API_URL = "http://127.0.0.1:8001";

// ============================================================
// LEARNING HUB
// ============================================================

function LearningHub() {
  const [courses, setCourses] = useState([]);
  const [selectedDepartment, setSelectedDepartment] = useState("");
  const [openResources, setOpenResources] = useState({});
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  // ==========================================================
  // LEARNING AREAS
  // ==========================================================

  const departments = [
    {
      name: "Computer Science & IT",
      icon: "💻",
      shortName: "Computer Science & IT",
    },
    {
      name: "AI & ML",
      icon: "🤖",
      shortName: "AI & Machine Learning",
    },
    {
      name: "Data Science & Analytics",
      icon: "📊",
      shortName: "Data Science & Analytics",
    },
    {
      name: "Cybersecurity",
      icon: "🔐",
      shortName: "Cybersecurity",
    },
    {
      name: "Cloud Computing",
      icon: "☁️",
      shortName: "Cloud Computing",
    },
    {
      name: "DevOps & SRE",
      icon: "⚙️",
      shortName: "DevOps & SRE",
    },
    {
      name: "Web & Full-Stack Development",
      icon: "🌐",
      shortName: "Web & Full-Stack Development",
    },
    {
      name: "Mobile Development",
      icon: "📱",
      shortName: "Mobile Development",
    },
    {
      name: "UI/UX & Product Design",
      icon: "🎨",
      shortName: "UI/UX & Product Design",
    },
    {
      name: "Civil Engineering",
      icon: "🏗️",
      shortName: "Civil Engineering",
    },
    {
      name: "Mechanical Engineering",
      icon: "⚙️",
      shortName: "Mechanical Engineering",
    },
    {
      name: "Electrical Engineering",
      icon: "⚡",
      shortName: "Electrical Engineering",
    },
    {
      name: "Electronics & Communication",
      icon: "📡",
      shortName: "Electronics & Communication",
    },
    {
      name: "Architecture",
      icon: "🏛️",
      shortName: "Architecture",
    },
    {
      name: "Robotics & Automation",
      icon: "🤖",
      shortName: "Robotics & Automation",
    },
    {
      name: "Biotechnology",
      icon: "🧬",
      shortName: "Biotechnology",
    },
    {
      name: "Chemical Engineering",
      icon: "🧪",
      shortName: "Chemical Engineering",
    },
    {
      name: "Business & Management",
      icon: "💼",
      shortName: "Business & Management",
    },
    {
      name: "Finance & Accounting",
      icon: "💰",
      shortName: "Finance & Accounting",
    },
    {
      name: "HR & People",
      icon: "👥",
      shortName: "HR & People",
    },
    {
      name: "Marketing & Digital Marketing",
      icon: "📣",
      shortName: "Marketing & Digital Marketing",
    },
    {
      name: "Content & Creator Skills",
      icon: "🎥",
      shortName: "Content & Creator Skills",
    },
    {
      name: "Freelancing",
      icon: "💻",
      shortName: "Freelancing",
    },
    {
      name: "Entrepreneurship",
      icon: "🚀",
      shortName: "Entrepreneurship",
    },
    {
      name: "Professional & Future Skills",
      icon: "🎯",
      shortName: "Professional & Future Skills",
    },
  ];

  // ==========================================================
  // LOAD SELECTED DEPARTMENT
  // ==========================================================

  async function selectDepartment(department) {
    setSelectedDepartment(department);
    setOpenResources({});
    setLoading(true);
    setError("");

    try {
      const response = await fetch(
        `${API_URL}/courses/department/${encodeURIComponent(
          department
        )}`
      );

      if (!response.ok) {
        throw new Error(
          "Unable to load the selected learning roadmap."
        );
      }

      const data = await response.json();

      setCourses(Array.isArray(data) ? data : []);

      window.scrollTo({
        top: 0,
        behavior: "smooth",
      });
    } catch (err) {
      console.error(err);

      setCourses([]);

      setError(
        "Unable to load this learning roadmap. Please check that the backend is running."
      );
    } finally {
      setLoading(false);
    }
  }

  // ==========================================================
  // BACK TO LEARNING AREAS
  // ==========================================================

  function backToAreas() {
    setSelectedDepartment("");
    setCourses([]);
    setOpenResources({});
    setError("");

    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  }

  // ==========================================================
  // GROUP COURSES BY SKILL
  // ==========================================================

  const topics = useMemo(() => {
    const topicMap = new Map();

    courses
      .slice()
      .sort((a, b) => {
        return Number(a.id || 0) - Number(b.id || 0);
      })
      .forEach((course) => {
        const skillName =
          course.skill || course.title || "Learning Topic";

        if (!topicMap.has(skillName)) {
          topicMap.set(skillName, []);
        }

        topicMap.get(skillName).push(course);
      });

    return Array.from(topicMap.entries()).map(
      ([skill, resources], index) => ({
        step: index + 1,
        skill,
        resources,
      })
    );
  }, [courses]);

  // ==========================================================
  // RESOURCE TOGGLE
  // ==========================================================

  function toggleResources(step) {
    setOpenResources((previous) => ({
      ...previous,
      [step]: !previous[step],
    }));
  }

  // ==========================================================
  // OPEN RESOURCE
  // ==========================================================

  function openResource(url) {
    if (!url) {
      return;
    }

    window.open(
      url,
      "_blank",
      "noopener,noreferrer"
    );
  }

  // ==========================================================
  // HOME / LEARNING AREAS
  // ==========================================================

  if (!selectedDepartment) {
    return (
      <div style={styles.page}>

        {/* ==================================================
            HEADER
        ================================================== */}

        <section style={styles.headerCard}>

          <div style={styles.headerIcon}>
            📚
          </div>

          <h1 style={styles.mainTitle}>
            Explore Learning
          </h1>

          <p style={styles.mainSubtitle}>
            Choose a learning area to discover a
            personalized roadmap and resources.
          </p>

        </section>

        {/* ==================================================
            LEARNING AREAS
        ================================================== */}

        <section style={styles.areaSection}>

          <div style={styles.areaGrid}>

            {departments.map((department) => (

              <button
                key={department.name}
                onClick={() =>
                  selectDepartment(
                    department.name
                  )
                }
                style={styles.areaCard}
              >

                <div style={styles.areaIcon}>
                  {department.icon}
                </div>

                <div style={styles.areaName}>
                  {department.shortName}
                </div>

                <div style={styles.areaArrow}>
                  →
                </div>

              </button>

            ))}

          </div>

        </section>

      </div>
    );
  }

  // ==========================================================
  // SELECTED ROADMAP
  // ==========================================================

  const selectedInfo =
    departments.find(
      (item) =>
        item.name === selectedDepartment
    );

  return (
    <div style={styles.page}>

      {/* ==================================================
          BACK BUTTON
      ================================================== */}

      <button
        onClick={backToAreas}
        style={styles.backButton}
      >
        ← Back to Learning Areas
      </button>

      {/* ==================================================
          ROADMAP HEADER
      ================================================== */}

      <section style={styles.roadmapHeader}>

        <div style={styles.roadmapIcon}>
          {selectedInfo?.icon || "📚"}
        </div>

        <div>

          <p style={styles.eyebrow}>
            PERSONALIZED LEARNING PATH
          </p>

          <h1 style={styles.roadmapTitle}>
            {selectedInfo?.shortName ||
              selectedDepartment}
          </h1>

          <p style={styles.roadmapSubtitle}>
            Follow these topics step by step and
            choose resources for each skill.
          </p>

        </div>

      </section>

      {/* ==================================================
          ERROR
      ================================================== */}

      {error && (
        <div style={styles.error}>
          ⚠️ {error}
        </div>
      )}

      {/* ==================================================
          LOADING
      ================================================== */}

      {loading && (
        <div style={styles.loadingCard}>
          <div style={styles.loadingIcon}>
            ⏳
          </div>

          <h2>
            Building your roadmap...
          </h2>

          <p>
            Loading topics and learning resources.
          </p>
        </div>
      )}

      {/* ==================================================
          ROADMAP
      ================================================== */}

      {!loading && topics.length > 0 && (

        <section style={styles.roadmapSection}>

          <div style={styles.roadmapTop}>

            <div>
              <p style={styles.roadmapLabel}>
                LEARNING ROADMAP
              </p>

              <h2 style={styles.sectionTitle}>
                {topics.length} Topics
              </h2>
            </div>

            <div style={styles.topicCount}>
              {topics.length}
              <span>
                Topics
              </span>
            </div>

          </div>

          {/* ==================================================
              ROADMAP TOPICS
          ================================================== */}

          <div style={styles.timeline}>

            {topics.map((topic) => {

              const isOpen =
                !!openResources[topic.step];

              return (
                <div
                  key={`${topic.skill}-${topic.step}`}
                  style={styles.topicWrapper}
                >

                  {/* TIMELINE LINE */}

                  {topic.step <
                    topics.length && (
                    <div
                      style={styles.timelineLine}
                    />
                  )}

                  {/* STEP NUMBER */}

                  <div style={styles.stepCircle}>
                    {topic.step}
                  </div>

                  {/* TOPIC CARD */}

                  <div style={styles.topicCard}>

                    <div style={styles.topicHeader}>

                      <div>

                        <p style={styles.stepLabel}>
                          STEP {topic.step}
                        </p>

                        <h3
                          style={styles.topicTitle}
                        >
                          {topic.skill}
                        </h3>

                        <p
                          style={
                            styles.topicDescription
                          }
                        >
                          Build your knowledge of{" "}
                          <strong>
                            {topic.skill}
                          </strong>{" "}
                          through practical learning
                          resources.
                        </p>

                      </div>

                      <div style={styles.resourceBadge}>
                        {topic.resources.length}{" "}
                        Resource
                        {topic.resources.length !==
                        1
                          ? "s"
                          : ""}
                      </div>

                    </div>

                    {/* ==================================================
                        RESOURCE BUTTON
                    ================================================== */}

                    <button
                      onClick={() =>
                        toggleResources(
                          topic.step
                        )
                      }
                      style={styles.resourceButton}
                    >
                      📚{" "}
                      {isOpen
                        ? "Hide Resources"
                        : "View Resources"}
                      <span>
                        {isOpen ? "▲" : "▼"}
                      </span>
                    </button>

                    {/* ==================================================
                        RESOURCES
                    ================================================== */}

                    {isOpen && (

                      <div
                        style={
                          styles.resourcesPanel
                        }
                      >

                        <div
                          style={
                            styles.resourcesTitle
                          }
                        >
                          <span>
                            📚
                          </span>

                          <strong>
                            Resources for{" "}
                            {topic.skill}
                          </strong>
                        </div>

                        <div
                          style={
                            styles.resourcesList
                          }
                        >

                          {topic.resources.map(
                            (resource) => (

                              <div
                                key={
                                  resource.id
                                }
                                style={
                                  styles.resourceCard
                                }
                              >

                                <div
                                  style={
                                    styles.resourceInfo
                                  }
                                >

                                  <div
                                    style={
                                      styles.resourceIcon
                                    }
                                  >
                                    {resource.resource_type ===
                                    "Video"
                                      ? "🎥"
                                      : resource.resource_type ===
                                        "Documentation"
                                      ? "📄"
                                      : "📘"}
                                  </div>

                                  <div>

                                    <h4
                                      style={
                                        styles.resourceTitle
                                      }
                                    >
                                      {resource.title}
                                    </h4>

                                    <p
                                      style={
                                        styles.resourceMeta
                                      }
                                    >
                                      {resource.provider ||
                                        "Learning Resource"}

                                      {resource.duration
                                        ? ` • ${resource.duration}`
                                        : ""}
                                    </p>

                                  </div>

                                </div>

                                <button
                                  onClick={() =>
                                    openResource(
                                      resource.url
                                    )
                                  }
                                  style={
                                    styles.openResourceButton
                                  }
                                >
                                  Open →
                                </button>

                              </div>

                            )
                          )}

                        </div>

                      </div>

                    )}

                  </div>

                </div>
              );
            })}

          </div>

        </section>
      )}

      {/* ==================================================
          NO TOPICS
      ================================================== */}

      {!loading &&
        topics.length === 0 && (
          <div style={styles.emptyCard}>

            <div style={styles.emptyIcon}>
              📚
            </div>

            <h2>
              No topics found
            </h2>

            <p>
              Learning resources are not available
              for this area yet.
            </p>

            <button
              onClick={backToAreas}
              style={styles.backMainButton}
            >
              ← Choose Another Area
            </button>

          </div>
        )}

    </div>
  );
}

// ============================================================
// STYLES
// ============================================================

const styles = {

  page: {
    minHeight: "100vh",
    padding: "45px 7%",
    background:
      "linear-gradient(180deg, #f8f7ff 0%, #eef2ff 100%)",
    fontFamily:
      "Arial, Helvetica, sans-serif",
    boxSizing: "border-box",
  },

  // ==========================================================
  // HOME HEADER
  // ==========================================================

  headerCard: {
    textAlign: "center",
    padding: "35px 20px 30px",
  },

  headerIcon: {
    fontSize: "42px",
    marginBottom: "10px",
  },

  mainTitle: {
    margin: "0",
    fontSize: "36px",
    fontWeight: "800",
    color: "#171b2d",
  },

  mainSubtitle: {
    margin: "12px auto 0",
    maxWidth: "650px",
    fontSize: "17px",
    lineHeight: "1.6",
    color: "#667085",
  },

  // ==========================================================
  // AREAS
  // ==========================================================

  areaSection: {
    background: "#ffffff",
    borderRadius: "22px",
    padding: "30px",
    boxShadow:
      "0 10px 35px rgba(31, 41, 55, 0.08)",
  },

  areaGrid: {
    display: "grid",
    gridTemplateColumns:
      "repeat(5, minmax(0, 1fr))",
    gap: "16px",
  },

  areaCard: {
    minHeight: "105px",
    borderRadius: "15px",
    border: "1px solid #e5e7eb",
    background: "#fafbff",
    padding: "18px 14px",
    cursor: "pointer",
    display: "flex",
    flexDirection: "column",
    justifyContent: "center",
    alignItems: "center",
    position: "relative",
    transition:
      "transform 0.2s ease, box-shadow 0.2s ease",
  },

  areaIcon: {
    fontSize: "28px",
    marginBottom: "9px",
  },

  areaName: {
    color: "#344054",
    fontWeight: "700",
    fontSize: "14px",
    lineHeight: "1.3",
    textAlign: "center",
  },

  areaArrow: {
    position: "absolute",
    right: "10px",
    bottom: "8px",
    color: "#7047e8",
    fontWeight: "bold",
  },

  // ==========================================================
  // BACK
  // ==========================================================

  backButton: {
    border: "none",
    background: "transparent",
    color: "#7047e8",
    fontSize: "15px",
    fontWeight: "700",
    cursor: "pointer",
    padding: "8px 0",
    marginBottom: "20px",
  },

  // ==========================================================
  // ROADMAP HEADER
  // ==========================================================

  roadmapHeader: {
    background:
      "linear-gradient(135deg, #ffffff 0%, #f1edff 100%)",
    borderRadius: "22px",
    padding: "35px",
    display: "flex",
    alignItems: "center",
    gap: "22px",
    marginBottom: "25px",
    boxShadow:
      "0 10px 35px rgba(31, 41, 55, 0.08)",
  },

  roadmapIcon: {
    width: "78px",
    height: "78px",
    borderRadius: "20px",
    background: "#7047e8",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    fontSize: "38px",
    flexShrink: 0,
  },

  eyebrow: {
    margin: "0 0 7px",
    color: "#7047e8",
    fontSize: "12px",
    fontWeight: "800",
    letterSpacing: "1.5px",
  },

  roadmapTitle: {
    margin: "0",
    fontSize: "34px",
    color: "#171b2d",
    fontWeight: "800",
  },

  roadmapSubtitle: {
    margin: "10px 0 0",
    color: "#667085",
    fontSize: "16px",
    lineHeight: "1.5",
  },

  // ==========================================================
  // ROADMAP
  // ==========================================================

  roadmapSection: {
    background: "#ffffff",
    borderRadius: "22px",
    padding: "30px",
    boxShadow:
      "0 10px 35px rgba(31, 41, 55, 0.08)",
  },

  roadmapTop: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    marginBottom: "30px",
  },

  roadmapLabel: {
    margin: "0 0 5px",
    color: "#7047e8",
    fontSize: "12px",
    fontWeight: "800",
    letterSpacing: "1.5px",
  },

  sectionTitle: {
    margin: 0,
    fontSize: "28px",
    color: "#171b2d",
  },

  topicCount: {
    width: "75px",
    height: "75px",
    borderRadius: "50%",
    background: "#f0ebff",
    color: "#7047e8",
    fontSize: "25px",
    fontWeight: "800",
    display: "flex",
    flexDirection: "column",
    justifyContent: "center",
    alignItems: "center",
  },

  // ==========================================================
  // TIMELINE
  // ==========================================================

  timeline: {
    position: "relative",
  },

  topicWrapper: {
    position: "relative",
    display: "flex",
    gap: "20px",
    paddingBottom: "25px",
  },

  timelineLine: {
    position: "absolute",
    left: "21px",
    top: "45px",
    bottom: "0",
    width: "2px",
    background: "#ddd6fe",
  },

  stepCircle: {
    width: "44px",
    height: "44px",
    minWidth: "44px",
    borderRadius: "50%",
    background: "#7047e8",
    color: "#ffffff",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    fontWeight: "800",
    fontSize: "16px",
    zIndex: 2,
  },

  // ==========================================================
  // TOPIC
  // ==========================================================

  topicCard: {
    flex: 1,
    background: "#ffffff",
    border: "1px solid #e4e7ec",
    borderRadius: "16px",
    padding: "22px",
    boxShadow:
      "0 4px 15px rgba(16, 24, 40, 0.05)",
  },

  topicHeader: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "flex-start",
    gap: "20px",
  },

  stepLabel: {
    margin: "0 0 6px",
    color: "#7047e8",
    fontSize: "11px",
    fontWeight: "800",
    letterSpacing: "1px",
  },

  topicTitle: {
    margin: 0,
    fontSize: "22px",
    color: "#172033",
  },

  topicDescription: {
    margin: "9px 0 0",
    color: "#667085",
    lineHeight: "1.5",
    fontSize: "14px",
  },

  resourceBadge: {
    background: "#f2f4f7",
    color: "#475467",
    padding: "7px 11px",
    borderRadius: "20px",
    fontSize: "12px",
    fontWeight: "700",
    whiteSpace: "nowrap",
  },

  // ==========================================================
  // RESOURCE BUTTON
  // ==========================================================

  resourceButton: {
    width: "100%",
    marginTop: "20px",
    padding: "13px 16px",
    border: "1px solid #ddd6fe",
    borderRadius: "10px",
    background: "#f7f5ff",
    color: "#5b21b6",
    fontWeight: "700",
    cursor: "pointer",
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    fontSize: "14px",
  },

  // ==========================================================
  // RESOURCE PANEL
  // ==========================================================

  resourcesPanel: {
    marginTop: "14px",
    padding: "18px",
    background: "#f8f9fc",
    borderRadius: "12px",
    border: "1px solid #eaecf0",
  },

  resourcesTitle: {
    display: "flex",
    alignItems: "center",
    gap: "8px",
    color: "#344054",
    marginBottom: "14px",
    fontSize: "14px",
  },

  resourcesList: {
    display: "flex",
    flexDirection: "column",
    gap: "10px",
  },

  resourceCard: {
    background: "#ffffff",
    border: "1px solid #e4e7ec",
    borderRadius: "10px",
    padding: "13px",
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    gap: "15px",
  },

  resourceInfo: {
    display: "flex",
    alignItems: "center",
    gap: "12px",
  },

  resourceIcon: {
    width: "38px",
    height: "38px",
    borderRadius: "9px",
    background: "#f0ebff",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    fontSize: "19px",
  },

  resourceTitle: {
    margin: 0,
    fontSize: "14px",
    color: "#172033",
  },

  resourceMeta: {
    margin: "4px 0 0",
    fontSize: "12px",
    color: "#667085",
  },

  openResourceButton: {
    border: "none",
    borderRadius: "8px",
    background: "#7047e8",
    color: "#ffffff",
    padding: "9px 15px",
    fontWeight: "700",
    cursor: "pointer",
    whiteSpace: "nowrap",
  },

  // ==========================================================
  // LOADING
  // ==========================================================

  loadingCard: {
    background: "#ffffff",
    borderRadius: "18px",
    padding: "60px 20px",
    textAlign: "center",
    boxShadow:
      "0 10px 30px rgba(16, 24, 40, 0.06)",
  },

  loadingIcon: {
    fontSize: "35px",
  },

  // ==========================================================
  // ERROR
  // ==========================================================

  error: {
    background: "#fee4e2",
    color: "#b42318",
    borderRadius: "10px",
    padding: "15px",
    marginBottom: "20px",
  },

  // ==========================================================
  // EMPTY
  // ==========================================================

  emptyCard: {
    background: "#ffffff",
    borderRadius: "18px",
    padding: "70px 20px",
    textAlign: "center",
    boxShadow:
      "0 10px 30px rgba(16, 24, 40, 0.06)",
  },

  emptyIcon: {
    fontSize: "45px",
  },

  backMainButton: {
    marginTop: "15px",
    border: "none",
    borderRadius: "10px",
    background: "#7047e8",
    color: "#ffffff",
    padding: "13px 22px",
    fontWeight: "700",
    cursor: "pointer",
  },
};

export default LearningHub;