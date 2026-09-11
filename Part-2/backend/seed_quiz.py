from database import SessionLocal
from models.roadmap import Skill
from models.quiz import QuizQuestion


# ============================================================
# SkillBridge AI - Complete Quiz Seeder
# ============================================================
#
# This script:
#   1. Keeps existing quiz questions
#   2. Finds all actual skills in the database
#   3. Adds quiz questions for skills without quizzes
#   4. Never deletes existing questions
#   5. Never creates duplicate questions
#
# ============================================================


# ============================================================
# Curated questions for important skills
# ============================================================

QUIZ_DATA = {

    "Programming Logic": [
        {
            "question": "Which programming construct is commonly used to make a decision?",
            "options": ["if statement", "import statement", "print statement", "comment"],
            "answer": "if statement"
        },
        {
            "question": "Which structure is commonly used to repeat a block of code?",
            "options": ["loop", "variable", "class", "package"],
            "answer": "loop"
        },
        {
            "question": "What is the main goal of programming logic?",
            "options": [
                "Solving problems systematically",
                "Changing computer hardware",
                "Designing logos",
                "Managing electricity"
            ],
            "answer": "Solving problems systematically"
        }
    ],

    "Data Structures": [
        {
            "question": "Which data structure follows LIFO?",
            "options": ["Stack", "Queue", "Array", "Graph"],
            "answer": "Stack"
        },
        {
            "question": "Which data structure follows FIFO?",
            "options": ["Queue", "Stack", "Tree", "Heap"],
            "answer": "Queue"
        },
        {
            "question": "Which data structure stores elements using nodes and links?",
            "options": ["Linked List", "Array", "String", "Integer"],
            "answer": "Linked List"
        }
    ],

    "Algorithms": [
        {
            "question": "What is an algorithm?",
            "options": [
                "A step-by-step procedure for solving a problem",
                "A computer monitor",
                "A database table",
                "A programming language"
            ],
            "answer": "A step-by-step procedure for solving a problem"
        },
        {
            "question": "Which algorithm is commonly used for finding the shortest path?",
            "options": ["Dijkstra's algorithm", "Bubble sort", "Binary search", "Selection sort"],
            "answer": "Dijkstra's algorithm"
        },
        {
            "question": "What does algorithm complexity describe?",
            "options": [
                "Resource usage as input size grows",
                "Screen resolution",
                "File format",
                "Keyboard layout"
            ],
            "answer": "Resource usage as input size grows"
        }
    ],

    "Object Oriented Programming": [
        {
            "question": "Which concept allows a class to inherit properties from another class?",
            "options": ["Inheritance", "Compilation", "Iteration", "Recursion"],
            "answer": "Inheritance"
        },
        {
            "question": "Which concept hides internal implementation details?",
            "options": ["Encapsulation", "Looping", "Sorting", "Parsing"],
            "answer": "Encapsulation"
        },
        {
            "question": "Which concept allows the same interface to have different implementations?",
            "options": ["Polymorphism", "Iteration", "Indexing", "Compilation"],
            "answer": "Polymorphism"
        }
    ],

    "DBMS": [
        {
            "question": "What does DBMS stand for?",
            "options": [
                "Database Management System",
                "Data Backup Management Software",
                "Database Machine Service",
                "Digital Business Management System"
            ],
            "answer": "Database Management System"
        },
        {
            "question": "Which language is commonly used to query relational databases?",
            "options": ["SQL", "HTML", "CSS", "XML"],
            "answer": "SQL"
        },
        {
            "question": "What is a primary key used for?",
            "options": [
                "Uniquely identifying a record",
                "Formatting a webpage",
                "Compressing files",
                "Running an operating system"
            ],
            "answer": "Uniquely identifying a record"
        }
    ],

    "Python": [
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["function", "def", "fun", "define"],
            "answer": "def"
        },
        {
            "question": "Which data type stores multiple ordered items?",
            "options": ["list", "integer", "boolean", "float"],
            "answer": "list"
        },
        {
            "question": "Which symbol is used for a comment in Python?",
            "options": ["//", "/*", "#", "--"],
            "answer": "#"
        }
    ],

    "Java": [
        {
            "question": "Which keyword is used to create a class in Java?",
            "options": ["class", "struct", "object", "define"],
            "answer": "class"
        },
        {
            "question": "Which method is the common entry point of a Java application?",
            "options": ["main()", "start()", "run()", "execute()"],
            "answer": "main()"
        },
        {
            "question": "Which keyword is used to inherit a class in Java?",
            "options": ["extends", "inherits", "implements", "superclass"],
            "answer": "extends"
        }
    ],

    "JavaScript": [
        {
            "question": "Which keyword can declare a block-scoped variable in JavaScript?",
            "options": ["let", "define", "varname", "variable"],
            "answer": "let"
        },
        {
            "question": "Which method converts JSON text into a JavaScript object?",
            "options": ["JSON.parse()", "JSON.convert()", "JSON.object()", "JSON.read()"],
            "answer": "JSON.parse()"
        },
        {
            "question": "Which symbol starts a single-line comment in JavaScript?",
            "options": ["//", "#", "<!--", "**"],
            "answer": "//"
        }
    ],

    "SQL": [
        {
            "question": "Which SQL command is used to retrieve data?",
            "options": ["SELECT", "GET", "FETCHDATA", "READ"],
            "answer": "SELECT"
        },
        {
            "question": "Which SQL clause filters rows?",
            "options": ["WHERE", "FILTER", "LIMITBY", "CHECK"],
            "answer": "WHERE"
        },
        {
            "question": "Which SQL command adds new records?",
            "options": ["INSERT", "ADD", "CREATE ROW", "APPEND"],
            "answer": "INSERT"
        }
    ],

    "HTML": [
        {
            "question": "What does HTML stand for?",
            "options": [
                "HyperText Markup Language",
                "HighText Machine Language",
                "Hyperlink Text Management Language",
                "Home Tool Markup Language"
            ],
            "answer": "HyperText Markup Language"
        },
        {
            "question": "Which tag creates a hyperlink?",
            "options": ["<a>", "<link>", "<href>", "<url>"],
            "answer": "<a>"
        },
        {
            "question": "Which tag is commonly used for the largest heading?",
            "options": ["<h1>", "<head>", "<title>", "<header>"],
            "answer": "<h1>"
        }
    ],

    "CSS": [
        {
            "question": "What is CSS mainly used for?",
            "options": [
                "Styling web pages",
                "Managing databases",
                "Running servers",
                "Writing SQL queries"
            ],
            "answer": "Styling web pages"
        },
        {
            "question": "Which property changes text color?",
            "options": ["color", "font-color", "text-style", "foreground"],
            "answer": "color"
        },
        {
            "question": "Which CSS layout system is useful for one-dimensional layouts?",
            "options": ["Flexbox", "SQL", "DOM", "JSON"],
            "answer": "Flexbox"
        }
    ],

    "React": [
        {
            "question": "React is primarily used to build what?",
            "options": [
                "User interfaces",
                "Operating systems",
                "Databases",
                "Network cables"
            ],
            "answer": "User interfaces"
        },
        {
            "question": "Which syntax is commonly used to write UI markup in React?",
            "options": ["JSX", "SQL", "XML-only", "CSSX"],
            "answer": "JSX"
        },
        {
            "question": "Which React Hook is commonly used for component state?",
            "options": ["useState", "useStyle", "useClass", "useData"],
            "answer": "useState"
        }
    ],

    "Git": [
        {
            "question": "What is Git primarily used for?",
            "options": [
                "Version control",
                "Image editing",
                "Database hosting",
                "Video streaming"
            ],
            "answer": "Version control"
        },
        {
            "question": "Which command creates a new Git repository?",
            "options": ["git init", "git start", "git new", "git create"],
            "answer": "git init"
        },
        {
            "question": "Which command records changes in Git?",
            "options": ["git commit", "git save", "git record", "git store"],
            "answer": "git commit"
        }
    ],

    "GitHub": [
        {
            "question": "GitHub is primarily used for what?",
            "options": [
                "Hosting and collaborating on software projects",
                "Editing videos",
                "Creating spreadsheets",
                "Designing buildings"
            ],
            "answer": "Hosting and collaborating on software projects"
        },
        {
            "question": "What is a GitHub repository?",
            "options": [
                "A project containing files and version history",
                "A computer processor",
                "A database server",
                "A design template"
            ],
            "answer": "A project containing files and version history"
        },
        {
            "question": "What is a pull request commonly used for?",
            "options": [
                "Proposing code changes for review",
                "Deleting an operating system",
                "Creating a database",
                "Formatting a hard disk"
            ],
            "answer": "Proposing code changes for review"
        }
    ],

    "Software Testing": [
        {
            "question": "What is the main purpose of software testing?",
            "options": [
                "Finding defects and verifying behavior",
                "Designing logos",
                "Increasing monitor size",
                "Writing advertisements"
            ],
            "answer": "Finding defects and verifying behavior"
        },
        {
            "question": "Which testing checks an individual unit of code?",
            "options": ["Unit testing", "System testing", "Load testing", "Acceptance testing"],
            "answer": "Unit testing"
        },
        {
            "question": "What is regression testing?",
            "options": [
                "Testing that existing functionality still works after changes",
                "Testing only new hardware",
                "Testing internet speed",
                "Testing database storage size"
            ],
            "answer": "Testing that existing functionality still works after changes"
        }
    ],

    "Debugging": [
        {
            "question": "What is debugging?",
            "options": [
                "Finding and fixing software errors",
                "Creating databases",
                "Designing graphics",
                "Installing hardware"
            ],
            "answer": "Finding and fixing software errors"
        },
        {
            "question": "Which tool is commonly used to inspect program execution?",
            "options": ["Debugger", "Compiler only", "Browser history", "File manager"],
            "answer": "Debugger"
        },
        {
            "question": "What should developers generally do first when debugging a problem?",
            "options": [
                "Reproduce and understand the problem",
                "Delete the project",
                "Replace the computer",
                "Disable all software"
            ],
            "answer": "Reproduce and understand the problem"
        }
    ],

    "Excel": [
        {
            "question": "What is Excel mainly used for?",
            "options": [
                "Spreadsheets and data analysis",
                "Operating system development",
                "Network routing",
                "Video editing"
            ],
            "answer": "Spreadsheets and data analysis"
        },
        {
            "question": "Which symbol normally starts a formula in Excel?",
            "options": ["=", "#", "$", "@"],
            "answer": "="
        },
        {
            "question": "Which function calculates the average of values?",
            "options": ["AVERAGE", "MEANVALUE", "AVGDATA", "MID"],
            "answer": "AVERAGE"
        }
    ],

    "GitHub Actions": [
        {
            "question": "What is GitHub Actions primarily used for?",
            "options": [
                "Automating software workflows",
                "Editing images",
                "Managing databases manually",
                "Designing websites only"
            ],
            "answer": "Automating software workflows"
        },
        {
            "question": "GitHub Actions is commonly used to implement what?",
            "options": ["CI/CD", "CAD", "CRM", "GIS"],
            "answer": "CI/CD"
        },
        {
            "question": "Where are GitHub Actions workflows commonly defined?",
            "options": [
                ".github/workflows",
                "src/actions",
                "actions.json",
                "github.config"
            ],
            "answer": ".github/workflows"
        }
    ],

    "Docker": [
        {
            "question": "What is Docker primarily used for?",
            "options": [
                "Containerizing applications",
                "Designing buildings",
                "Editing spreadsheets",
                "Writing SQL only"
            ],
            "answer": "Containerizing applications"
        },
        {
            "question": "What is a Docker image?",
            "options": [
                "A packaged template used to create containers",
                "A photograph",
                "A database row",
                "A network cable"
            ],
            "answer": "A packaged template used to create containers"
        },
        {
            "question": "Which command lists running Docker containers?",
            "options": [
                "docker ps",
                "docker list-images",
                "docker running",
                "docker show"
            ],
            "answer": "docker ps"
        }
    ],

    "Machine Learning": [
        {
            "question": "Which type of learning uses labeled training data?",
            "options": [
                "Supervised learning",
                "Unsupervised learning",
                "Random learning",
                "Manual learning"
            ],
            "answer": "Supervised learning"
        },
        {
            "question": "Which task predicts a continuous numeric value?",
            "options": [
                "Regression",
                "Classification",
                "Clustering",
                "Association"
            ],
            "answer": "Regression"
        },
        {
            "question": "Which library is widely used for traditional machine learning in Python?",
            "options": [
                "Scikit-learn",
                "React",
                "Django",
                "Bootstrap"
            ],
            "answer": "Scikit-learn"
        }
    ],

    "Artificial Intelligence": [
        {
            "question": "What is a major goal of artificial intelligence?",
            "options": [
                "Building systems that perform tasks requiring intelligence",
                "Only storing files",
                "Only designing webpages",
                "Only editing images"
            ],
            "answer": "Building systems that perform tasks requiring intelligence"
        },
        {
            "question": "Which field is commonly considered part of AI?",
            "options": [
                "Machine Learning",
                "Spreadsheet formatting",
                "Word processing",
                "File compression"
            ],
            "answer": "Machine Learning"
        },
        {
            "question": "Which technology is commonly used to understand human language?",
            "options": [
                "Natural Language Processing",
                "CAD",
                "DNS",
                "Spreadsheet formulas"
            ],
            "answer": "Natural Language Processing"
        }
    ],

    "Data Science": [
        {
            "question": "Which activity is commonly part of data science?",
            "options": [
                "Data analysis and modeling",
                "Circuit soldering only",
                "Building construction only",
                "Video recording only"
            ],
            "answer": "Data analysis and modeling"
        },
        {
            "question": "Which Python library is widely used for tabular data?",
            "options": ["Pandas", "React", "Flask", "TensorFlow.js"],
            "answer": "Pandas"
        },
        {
            "question": "Which field helps measure uncertainty in data?",
            "options": ["Statistics", "HTML", "CSS", "Git"],
            "answer": "Statistics"
        }
    ],

    "Cybersecurity Fundamentals": [
        {
            "question": "What is a major goal of cybersecurity?",
            "options": [
                "Protecting systems and information",
                "Designing logos",
                "Editing videos",
                "Creating spreadsheets"
            ],
            "answer": "Protecting systems and information"
        },
        {
            "question": "Which principle protects information from unauthorized disclosure?",
            "options": [
                "Confidentiality",
                "Compilation",
                "Iteration",
                "Rendering"
            ],
            "answer": "Confidentiality"
        },
        {
            "question": "Which tool is commonly used for network packet analysis?",
            "options": ["Wireshark", "Excel", "Figma", "Blender"],
            "answer": "Wireshark"
        }
    ]
}


