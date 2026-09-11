import { useEffect, useMemo, useState } from 'react';
import type { FormEvent, ReactNode } from 'react';

const API = 'http://localhost:8000';

type User = {
  id: number;
  email: string;
};

type Profile = {
  user_id: number;
  email: string;
  full_name: string;
  phone: string;
  branch: string;
  education_level: string;
  college: string;
  graduation_year: number | null;
  target_career: string;
  bio: string;
};

const branches = [
  'Computer Science & IT',
  'AI / Machine Learning',
  'Data Science & Analytics',
  'Cybersecurity',
  'Cloud & DevOps',
  'Civil Engineering',
  'Mechanical Engineering',
  'Electrical Engineering',
  'Electronics & Communication',
  'Architecture',
  'Robotics & Automation',
  'Business & Management',
  'Finance & Accounting',
  'HR',
  'Digital Marketing & SEO',
];

const careerOptions = [
  'Software Developer',
  'Full Stack Developer',
  'Data Analyst',
  'Data Scientist',
  'AI/ML Engineer',
  'Cybersecurity',
  'Cloud Engineer',
  'DevOps Engineer',
  'UI/UX Designer',
  'Civil Engineer',
  'Mechanical Engineer',
  'Electrical Engineer',
  'Electronics Engineer',
  'Business Analyst',
  'Finance',
];

async function api(path: string, options: RequestInit = {}) {
  const token = localStorage.getItem('skillup_token');

  const headers = new Headers(options.headers);

  if (!headers.has('Content-Type')) {
    headers.set('Content-Type', 'application/json');
  }

  if (token) {
    headers.set('Authorization', `Bearer ${token}`);
  }

  const response = await fetch(`${API}${path}`, {
    ...options,
    headers,
  });

  const text = await response.text();

  let data: any;

  try {
    data = text ? JSON.parse(text) : null;
  } catch {
    data = text;
  }

  if (!response.ok) {
    throw new Error(
      data?.detail ||
        data?.message ||
        `Request failed (${response.status})`
    );
  }

  return data;
}

function Logo() {
  return (
    <div className="logo">
      <div className="logoMark">S</div>

      <div>
        <b>Skill Up AI</b>
        <span>Learn. Build. Grow.</span>
      </div>
    </div>
  );
}

function Auth({
  mode,
  onDone,
  onSwitch,
}: {
  mode: 'login' | 'signup';
  onDone: (user: User) => void;
  onSwitch: (mode: 'login' | 'signup') => void;
}) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState('');

  const signup = mode === 'signup';

  async function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();

    setErr('');
    setBusy(true);

    try {
      const data = await api(
        `/api/auth/${signup ? 'signup' : 'login'}`,
        {
          method: 'POST',
          body: JSON.stringify({
            email,
            password,
          }),
        }
      );

      localStorage.setItem(
        'skillup_token',
        data.access_token
      );

      onDone(data.user);
    } catch (error) {
      setErr(
        error instanceof Error
          ? error.message
          : 'Unable to complete request'
      );
    } finally {
      setBusy(false);
    }
  }

  return (
    <div className="authPage">
      <div className="authCard">
        <Logo />

        <div className="authCopy">
          <h1>
            {signup
              ? 'Create your account'
              : 'Welcome back'}
          </h1>

          <p>
            {signup
              ? 'Start your personalized learning journey.'
              : 'Continue your learning journey.'}
          </p>
        </div>

        {signup && (
          <div className="notice">
            🔐 Create your account with an email address
            and password. Your password is securely hashed
            and can be used to log in again later.
          </div>
        )}

        <form onSubmit={submit}>
          <label htmlFor="email">
            Email address
          </label>

          <input
            id="email"
            type="email"
            value={email}
            onChange={(event) =>
              setEmail(event.target.value)
            }
            placeholder="you@example.com"
            required
          />

          <label htmlFor="password">
            Password
          </label>

          <input
            id="password"
            type="password"
            value={password}
            onChange={(event) =>
              setPassword(event.target.value)
            }
            placeholder="At least 8 characters"
            minLength={8}
            maxLength={72}
            required
          />

          {err && (
            <div className="error">{err}</div>
          )}

          <button
            type="submit"
            className="primary"
            disabled={busy}
          >
            {busy
              ? 'Please wait…'
              : signup
              ? 'Create account'
              : 'Continue'}

            <span>→</span>
          </button>
        </form>

        <div className="terms">
          By continuing, you agree to Skill Up AI's
          Terms and Privacy Policy.
        </div>

        <button
          type="button"
          className="linkBtn"
          onClick={() =>
            onSwitch(
              signup ? 'login' : 'signup'
            )
          }
        >
          {signup
            ? 'Already have an account? Log in'
            : 'New to Skill Up AI? Create an account'}
        </button>
      </div>
    </div>
  );
}

