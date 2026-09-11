import os

from flask import Blueprint, render_template, request, jsonify
from dotenv import load_dotenv
from groq import Groq


load_dotenv()


part4 = Blueprint(
    "part4",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/part4-static"
)


# ============================================================
# GROQ
# ============================================================

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_MODEL = os.getenv(
    "GROQ_MODEL",
    "openai/gpt-oss-20b"
)


client = (
    Groq(api_key=GROQ_API_KEY)
    if GROQ_API_KEY
    else None
)


# ============================================================
# AI ASSISTANT PAGE
# ============================================================

@part4.route("/ai")
def ai_page():

    return render_template("ai.html")


# ============================================================
# INTERVIEW PAGE
# ============================================================

@part4.route("/interview")
def interview_page():

    return render_template("interview.html")


# ============================================================
# AI TUTOR
# ============================================================

@part4.route(
    "/api/tutor",
    methods=["POST"]
)
def tutor():

    data = request.get_json() or {}

    message = (
        data.get("message") or ""
    ).strip()

    history = data.get(
        "history",
        []
    )

    if not message:

        return jsonify({
            "error": "Please enter a question."
        }), 400


    if not client:

        return jsonify({
            "error":
                "GROQ_API_KEY is missing."
        }), 500


    system_prompt = """
You are Skill Up AI, a friendly personal learning tutor.

You teach students like a patient human teacher.

IMPORTANT:

- Answer exactly what the student asks.
- Keep simple questions short.
- Do not give a huge lesson unless the student asks for detail.
- Use simple English.
- Be conversational and natural.
- Give one simple example when useful.
- If the student asks "why", answer why directly.
- If the student asks "how", explain how directly.
- If the student asks for more detail, then explain more.
- If the student says "I don't understand", simplify the explanation.
- For coding problems, explain the problem and show a small corrected example.
- Do not overload the student with unnecessary headings or tables.
- Never behave like a textbook.

Example:

Student:
What is networking?

Good answer:
"Networking is the way computers and other devices communicate
and share data with each other. For example, your phone uses
networking when it connects to the internet."

Keep the response appropriate to the question.
"""


    messages = [

        {
            "role": "system",
            "content": system_prompt
        }

    ]


    # Previous conversation
    if isinstance(history, list):

        for item in history[-12:]:

            if not isinstance(item, dict):
                continue

            role = item.get("role")
            content = item.get("content")

            if (
                role in ["user", "assistant"]
                and content
            ):

                messages.append({
                    "role": role,
                    "content": content
                })


    messages.append({

        "role": "user",

        "content": message

    })


    try:

        response = client.chat.completions.create(

            model=GROQ_MODEL,

            messages=messages,

            temperature=0.4,

            max_tokens=500,

            include_reasoning=False
        )


        answer = (
            response
            .choices[0]
            .message
            .content
            .strip()
        )


        return jsonify({
            "answer": answer
        })


    except Exception as e:

        print(
            "TUTOR ERROR:",
            e
        )


        return jsonify({
            "error":
                "Unable to connect to the AI."
        }), 500


# ============================================================
# START INTERVIEW
# ============================================================

@part4.route(
    "/api/interview/start",
    methods=["POST"]
)
def start_interview():

    data = request.get_json() or {}

    career = (
        data.get(
            "career",
            "Software Engineer"
        )
    )

    skill = (
        data.get(
            "skill",
            "Python"
        )
    )

    level = (
        data.get(
            "level",
            "Beginner"
        )
    )


    if not client:

        return jsonify({
            "error":
                "GROQ_API_KEY is missing."
        }), 500


    system_prompt = f"""
You are the interviewer for Skill Up AI.

Conduct a realistic one-on-one mock interview.

Career:
{career}

Main skill:
{skill}

Difficulty:
{level}

RULES:

1. Ask exactly ONE question.
2. Do not provide the answer.
3. Keep it relevant to the selected career and skill.
4. Start naturally.
5. Sound like a real interviewer.
6. Keep the question concise.
7. Do not use unnecessary markdown.
8. Do not ask multiple questions.
"""


    try:

        response = client.chat.completions.create(

            model=GROQ_MODEL,

            messages=[

                {
                    "role": "system",
                    "content": system_prompt
                },

                {
                    "role": "user",
                    "content":
                        "Start the interview."
                }

            ],

            temperature=0.5,

            max_tokens=200,

            include_reasoning=False
        )


        question = (
            response
            .choices[0]
            .message
            .content
            .strip()
        )


        return jsonify({
            "question": question
        })


    except Exception as e:

        print(
            "INTERVIEW START ERROR:",
            e
        )


        return jsonify({
            "error":
                "Unable to start interview."
        }), 500