# ============================================================
# Generic fallback questions
# ============================================================
#
# Some of the 414 skills are specialized tools or subjects.
# If a skill does not have curated questions above, these
# questions make sure that the skill still has a quiz.
#
# ============================================================

def create_fallback_questions(skill_name):
    return [
        {
            "question": f"Which topic is this question assessing?",
            "options": [
                skill_name,
                "Unrelated Topic A",
                "Unrelated Topic B",
                "Unrelated Topic C"
            ],
            "answer": skill_name
        },
        {
            "question": f"Which option represents the skill '{skill_name}'?",
            "options": [
                "General Computer Hardware",
                skill_name,
                "Unrelated Business Topic",
                "Unrelated Design Topic"
            ],
            "answer": skill_name
        },
        {
            "question": f"Which skill should a learner study to improve their knowledge of '{skill_name}'?",
            "options": [
                "Basic Cooking",
                "Sports Training",
                skill_name,
                "Music Theory"
            ],
            "answer": skill_name
        }
    ]


# ============================================================
# Convert options to database columns
# ============================================================

def add_question(db, skill_id, question_data):
    existing = (
        db.query(QuizQuestion)
        .filter(
            QuizQuestion.skill_id == skill_id,
            QuizQuestion.question == question_data["question"]
        )
        .first()
    )

    if existing:
        return False

    options = question_data["options"]

    question = QuizQuestion(
        skill_id=skill_id,
        question=question_data["question"],
        option_a=options[0],
        option_b=options[1],
        option_c=options[2],
        option_d=options[3],
        correct_answer=question_data["answer"]
    )

    db.add(question)

    return True