function Shell({
  user,
  profile,
  onLogout,
  view,
  setView,
  children,
}: {
  user: User;
  profile: Profile;
  onLogout: () => void;
  view: string;
  setView: (view: string) => void;
  children: ReactNode;
}) {
 const nav = [
  ['dashboard', 'Dashboard', '⌂'],
  ['profile', 'My Profile', '◉'],
  ['learning', 'Learning', '▣'],
  ['resources', 'Resources', '▤'],
  ['ai', 'AI Assistant', '✦'],
  ['interview', 'AI Interview', '◈'],
  ];

  const headingMap: Record<string, string> = {
    dashboard: 'Your learning command center',
    profile: 'Student Profile',
    learning: 'Learning',
    roadmap: 'Roadmap',
    skills: 'Skill Building',
    quiz: 'Quiz',
    resources: 'Resources',
    ai: 'AI Assistant',
    interview: 'AI Interview',
  };

  return (
    <div className="app">
      <aside>
        <Logo />

        <nav>
          {nav.map(([key, label, icon]) => (
            <button
              key={key}
              type="button"
              className={
                view === key ? 'active' : ''
              }
              onClick={() => setView(key)}
            >
              <i>{icon}</i>
              {label}
            </button>
          ))}
        </nav>

        <div className="sideBottom">
          <button
            type="button"
            onClick={() =>
              setView('profile')
            }
          >
            ⚙ Profile settings
          </button>

          <button
            type="button"
            onClick={onLogout}
          >
            ↪ Log out
          </button>
        </div>
      </aside>

      <main>
        <header>
          <div>
            <span className="eyebrow">
              SKILL UP AI
            </span>

            <h2>
              {headingMap[view] || 'Workspace'}
            </h2>
          </div>

          <div className="userPill">
            <span>
              {(profile.full_name || user.email)
                .slice(0, 1)
                .toUpperCase()}
            </span>

            <div>
              <b>
                {profile.full_name ||
                  'Student'}
              </b>
              <small>{user.email}</small>
            </div>
          </div>
        </header>

        {children}
      </main>
    </div>
  );
}

