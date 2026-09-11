# Skill Up AI — Part 1

Part 1 is the shared foundation owned by this team member:

- Email/password authentication
- Secure bcrypt password hashing
- JWT authentication/session
- Shared `/api/auth/me` identity endpoint
- Student profile create/read/update
- Dashboard foundation connected to the authenticated student

Career Analysis is **not included** in Part 1. It can be added later as a separate module if the team decides to do so.

## Included dashboard areas

The common dashboard shell exposes connection points for:
- Learning
- Roadmap
- Skill Building
- Quiz
- Resources
- AI Assistant
- AI Interview

These are placeholders for teammates' modules and are intentionally not implemented here.

## Backend
```cmd
cd backend
python -m venv venv
venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

API docs: http://127.0.0.1:8000/docs

## Frontend
Open another terminal:
```cmd
cd frontend
npm install
npm run dev
```

Then open the Vite URL, normally http://localhost:5173.

## API contract for teammates

Authenticated requests use:
`Authorization: Bearer <JWT>`

Backend modules can use:
`from app.auth.dependencies import current_user`

and receive the logged-in user with:
`def endpoint(user: User = Depends(current_user), db: Session = Depends(get_db)):`

Use `user.id` as the shared `user_id` in module tables. Do not create another users table or another login system.

### Authentication
- `POST /api/auth/signup`
- `POST /api/auth/login`
- `GET /api/auth/me`
- `POST /api/auth/logout`

### Student profile
- `GET /api/profile`
- `PUT /api/profile`

### System
- `GET /`
- `GET /api/health`
