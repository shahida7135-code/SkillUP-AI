# Skill Up AI — Part 1 Integration Contract

## What Part 1 owns
1. Email/password authentication
2. Shared user identity and JWT session
3. Student profile
4. Common dashboard shell

## What is NOT in Part 1
Career Analysis has been removed from this version. Other teams can implement it later as an independent module if required.

## What teammates should use
Authenticated API requests carry:
`Authorization: Bearer <JWT>`

Backend modules should import:
`from app.auth.dependencies import current_user`

and receive the user with:
`def endpoint(user: User = Depends(current_user), db: Session = Depends(get_db)):`

Use `user.id` as the foreign-key reference for module data.

## Do not duplicate
- users table
- password storage
- JWT creation
- login/signup screens

## Module namespace recommendation
- `/api/learning/*`
- `/api/roadmap/*`
- `/api/skills/*`
- `/api/quiz/*`
- `/api/resources/*`
- `/api/assistant/*`
- `/api/interview/*`
- `/api/career/*` only if Career Analysis is assigned later