function Dashboard({
  profile,
  setView,
}: {
  profile: Profile;
  setView: (view: string) => void;
}) {
  const completeness = useMemo(() => {
    const values = [
      profile.full_name,
      profile.branch,
      profile.education_level,
      profile.college,
      profile.target_career,
    ];

    return Math.round(
      (values.filter(Boolean).length /
        values.length) *
        100
    );
  }, [profile]);

  return (
    <div className="page">
      <section className="hero">
        <div>
          <span className="pill">
            Student workspace
          </span>

          <h1>
            Hi{' '}
            {profile.full_name?.split(' ')[0] ||
              'there'}{' '}
            👋
          </h1>

          <p>
            Keep your student information ready for
            the learning, roadmap, skill and AI
            modules that connect to Skill Up AI.
          </p>

          <button
            type="button"
            className="primary small"
            onClick={() => setView('profile')}
          >
            {profile.full_name
              ? 'View / edit profile'
              : 'Complete profile'}{' '}
            →
          </button>
        </div>

        <div className="progressRing">
          <strong>{completeness}%</strong>

          <span>
            profile
            <br />
            complete
          </span>
        </div>
      </section>

      <div className="grid3">
        <Stat
          title="Target career"
          value={
            profile.target_career ||
            'Not selected'
          }
          icon="🎯"
        />

        <Stat
          title="Branch"
          value={
            profile.branch || 'Not added'
          }
          icon="🎓"
        />

        <Stat
          title="Account"
          value="Active"
          icon="✓"
        />
      </div>

      <section className="section">
        <div className="sectionHead">
          <div>
            <span className="eyebrow">
              YOUR FOUNDATION
            </span>

            <h3>
              Set up your student profile
            </h3>
          </div>

          <button
            type="button"
            className="textBtn"
            onClick={() => setView('profile')}
          >
            Edit profile →
          </button>
        </div>

        <div className="cardGrid">
          <Feature
            icon="◉"
            title="Student Profile"
            text="Keep your academic background, goals and personal details in one place."
            onClick={() => setView('profile')}
          />

          <Feature
            icon="✦"
            title="Ready for learning"
            text="Open the learning module and continue building your skills."
            onClick={() => setView('learning')}
          />

          <Feature
            icon="◇"
            title="Personalized roadmap"
            text="Open your personalized roadmap and career learning path."
            onClick={() => setView('roadmap')}
          />
        </div>
      </section>
    </div>
  );
}

function Stat({
  title,
  value,
  icon,
}: {
  title: string;
  value: string;
  icon: string;
}) {
  return (
    <div className="stat">
      <span>{icon}</span>
      <small>{title}</small>
      <strong>{value}</strong>
    </div>
  );
}

function Feature({
  icon,
  title,
  text,
  onClick,
}: {
  icon: string;
  title: string;
  text: string;
  onClick: () => void;
}) {
  return (
    <button
      type="button"
      className="feature"
      onClick={onClick}
    >
      <span className="featureIcon">
        {icon}
      </span>

      <div>
        <h4>{title}</h4>
        <p>{text}</p>
      </div>

      <b>→</b>
    </button>
  );
}

