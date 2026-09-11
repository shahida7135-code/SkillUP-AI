import React from 'react';
import YouTubeVideoList from '../components/youtube/YouTubeVideoList';
import './LearningHub.css';

const quickTopics = [
  { label: 'Python', icon: '🐍', query: 'Python programming for beginners' },
  { label: 'Web Development', icon: '🌐', query: 'web development for beginners' },
  { label: 'AI & ML', icon: '🤖', query: 'AI and machine learning for beginners' },
  { label: 'Cybersecurity', icon: '🔐', query: 'cybersecurity for beginners' },
  { label: 'Data Science', icon: '📊', query: 'data science for beginners' },
  { label: 'Cloud', icon: '☁️', query: 'cloud computing for beginners' },
];

const LearningHub = () => {
  const scrollToVideos = () => {
    document.getElementById('video-resources')?.scrollIntoView({
      behavior: 'smooth',
      block: 'start',
    });
  };

  return (
    <div className="learningHubPage">
      <div className="learningHubContainer">
        {/* HERO */}
        <section className="learningHero">
          <div className="heroText">
            <span className="heroEyebrow">LEARNING RESOURCES</span>
            <h1>Learn something new today.</h1>
            <p>
              Find clear video tutorials, practical guides, and useful lessons
              to build the skills you need for your career.
            </p>

            <button type="button" className="heroButton" onClick={scrollToVideos}>
              Explore video resources <span>→</span>
            </button>
          </div>

          <div className="heroVisual" aria-hidden="true">
            <div className="heroIconMain">▶</div>
            <div className="floatingIcon floatingOne">📚</div>
            <div className="floatingIcon floatingTwo">💡</div>
            <div className="floatingIcon floatingThree">🚀</div>
          </div>
        </section>

        {/* QUICK TOPICS */}
        <section className="topicSection">
          <div className="sectionHeading">
            <div>
              <span className="sectionEyebrow">QUICK START</span>
              <h2>Explore popular skills</h2>
            </div>
            <p>Start with a topic or search for anything you want to learn.</p>
          </div>

          <div className="topicGrid">
            {quickTopics.map((topic) => (
              <button
                type="button"
                className="topicCard"
                key={topic.label}
                onClick={() => {
                  window.dispatchEvent(
                    new CustomEvent('skillbridge-resource-search', {
                      detail: { query: topic.query },
                    })
                  );
                  setTimeout(() => {
                    document
                      .getElementById('video-resources')
                      ?.scrollIntoView({ behavior: 'smooth', block: 'start' });
                  }, 50);
                }}
              >
                <span className="topicIcon">{topic.icon}</span>
                <span className="topicLabel">{topic.label}</span>
                <span className="topicArrow">→</span>
              </button>
            ))}
          </div>
        </section>

        {/* VIDEO RESOURCES */}
        <section className="resourcesSection" id="video-resources">
          <div className="resourcesHeader">
            <div>
              <span className="sectionEyebrow">VIDEO LEARNING</span>
              <h2>Recommended resources</h2>
              <p>
                Search for tutorials and lectures based on the skill you want
                to improve.
              </p>
            </div>

            <div className="resourceCount">
              <span className="countIcon">▶</span>
              <div>
                <strong>YouTube</strong>
                <small>Learning videos</small>
              </div>
            </div>
          </div>

          <div className="videoArea">
            <YouTubeVideoList defaultQuery="Python programming for beginners" />
          </div>
        </section>

        {/* LEARNING TIPS */}
        <section className="tipsSection">
          <div className="sectionHeading tipsHeading">
            <div>
              <span className="sectionEyebrow">MAKE PROGRESS</span>
              <h2>Learn effectively</h2>
            </div>
          </div>

          <div className="tipsGrid">
            <article className="tipCard">
              <span className="tipIcon">📚</span>
              <div>
                <h3>Learn at your pace</h3>
                <p>Choose lessons that match your current level and goals.</p>
              </div>
            </article>

            <article className="tipCard">
              <span className="tipIcon">💡</span>
              <div>
                <h3>Practice what you learn</h3>
                <p>Turn concepts into skills by building small practical projects.</p>
              </div>
            </article>

            <article className="tipCard">
              <span className="tipIcon">🚀</span>
              <div>
                <h3>Keep improving</h3>
                <p>Learn consistently and move from fundamentals to advanced topics.</p>
              </div>
            </article>
          </div>
        </section>
      </div>
    </div>
  );
};

export default LearningHub;