# ============================================================
# MAIN
# ============================================================

def main():

    db = SessionLocal()

    questions_added = 0
    questions_skipped = 0
    skills_with_quizzes = 0
    skills_without_quizzes = []

    try:

        skills = (
            db.query(Skill)
            .order_by(Skill.id)
            .all()
        )

        print("=" * 70)
        print("SkillBridge AI Quiz Database")
        print("=" * 70)

        print("Skills found:", len(skills))
        print()

        for skill in skills:

            # ------------------------------------------------
            # Check whether this skill already has questions
            # ------------------------------------------------

            existing_count = (
                db.query(QuizQuestion)
                .filter(
                    QuizQuestion.skill_id == skill.id
                )
                .count()
            )

            # If questions already exist, keep them.
            if existing_count > 0:

                skills_with_quizzes += 1

                print(
                    f"SKIP  | {skill.id:3} | "
                    f"{skill.name} | "
                    f"{existing_count} existing questions"
                )

                continue

            # ------------------------------------------------
            # Get curated questions if available
            # ------------------------------------------------

            if skill.name in QUIZ_DATA:

                quiz_questions = QUIZ_DATA[skill.name]

            else:

                quiz_questions = create_fallback_questions(
                    skill.name
                )

            # ------------------------------------------------
            # Add questions
            # ------------------------------------------------

            skill_added = 0

            for question_data in quiz_questions:

                added = add_question(
                    db,
                    skill.id,
                    question_data
                )

                if added:

                    questions_added += 1
                    skill_added += 1

                else:

                    questions_skipped += 1

            if skill_added > 0:

                skills_with_quizzes += 1

                print(
                    f"ADD   | {skill.id:3} | "
                    f"{skill.name} | "
                    f"{skill_added} questions"
                )

            else:

                skills_without_quizzes.append(
                    skill.name
                )

        # ----------------------------------------------------
        # Save everything
        # ----------------------------------------------------

        db.commit()

        total_questions = (
            db.query(QuizQuestion).count()
        )

        skills_with_questions = 0

        for skill in skills:

            count = (
                db.query(QuizQuestion)
                .filter(
                    QuizQuestion.skill_id == skill.id
                )
                .count()
            )

            if count > 0:
                skills_with_questions += 1

        print()
        print("=" * 70)
        print("QUIZ SEEDING COMPLETED")
        print("=" * 70)

        print(
            "Questions added      :",
            questions_added
        )

        print(
            "Questions skipped    :",
            questions_skipped
        )

        print(
            "Total questions      :",
            total_questions
        )

        print(
            "Skills with quizzes  :",
            skills_with_questions
        )

        print(
            "Skills without quiz :",
            len(skills) - skills_with_questions
        )

        if skills_without_quizzes:

            print()
            print("Skills without quizzes:")

            for name in skills_without_quizzes:
                print("  -", name)

        print("=" * 70)

    except Exception as e:

        db.rollback()

        print()
        print("=" * 70)
        print("ERROR")
        print("=" * 70)
        print(e)
        print("=" * 70)

        raise

    finally:

        db.close()


if __name__ == "__main__":
    main()