function ProfilePage({
  profile,
  setProfile,
}: {
  profile: Profile;
  setProfile: (profile: Profile) => void;
}) {
  const [form, setForm] =
    useState<Profile>(profile);

  const [saved, setSaved] =
    useState('');

  const update = (
    key: keyof Profile,
    value: string | number | null
  ) => {
    setForm((current) => ({
      ...current,
      [key]: value,
    }));
  };

  async function save(
    event: FormEvent<HTMLFormElement>
  ) {
    event.preventDefault();

    try {
      const data = await api(
        '/api/profile',
        {
          method: 'PUT',
          body: JSON.stringify({
            ...form,
            graduation_year:
              form.graduation_year
                ? Number(
                    form.graduation_year
                  )
                : null,
          }),
        }
      );

      setProfile(data);
      setForm(data);
      setSaved(
        'Profile saved successfully.'
      );

      window.setTimeout(() => {
        setSaved('');
      }, 2500);
    } catch (error) {
      setSaved(
        error instanceof Error
          ? error.message
          : 'Unable to save profile'
      );
    }
  }

  return (
    <div className="page">
      <div className="profileTop">
        <div className="avatarBig">
          {(form.full_name || form.email)
            .slice(0, 1)
            .toUpperCase()}
        </div>

        <div>
          <h1>
            {form.full_name ||
              'Complete your profile'}
          </h1>

          <p>{form.email}</p>
        </div>

        <div className="profileBadge">
          Student account
        </div>
      </div>

      <form
        className="formCard"
        onSubmit={save}
      >
        <div className="formHead">
          <div>
            <span className="eyebrow">
              PERSONAL INFORMATION
            </span>

            <h3>
              Your student profile
            </h3>

            <p>
              This information becomes the common
              foundation for future Skill Up AI
              modules.
            </p>
          </div>

          {saved && (
            <span
              className={
                saved.includes('success')
                  ? 'success'
                  : 'error'
              }
            >
              {saved}
            </span>
          )}
        </div>

        <div className="formGrid">
          <Field label="Full name">
            <input
              value={form.full_name}
              onChange={(event) =>
                update(
                  'full_name',
                  event.target.value
                )
              }
              placeholder="Your full name"
            />
          </Field>

          <Field label="Phone">
            <input
              value={form.phone}
              onChange={(event) =>
                update(
                  'phone',
                  event.target.value
                )
              }
              placeholder="Optional"
            />
          </Field>

          <Field label="Education level">
            <select
              value={form.education_level}
              onChange={(event) =>
                update(
                  'education_level',
                  event.target.value
                )
              }
            >
              <option value="">
                Select level
              </option>
              <option>
                B.Tech / B.E.
              </option>
              <option>B.Sc.</option>
              <option>BCA</option>
              <option>
                M.Tech / M.E.
              </option>
              <option>MCA</option>
              <option>Diploma</option>
              <option>Other</option>
            </select>
          </Field>

          <Field label="Branch / field">
            <select
              value={form.branch}
              onChange={(event) =>
                update(
                  'branch',
                  event.target.value
                )
              }
            >
              <option value="">
                Select branch
              </option>

              {branches.map(
                (branch) => (
                  <option
                    key={branch}
                    value={branch}
                  >
                    {branch}
                  </option>
                )
              )}
            </select>
          </Field>

          <Field label="College / institution">
            <input
              value={form.college}
              onChange={(event) =>
                update(
                  'college',
                  event.target.value
                )
              }
              placeholder="College name"
            />
          </Field>

          <Field label="Graduation year">
            <input
              type="number"
              value={
                form.graduation_year ?? ''
              }
              onChange={(event) =>
                update(
                  'graduation_year',
                  event.target.value
                    ? Number(
                        event.target.value
                      )
                    : null
                )
              }
              placeholder="2027"
            />
          </Field>

          <Field
            label="Target career"
            full
          >
            <select
              value={
                form.target_career
              }
              onChange={(event) =>
                update(
                  'target_career',
                  event.target.value
                )
              }
            >
              <option value="">
                Select your target career
              </option>

              {careerOptions.map(
                (career) => (
                  <option
                    key={career}
                    value={career}
                  >
                    {career}
                  </option>
                )
              )}
            </select>
          </Field>

          <Field
            label="About you"
            full
          >
            <textarea
              value={form.bio}
              onChange={(event) =>
                update(
                  'bio',
                  event.target.value
                )
              }
              placeholder="Tell us briefly about your interests, goals or experience…"
              rows={4}
            />
          </Field>
        </div>

        <button
          type="submit"
          className="primary save"
        >
          Save profile
        </button>
      </form>
    </div>
  );
}

function Field({
  label,
  children,
  full = false,
}: {
  label: string;
  children: ReactNode;
  full?: boolean;
}) {
  return (
    <label
      className={full ? 'full' : ''}
    >
      {label}
      {children}
    </label>
  );
}

/* =========================================================
   MODULE FRAME
   ========================================================= */

function ModuleFrame({
  title,
  url,
}: {
  title: string;
  url: string;
}) {
  return (
    <div
      className="page"
      style={{
        padding: '0 24px 24px',
      }}
    >
      <div
        style={{
          width: '100%',
          height:
            'calc(100vh - 145px)',
          minHeight: '650px',
          overflow: 'hidden',
          borderRadius: '18px',
          background: '#ffffff',
          border:
            '1px solid #e7e2f7',
          boxShadow:
            '0 10px 30px rgba(60,40,120,0.06)',
        }}
      >
        <iframe
          title={title}
          src={url}
          style={{
            width: '100%',
            height: '100%',
            border: 'none',
            display: 'block',
          }}
          allow="camera; microphone; display-capture; fullscreen"
          allowFullScreen
        />
      </div>
    </div>
  );
}