# ============================================================
# INTERVIEW NEXT QUESTION
# ============================================================

@part4.route(
    "/api/interview/next",
    methods=["POST"]
)
def next_question():

    data = request.get_json() or {}

    career = data.get(
        "career",
        "Software Engineer"
    )

    skill = data.get(
        "skill",
        "Python"
    )

    level = data.get(
        "level",
        "Beginner"
    )

    history = data.get(
        "history",
        []
    )


    if not client:

        return jsonify({
            "error":
                "GROQ_API_KEY is missing."
        }), 500


    system_prompt = f"""
You are conducting a realistic mock interview.

Career:
{career}

Skill:
{skill}

Difficulty:
{level}

RULES:

- Ask exactly ONE next question.
- Read the candidate's previous answer.
- Ask a natural follow-up when appropriate.
- Gradually increase difficulty.
- Do not repeat questions.
- Do not give the answer.
- Keep the response concise.
- Sound like a real professional interviewer.
"""


    messages = [

        {
            "role": "system",
            "content": system_prompt
        }

    ]


    if isinstance(history, list):

        for item in history[-16:]:

            if not isinstance(item, dict):
                continue

            role = item.get("role")
            content = item.get("content")

            if (
                role in ["user", "assistant"]
                and content
            ):

                messages.append({

                    "role": role,

                    "content": content

                })


    try:

        response = client.chat.completions.create(

            model=GROQ_MODEL,

            messages=messages,

            temperature=0.5,

            max_tokens=220,

            include_reasoning=False
        )


        question = (
            response
            .choices[0]
            .message
            .content
            .strip()
        )


        return jsonify({

            "question": question

        })


    except Exception as e:

        print(
            "NEXT QUESTION ERROR:",
            e
        )


        return jsonify({
            "error":
                "Unable to generate next question."
        }), 500


# ============================================================
# INTERVIEW FEEDBACK
# ============================================================

@part4.route(
    "/api/interview/feedback",
    methods=["POST"]
)
def interview_feedback():

    data = request.get_json() or {}

    career = data.get(
        "career",
        "Software Engineer"
    )

    skill = data.get(
        "skill",
        "Python"
    )

    history = data.get(
        "history",
        []
    )


    if not client:

        return jsonify({
            "error":
                "GROQ_API_KEY is missing."
        }), 500


    system_prompt = f"""
You are an expert interview evaluator.

Evaluate the candidate's completed mock interview.

Career:
{career}

Skill:
{skill}

Provide concise feedback using these sections:

Overall Score:
Communication:
Technical Knowledge:
Strengths:
Areas to Improve:
Better Answers:
Final Advice:

Be constructive and practical.
Do not ask another question.
"""


    messages = [

        {
            "role": "system",
            "content": system_prompt
        }

    ]


    if isinstance(history, list):

        for item in history:

            if not isinstance(item, dict):
                continue

            role = item.get("role")
            content = item.get("content")

            if (
                role in ["user", "assistant"]
                and content
            ):

                messages.append({

                    "role": role,

                    "content": content

                })


    try:

        response = client.chat.completions.create(

            model=GROQ_MODEL,

            messages=messages,

            temperature=0.3,

            max_tokens=700,

            include_reasoning=False
        )


        feedback = (
            response
            .choices[0]
            .message
            .content
            .strip()
        )


        return jsonify({

            "feedback": feedback

        })


    except Exception as e:

        print(
            "FEEDBACK ERROR:",
            e
        )


        return jsonify({
            "error":
                "Unable to generate feedback."
        }), 500