/* =========================================================
   MAIN APP
   ========================================================= */

export default function App() {
  const [user, setUser] =
    useState<User | null>(null);

  const [profile, setProfile] =
    useState<Profile | null>(null);

  const [view, setView] =
    useState('dashboard');

  const [auth, setAuth] =
    useState<
      'login' | 'signup' | null
    >(null);

  useEffect(() => {
    const token =
      localStorage.getItem(
        'skillup_token'
      );

    if (!token) {
      setAuth(
        window.location.hash ===
          '#signup'
          ? 'signup'
          : 'login'
      );

      return;
    }

    api('/api/auth/me')
      .then((currentUser: User) => {
        setUser(currentUser);
        return api('/api/profile');
      })
      .then((currentProfile: Profile) => {
        setProfile(currentProfile);
      })
      .catch(() => {
        localStorage.removeItem(
          'skillup_token'
        );

        setUser(null);
        setProfile(null);
        setAuth('login');
      });
  }, []);

  if (!user || !profile) {
    if (!auth) {
      return (
        <div className="loading">
          Loading Skill Up AI…
        </div>
      );
    }

    return (
      <Auth
        mode={auth}
        onDone={async (
          loggedInUser
        ) => {
          setUser(loggedInUser);

          try {
            const currentProfile =
              await api('/api/profile');

            setProfile(
              currentProfile
            );

            setAuth(null);
          } catch (error) {
            setUser(null);

            alert(
              error instanceof Error
                ? error.message
                : 'Unable to load profile'
            );
          }
        }}
        onSwitch={(mode) => {
          setAuth(mode);
          window.location.hash =
            mode;
        }}
      />
    );
  }

  function logout() {
    localStorage.removeItem(
      'skillup_token'
    );

    setUser(null);
    setProfile(null);
    setView('dashboard');
    setAuth('login');

    window.location.hash = '';
  }

  let content: ReactNode;

  switch (view) {
    case 'dashboard':
      content = (
        <Dashboard
          profile={profile}
          setView={setView}
        />
      );
      break;

    case 'profile':
      content = (
        <ProfilePage
          profile={profile}
          setProfile={setProfile}
        />
      );
      break;

    /* =========================
       PART 2
       ========================= */

    case 'learning':
      content = (
        <ModuleFrame
          title="Learning"
          url="http://localhost:5174"
        />
      );
      break;

    case 'roadmap':
      content = (
        <ModuleFrame
          title="Roadmap"
          url="http://localhost:5174"
        />
      );
      break;

    case 'skills':
      content = (
        <ModuleFrame
          title="Skill Building"
          url="http://localhost:5174"
        />
      );
      break;

    case 'quiz':
      content = (
        <ModuleFrame
          title="Quiz"
          url="http://localhost:5174"
        />
      );
      break;

    /* =========================
       PART 3
       ========================= */

    case 'resources':
      content = (
        <ModuleFrame
          title="Resources"
          url="http://localhost:5175"
        />
      );
      break;

    /* =========================
       PART 4
       ========================= */

    case 'ai':
      content = (
        <ModuleFrame
          title="AI Assistant"
          url="http://localhost:5000/ai"
        />
      );
      break;

    case 'interview':
      content = (
        <ModuleFrame
          title="AI Interview"
          url="http://localhost:5000/interview"
        />
      );
      break;

    default:
      content = (
        <Dashboard
          profile={profile}
          setView={setView}
        />
      );
  }

  return (
    <Shell
      user={user}
      profile={profile}
      onLogout={logout}
      view={view}
      setView={setView}
    >
      {content}
    </Shell>
  );
}