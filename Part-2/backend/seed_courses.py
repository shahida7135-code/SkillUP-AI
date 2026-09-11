from database import SessionLocal
from models.course import Course


courses = [

    # =========================================================
    # COMPUTER SCIENCE & IT
    # =========================================================

    {
        "title": "Python Programming",
        "description": "Learn Python programming from basics to practical development.",
        "department": "Computer Science & IT",
        "category": "Programming Languages",
        "skill": "Python",
        "level": "Beginner",
        "provider": "W3Schools",
        "duration": "Self-paced",
        "url": "https://www.w3schools.com/python/"
    },
    {
        "title": "Java Programming",
        "description": "Learn Java programming and object oriented programming.",
        "department": "Computer Science & IT",
        "category": "Programming Languages",
        "skill": "Java",
        "level": "Beginner",
        "provider": "W3Schools",
        "duration": "Self-paced",
        "url": "https://www.w3schools.com/java/"
    },
    {
        "title": "C Programming",
        "description": "Learn C programming fundamentals.",
        "department": "Computer Science & IT",
        "category": "Programming Languages",
        "skill": "C",
        "level": "Beginner",
        "provider": "W3Schools",
        "duration": "Self-paced",
        "url": "https://www.w3schools.com/c/"
    },
    {
        "title": "C++ Programming",
        "description": "Learn C++ programming and OOP concepts.",
        "department": "Computer Science & IT",
        "category": "Programming Languages",
        "skill": "C++",
        "level": "Beginner",
        "provider": "W3Schools",
        "duration": "Self-paced",
        "url": "https://www.w3schools.com/cpp/"
    },
    {
        "title": "C# Programming",
        "description": "Learn C# programming fundamentals.",
        "department": "Computer Science & IT",
        "category": "Programming Languages",
        "skill": "C#",
        "level": "Beginner",
        "provider": "W3Schools",
        "duration": "Self-paced",
        "url": "https://www.w3schools.com/cs/"
    },
    {
        "title": "JavaScript Programming",
        "description": "Learn JavaScript for web development.",
        "department": "Computer Science & IT",
        "category": "Programming Languages",
        "skill": "JavaScript",
        "level": "Beginner",
        "provider": "W3Schools",
        "duration": "Self-paced",
        "url": "https://www.w3schools.com/js/"
    },
    {
        "title": "TypeScript Programming",
        "description": "Learn TypeScript for modern applications.",
        "department": "Computer Science & IT",
        "category": "Programming Languages",
        "skill": "TypeScript",
        "level": "Intermediate",
        "provider": "W3Schools",
        "duration": "Self-paced",
        "url": "https://www.w3schools.com/typescript/"
    },
    {
        "title": "Data Structures",
        "description": "Learn arrays, linked lists, stacks, queues, trees and graphs.",
        "department": "Computer Science & IT",
        "category": "Software Development",
        "skill": "Data Structures",
        "level": "Beginner",
        "provider": "W3Schools",
        "duration": "Self-paced",
        "url": "https://www.w3schools.com/dsa/"
    },
    {
        "title": "SQL",
        "description": "Learn SQL and relational database concepts.",
        "department": "Computer Science & IT",
        "category": "Databases",
        "skill": "SQL",
        "level": "Beginner",
        "provider": "W3Schools",
        "duration": "Self-paced",
        "url": "https://www.w3schools.com/sql/"
    },
    {
        "title": "MySQL",
        "description": "Learn MySQL database fundamentals.",
        "department": "Computer Science & IT",
        "category": "Databases",
        "skill": "MySQL",
        "level": "Beginner",
        "provider": "W3Schools",
        "duration": "Self-paced",
        "url": "https://www.w3schools.com/mysql/"
    },
    {
        "title": "MongoDB",
        "description": "Learn MongoDB and NoSQL database concepts.",
        "department": "Computer Science & IT",
        "category": "Databases",
        "skill": "MongoDB",
        "level": "Intermediate",
        "provider": "W3Schools",
        "duration": "Self-paced",
        "url": "https://www.w3schools.com/mongodb/"
    },
    {
        "title": "Git",
        "description": "Learn Git version control.",
        "department": "Computer Science & IT",
        "category": "Development Tools",
        "skill": "Git",
        "level": "Beginner",
        "provider": "W3Schools",
        "duration": "Self-paced",
        "url": "https://www.w3schools.com/git/"
    },
    {
        "title": "GitHub Skills",
        "description": "Learn GitHub repositories, collaboration and workflows.",
        "department": "Computer Science & IT",
        "category": "Development Tools",
        "skill": "GitHub",
        "level": "Beginner",
        "provider": "GitHub",
        "duration": "Self-paced",
        "url": "https://skills.github.com/"
    },

    # =========================================================
    # WEB & FULL STACK
    # =========================================================

    {
        "title": "HTML",
        "description": "Learn HTML for building web pages.",
        "department": "Web & Full-Stack Development",
        "category": "Frontend",
        "skill": "HTML",
        "level": "Beginner",
        "provider": "W3Schools",
        "duration": "Self-paced",
        "url": "https://www.w3schools.com/html/"
    },
    {
        "title": "CSS",
        "description": "Learn CSS styling and responsive layouts.",
        "department": "Web & Full-Stack Development",
        "category": "Frontend",
        "skill": "CSS",
        "level": "Beginner",
        "provider": "W3Schools",
        "duration": "Self-paced",
        "url": "https://www.w3schools.com/css/"
    },
    {
        "title": "React",
        "description": "Learn React frontend development.",
        "department": "Web & Full-Stack Development",
        "category": "Frontend",
        "skill": "React",
        "level": "Intermediate",
        "provider": "W3Schools",
        "duration": "Self-paced",
        "url": "https://www.w3schools.com/react/"
    },
    {
        "title": "Node.js",
        "description": "Learn backend development using Node.js.",
        "department": "Web & Full-Stack Development",
        "category": "Backend",
        "skill": "Node.js",
        "level": "Intermediate",
        "provider": "W3Schools",
        "duration": "Self-paced",
        "url": "https://www.w3schools.com/nodejs/"
    },
    {
        "title": "Django",
        "description": "Learn Python Django web development.",
        "department": "Web & Full-Stack Development",
        "category": "Backend",
        "skill": "Django",
        "level": "Intermediate",
        "provider": "W3Schools",
        "duration": "Self-paced",
        "url": "https://www.w3schools.com/django/"
    },
    {
        "title": "FastAPI Documentation",
        "description": "Learn FastAPI backend API development.",
        "department": "Web & Full-Stack Development",
        "category": "Backend",
        "skill": "FastAPI",
        "level": "Intermediate",
        "provider": "FastAPI",
        "duration": "Self-paced",
        "url": "https://fastapi.tiangolo.com/tutorial/"
    },
    {
        "title": "Spring Boot",
        "description": "Learn Java Spring Boot backend development.",
        "department": "Web & Full-Stack Development",
        "category": "Backend",
        "skill": "Spring Boot",
        "level": "Intermediate",
        "provider": "Spring",
        "duration": "Self-paced",
        "url": "https://spring.io/guides"
    },

    # =========================================================
    # AI & MACHINE LEARNING
    # =========================================================

    {
        "title": "Artificial Intelligence",
        "description": "Learn fundamental AI concepts.",
        "department": "AI & Machine Learning",
        "category": "AI Fundamentals",
        "skill": "Artificial Intelligence",
        "level": "Beginner",
        "provider": "W3Schools",
        "duration": "Self-paced",
        "url": "https://www.w3schools.com/ai/"
    },
    {
        "title": "Machine Learning",
        "description": "Learn machine learning concepts and algorithms.",
        "department": "AI & Machine Learning",
        "category": "Machine Learning",
        "skill": "Machine Learning",
        "level": "Intermediate",
        "provider": "W3Schools",
        "duration": "Self-paced",
        "url": "https://www.w3schools.com/python/python_ml_getting_started.asp"
    },
    {
        "title": "Deep Learning",
        "description": "Learn neural networks and deep learning.",
        "department": "AI & Machine Learning",
        "category": "Deep Learning",
        "skill": "Deep Learning",
        "level": "Advanced",
        "provider": "PyTorch",
        "duration": "Self-paced",
        "url": "https://pytorch.org/tutorials/"
    },
    {
        "title": "Generative AI",
        "description": "Learn generative AI concepts.",
        "department": "AI & Machine Learning",
        "category": "Generative AI",
        "skill": "Generative AI",
        "level": "Beginner",
        "provider": "W3Schools",
        "duration": "Self-paced",
        "url": "https://www.w3schools.com/gen_ai/"
    },
    {
        "title": "Hugging Face NLP Course",
        "description": "Learn NLP and transformer models.",
        "department": "AI & Machine Learning",
        "category": "Generative AI",
        "skill": "Transformers",
        "level": "Advanced",
        "provider": "Hugging Face",
        "duration": "Self-paced",
        "url": "https://huggingface.co/learn/nlp-course/"
    },

    # =========================================================
    # DATA SCIENCE & ANALYTICS
    # =========================================================

    {
        "title": "Data Science",
        "description": "Learn data science fundamentals.",
        "department": "Data Science & Analytics",
        "category": "Data Science",
        "skill": "Data Science",
        "level": "Beginner",
        "provider": "W3Schools",
        "duration": "Self-paced",
        "url": "https://www.w3schools.com/datascience/"
    },
    {
        "title": "Statistics",
        "description": "Learn statistics for analytics and data science.",
        "department": "Data Science & Analytics",
        "category": "Statistics",
        "skill": "Statistics",
        "level": "Beginner",
        "provider": "W3Schools",
        "duration": "Self-paced",
        "url": "https://www.w3schools.com/statistics/"
    },
    {
        "title": "NumPy",
        "description": "Learn numerical computing using NumPy.",
        "department": "Data Science & Analytics",
        "category": "Python Tools",
        "skill": "NumPy",
        "level": "Intermediate",
        "provider": "W3Schools",
        "duration": "Self-paced",
        "url": "https://www.w3schools.com/python/numpy/"
    },
    {
        "title": "Pandas",
        "description": "Learn data analysis using Pandas.",
        "department": "Data Science & Analytics",
        "category": "Python Tools",
        "skill": "Pandas",
        "level": "Intermediate",
        "provider": "W3Schools",
        "duration": "Self-paced",
        "url": "https://www.w3schools.com/python/pandas/"
    },
    {
        "title": "Excel",
        "description": "Learn Excel for data analysis.",
        "department": "Data Science & Analytics",
        "category": "Analytics",
        "skill": "Excel",
        "level": "Beginner",
        "provider": "W3Schools",
        "duration": "Self-paced",
        "url": "https://www.w3schools.com/excel/"
    },
    {
        "title": "Power BI",
        "description": "Learn business intelligence and dashboards.",
        "department": "Data Science & Analytics",
        "category": "BI Tools",
        "skill": "Power BI",
        "level": "Intermediate",
        "provider": "Microsoft",
        "duration": "Self-paced",
        "url": "https://learn.microsoft.com/en-us/training/powerplatform/power-bi/"
    },

    # =========================================================
    # CYBERSECURITY
    # =========================================================

    {
        "title": "Cybersecurity Fundamentals",
        "description": "Learn cybersecurity concepts and security principles.",
        "department": "Cybersecurity",
        "category": "Fundamentals",
        "skill": "Cyber Security",
        "level": "Beginner",
        "provider": "W3Schools",
        "duration": "Self-paced",
        "url": "https://www.w3schools.com/cybersecurity/"
    },
    {
        "title": "OWASP Top 10",
        "description": "Learn common web application security risks.",
        "department": "Cybersecurity",
        "category": "Application Security",
        "skill": "Application Security",
        "level": "Intermediate",
        "provider": "OWASP",
        "duration": "Self-paced",
        "url": "https://owasp.org/www-project-top-ten/"
    },
    {
        "title": "Kali Linux Documentation",
        "description": "Learn Kali Linux and security tools.",
        "department": "Cybersecurity",
        "category": "Ethical Hacking",
        "skill": "Kali Linux",
        "level": "Intermediate",
        "provider": "Kali Linux",
        "duration": "Self-paced",
        "url": "https://www.kali.org/docs/"
    },

    # =========================================================
    # CLOUD
    # =========================================================

    {
        "title": "AWS Training",
        "description": "Learn AWS cloud services.",
        "department": "Cloud Computing",
        "category": "AWS",
        "skill": "AWS",
        "level": "Beginner",
        "provider": "Amazon Web Services",
        "duration": "Self-paced",
        "url": "https://aws.amazon.com/training/"
    },
    {
        "title": "Azure Training",
        "description": "Learn Microsoft Azure cloud technologies.",
        "department": "Cloud Computing",
        "category": "Azure",
        "skill": "Azure",
        "level": "Beginner",
        "provider": "Microsoft",
        "duration": "Self-paced",
        "url": "https://learn.microsoft.com/en-us/training/azure/"
    },
    {
        "title": "Google Cloud Skills Boost",
        "description": "Learn Google Cloud through hands-on training.",
        "department": "Cloud Computing",
        "category": "GCP",
        "skill": "GCP",
        "level": "Beginner",
        "provider": "Google Cloud",
        "duration": "Self-paced",
        "url": "https://www.cloudskillsboost.google/"
    },

    # =========================================================
    # DEVOPS & SRE
    # =========================================================

    {
        "title": "Docker",
        "description": "Learn containers and Docker.",
        "department": "DevOps & SRE",
        "category": "Containers",
        "skill": "Docker",
        "level": "Beginner",
        "provider": "Docker",
        "duration": "Self-paced",
        "url": "https://docs.docker.com/get-started/"
    },
    {
        "title": "Kubernetes Basics",
        "description": "Learn Kubernetes container orchestration.",
        "department": "DevOps & SRE",
        "category": "Containers",
        "skill": "Kubernetes",
        "level": "Intermediate",
        "provider": "Kubernetes",
        "duration": "Self-paced",
        "url": "https://kubernetes.io/docs/tutorials/kubernetes-basics/"
    },
    {
        "title": "GitHub Actions",
        "description": "Learn CI/CD automation.",
        "department": "DevOps & SRE",
        "category": "CI/CD",
        "skill": "CI/CD",
        "level": "Intermediate",
        "provider": "GitHub",
        "duration": "Self-paced",
        "url": "https://docs.github.com/en/actions"
    },

    # =========================================================
    # MOBILE DEVELOPMENT
    # =========================================================

    {
        "title": "Android Development",
        "description": "Learn Android development.",
        "department": "Mobile Development",
        "category": "Android",
        "skill": "Android",
        "level": "Beginner",
        "provider": "Android Developers",
        "duration": "Self-paced",
        "url": "https://developer.android.com/courses"
    },
    {
        "title": "Kotlin",
        "description": "Learn Kotlin programming.",
        "department": "Mobile Development",
        "category": "Android",
        "skill": "Kotlin",
        "level": "Beginner",
        "provider": "W3Schools",
        "duration": "Self-paced",
        "url": "https://www.w3schools.com/kotlin/"
    },
    {
        "title": "Swift",
        "description": "Learn Swift programming.",
        "department": "Mobile Development",
        "category": "iOS",
        "skill": "Swift",
        "level": "Beginner",
        "provider": "Swift",
        "duration": "Self-paced",
        "url": "https://www.swift.org/documentation/"
    },
    {
        "title": "Flutter",
        "description": "Learn cross-platform Flutter development.",
        "department": "Mobile Development",
        "category": "Cross Platform",
        "skill": "Flutter",
        "level": "Beginner",
        "provider": "Flutter",
        "duration": "Self-paced",
        "url": "https://docs.flutter.dev/get-started/learn-flutter"
    },

    # =========================================================
    # UI/UX
    # =========================================================

    {
        "title": "Figma",
        "description": "Learn UI design and prototyping with Figma.",
        "department": "UI/UX & Product Design",
        "category": "UI Design",
        "skill": "Figma",
        "level": "Beginner",
        "provider": "Figma",
        "duration": "Self-paced",
        "url": "https://help.figma.com/hc/en-us/categories/360002051613"
    },
    {
        "title": "Material Design",
        "description": "Learn UI components and design systems.",
        "department": "UI/UX & Product Design",
        "category": "Design Systems",
        "skill": "Design Systems",
        "level": "Intermediate",
        "provider": "Google",
        "duration": "Self-paced",
        "url": "https://m3.material.io/"
    },

    # =========================================================
    # CIVIL ENGINEERING
    # =========================================================

    {
        "title": "Civil Engineering Fundamentals",
        "description": "Explore civil engineering fundamentals.",
        "department": "Civil Engineering",
        "category": "Fundamentals",
        "skill": "Civil Engineering Fundamentals",
        "level": "Beginner",
        "provider": "NPTEL",
        "duration": "Self-paced",
        "url": "https://www.nptel.ac.in/courses"
    },
    {
        "title": "Structural Engineering",
        "description": "Learn structural engineering concepts.",
        "department": "Civil Engineering",
        "category": "Structural",
        "skill": "Structural Engineering",
        "level": "Intermediate",
        "provider": "NPTEL",
        "duration": "Self-paced",
        "url": "https://www.nptel.ac.in/courses"
    },
    {
        "title": "Geotechnical Engineering",
        "description": "Learn soil mechanics and geotechnical engineering.",
        "department": "Civil Engineering",
        "category": "Geotechnical",
        "skill": "Geotechnical Engineering",
        "level": "Intermediate",
        "provider": "NPTEL",
        "duration": "Self-paced",
        "url": "https://www.nptel.ac.in/courses"
    },

    # =========================================================
    # MECHANICAL ENGINEERING
    # =========================================================

    {
        "title": "Mechanical Engineering Fundamentals",
        "description": "Learn mechanical engineering fundamentals.",
        "department": "Mechanical Engineering",
        "category": "Fundamentals",
        "skill": "Mechanical Engineering Fundamentals",
        "level": "Beginner",
        "provider": "NPTEL",
        "duration": "Self-paced",
        "url": "https://www.nptel.ac.in/courses"
    },
    {
        "title": "Machine Design",
        "description": "Learn machine design principles.",
        "department": "Mechanical Engineering",
        "category": "Mechanical Design",
        "skill": "Machine Design",
        "level": "Intermediate",
        "provider": "NPTEL",
        "duration": "Self-paced",
        "url": "https://www.nptel.ac.in/courses"
    },
    {
        "title": "Manufacturing Engineering",
        "description": "Learn manufacturing processes.",
        "department": "Mechanical Engineering",
        "category": "Manufacturing",
        "skill": "Manufacturing",
        "level": "Intermediate",
        "provider": "NPTEL",
        "duration": "Self-paced",
        "url": "https://www.nptel.ac.in/courses"
    },

    # =========================================================
    # ELECTRICAL ENGINEERING
    # =========================================================

    {
        "title": "Electrical Engineering Fundamentals",
        "description": "Learn electrical engineering fundamentals.",
        "department": "Electrical Engineering",
        "category": "Fundamentals",
        "skill": "Electrical Engineering Fundamentals",
        "level": "Beginner",
        "provider": "NPTEL",
        "duration": "Self-paced",
        "url": "https://www.nptel.ac.in/courses"
    },
    {
        "title": "Power Systems",
        "description": "Learn electrical power systems.",
        "department": "Electrical Engineering",
        "category": "Power Systems",
        "skill": "Power Systems",
        "level": "Intermediate",
        "provider": "NPTEL",
        "duration": "Self-paced",
        "url": "https://www.nptel.ac.in/courses"
    },
    {
        "title": "Power Electronics",
        "description": "Learn power electronic systems.",
        "department": "Electrical Engineering",
        "category": "Power Electronics",
        "skill": "Power Electronics",
        "level": "Intermediate",
        "provider": "NPTEL",
        "duration": "Self-paced",
        "url": "https://www.nptel.ac.in/courses"
    },

    # =========================================================
    # ELECTRONICS & COMMUNICATION
    # =========================================================

    {
        "title": "Electronics Fundamentals",
        "description": "Learn analog and digital electronics.",
        "department": "Electronics & Communication",
        "category": "Electronics Fundamentals",
        "skill": "Electronics Fundamentals",
        "level": "Beginner",
        "provider": "NPTEL",
        "duration": "Self-paced",
        "url": "https://www.nptel.ac.in/courses"
    },
    {
        "title": "Embedded Systems",
        "description": "Learn embedded systems and microcontrollers.",
        "department": "Electronics & Communication",
        "category": "Embedded",
        "skill": "Embedded Systems",
        "level": "Intermediate",
        "provider": "NPTEL",
        "duration": "Self-paced",
        "url": "https://www.nptel.ac.in/courses"
    },
    {
        "title": "VLSI Design",
        "description": "Learn VLSI and digital hardware design.",
        "department": "Electronics & Communication",
        "category": "VLSI",
        "skill": "VLSI",
        "level": "Advanced",
        "provider": "NPTEL",
        "duration": "Self-paced",
        "url": "https://www.nptel.ac.in/courses"
    },

    # =========================================================
    # ARCHITECTURE
    # =========================================================

    {
        "title": "Architecture Fundamentals",
        "description": "Learn architecture and planning fundamentals.",
        "department": "Architecture",
        "category": "Fundamentals",
        "skill": "Architecture Fundamentals",
        "level": "Beginner",
        "provider": "NPTEL",
        "duration": "Self-paced",
        "url": "https://www.nptel.ac.in/courses"
    },
    {
        "title": "Building Information Modelling",
        "description": "Learn BIM concepts and digital construction.",
        "department": "Architecture",
        "category": "Digital Architecture",
        "skill": "BIM",
        "level": "Intermediate",
        "provider": "Autodesk",
        "duration": "Self-paced",
        "url": "https://www.autodesk.com/learn"
    },

    # =========================================================
    # ROBOTICS & AUTOMATION
    # =========================================================

    {
        "title": "ROS 2 Tutorials",
        "description": "Learn Robot Operating System and robotics programming.",
        "department": "Robotics & Automation",
        "category": "Robot Programming",
        "skill": "ROS",
        "level": "Intermediate",
        "provider": "ROS",
        "duration": "Self-paced",
        "url": "https://docs.ros.org/en/rolling/Tutorials.html"
    },
    {
        "title": "OpenCV Computer Vision",
        "description": "Learn computer vision for robotics.",
        "department": "Robotics & Automation",
        "category": "Computer Vision",
        "skill": "Computer Vision",
        "level": "Intermediate",
        "provider": "OpenCV",
        "duration": "Self-paced",
        "url": "https://docs.opencv.org/4.x/d9/df8/tutorial_root.html"
    },

    # =========================================================
    # BIOTECHNOLOGY
    # =========================================================

    {
        "title": "Biotechnology Fundamentals",
        "description": "Learn biotechnology fundamentals.",
        "department": "Biotechnology",
        "category": "Fundamentals",
        "skill": "Biotechnology Fundamentals",
        "level": "Beginner",
        "provider": "NPTEL",
        "duration": "Self-paced",
        "url": "https://www.nptel.ac.in/courses"
    },
    {
        "title": "Bioinformatics",
        "description": "Learn computational methods used in biology.",
        "department": "Biotechnology",
        "category": "Bioinformatics",
        "skill": "Bioinformatics",
        "level": "Intermediate",
        "provider": "NCBI",
        "duration": "Self-paced",
        "url": "https://www.ncbi.nlm.nih.gov/education/"
    },

    # =========================================================
    # CHEMICAL ENGINEERING
    # =========================================================

    {
        "title": "Chemical Engineering Fundamentals",
        "description": "Explore chemical engineering fundamentals.",
        "department": "Chemical Engineering",
        "category": "Fundamentals",
        "skill": "Chemical Engineering Fundamentals",
        "level": "Beginner",
        "provider": "NPTEL",
        "duration": "Self-paced",
        "url": "https://www.nptel.ac.in/courses"
    },
    {
        "title": "Chemical Process Engineering",
        "description": "Explore process engineering concepts.",
        "department": "Chemical Engineering",
        "category": "Process Engineering",
        "skill": "Process Engineering",
        "level": "Intermediate",
        "provider": "NPTEL",
        "duration": "Self-paced",
        "url": "https://www.nptel.ac.in/courses"
    },

    # =========================================================
    # BUSINESS & MANAGEMENT
    # =========================================================

    {
        "title": "Business Analytics",
        "description": "Learn analytics for business decision making.",
        "department": "Business & Management",
        "category": "Business Analytics",
        "skill": "Business Analytics",
        "level": "Beginner",
        "provider": "Microsoft",
        "duration": "Self-paced",
        "url": "https://learn.microsoft.com/en-us/training/"
    },
    {
        "title": "Project Management",
        "description": "Learn project planning and management.",
        "department": "Business & Management",
        "category": "Management",
        "skill": "Project Management",
        "level": "Beginner",
        "provider": "Atlassian",
        "duration": "Self-paced",
        "url": "https://www.atlassian.com/agile/project-management"
    },

    # =========================================================
    # FINANCE & ACCOUNTING
    # =========================================================

    {
        "title": "Financial Modelling with Excel",
        "description": "Learn Excel for financial analysis.",
        "department": "Finance & Accounting",
        "category": "Financial Analysis",
        "skill": "Financial Modeling",
        "level": "Intermediate",
        "provider": "W3Schools",
        "duration": "Self-paced",
        "url": "https://www.w3schools.com/excel/"
    },
    {
        "title": "FinTech",
        "description": "Explore financial technology and digital finance.",
        "department": "Finance & Accounting",
        "category": "FinTech",
        "skill": "FinTech",
        "level": "Intermediate",
        "provider": "NPTEL",
        "duration": "Self-paced",
        "url": "https://www.nptel.ac.in/courses"
    },

    # =========================================================
    # HR & PEOPLE
    # =========================================================

    {
        "title": "Human Resources Fundamentals",
        "description": "Learn recruitment, talent management and HR operations.",
        "department": "HR & People",
        "category": "HR Fundamentals",
        "skill": "Human Resources",
        "level": "Beginner",
        "provider": "Microsoft",
        "duration": "Self-paced",
        "url": "https://learn.microsoft.com/en-us/training/"
    },
    {
        "title": "People Analytics",
        "description": "Learn data-driven HR and people analytics.",
        "department": "HR & People",
        "category": "HR Analytics",
        "skill": "People Analytics",
        "level": "Intermediate",
        "provider": "Microsoft",
        "duration": "Self-paced",
        "url": "https://learn.microsoft.com/en-us/training/"
    },

    # =========================================================
    # MARKETING
    # =========================================================

    {
        "title": "Digital Marketing",
        "description": "Learn SEO, social media and digital marketing.",
        "department": "Marketing & Digital Marketing",
        "category": "Digital Marketing",
        "skill": "Digital Marketing",
        "level": "Beginner",
        "provider": "Google",
        "duration": "Self-paced",
        "url": "https://skillshop.withgoogle.com/"
    },
    {
        "title": "Marketing Analytics",
        "description": "Learn analytics for marketing decisions.",
        "department": "Marketing & Digital Marketing",
        "category": "Marketing Analytics",
        "skill": "Marketing Analytics",
        "level": "Intermediate",
        "provider": "Google",
        "duration": "Self-paced",
        "url": "https://skillshop.withgoogle.com/"
    },

    # =========================================================
    # CONTENT & CREATOR
    # =========================================================

    {
        "title": "YouTube Creator Academy",
        "description": "Learn content creation and YouTube strategy.",
        "department": "Content & Creator Skills",
        "category": "Content Creation",
        "skill": "Content Creation",
        "level": "Beginner",
        "provider": "YouTube",
        "duration": "Self-paced",
        "url": "https://creatoracademy.youtube.com/"
    },
    {
        "title": "Canva Design School",
        "description": "Learn graphic design and visual content creation.",
        "department": "Content & Creator Skills",
        "category": "Graphic Design",
        "skill": "Graphic Design",
        "level": "Beginner",
        "provider": "Canva",
        "duration": "Self-paced",
        "url": "https://www.canva.com/designschool/"
    },
    {
        "title": "Blender Tutorials",
        "description": "Learn 3D modelling and animation.",
        "department": "Content & Creator Skills",
        "category": "3D & Animation",
        "skill": "3D & Animation",
        "level": "Intermediate",
        "provider": "Blender",
        "duration": "Self-paced",
        "url": "https://www.blender.org/support/tutorials/"
    },

    # =========================================================
    # FREELANCING
    # =========================================================

    {
        "title": "Freelancing Resources",
        "description": "Learn how to start freelancing and find clients.",
        "department": "Freelancing",
        "category": "Getting Started",
        "skill": "Freelancing",
        "level": "Beginner",
        "provider": "Upwork",
        "duration": "Self-paced",
        "url": "https://www.upwork.com/resources"
    },
    {
        "title": "Freelance Web Development",
        "description": "Learn resources for freelance web development.",
        "department": "Freelancing",
        "category": "Web Development",
        "skill": "Freelance Web Development",
        "level": "Intermediate",
        "provider": "Upwork",
        "duration": "Self-paced",
        "url": "https://www.upwork.com/resources"
    },

    # =========================================================
    # ENTREPRENEURSHIP
    # =========================================================

    {
        "title": "Startup School",
        "description": "Learn startup fundamentals and entrepreneurship.",
        "department": "Entrepreneurship",
        "category": "Startup Fundamentals",
        "skill": "Entrepreneurship",
        "level": "Beginner",
        "provider": "Y Combinator",
        "duration": "Self-paced",
        "url": "https://www.startupschool.org/"
    },
    {
        "title": "Y Combinator Startup Library",
        "description": "Explore startup and founder resources.",
        "department": "Entrepreneurship",
        "category": "Startup",
        "skill": "Startup Development",
        "level": "Beginner",
        "provider": "Y Combinator",
        "duration": "Self-paced",
        "url": "https://www.ycombinator.com/library"
    },

    # =========================================================
    # PROFESSIONAL & FUTURE SKILLS
    # =========================================================

    {
        "title": "Career Readiness",
        "description": "Learn workplace, collaboration and career skills.",
        "department": "Professional & Future Skills",
        "category": "Career Readiness",
        "skill": "Career Readiness",
        "level": "Beginner",
        "provider": "Microsoft",
        "duration": "Self-paced",
        "url": "https://learn.microsoft.com/en-us/training/"
    },
    {
        "title": "AI Literacy",
        "description": "Learn practical AI literacy and responsible AI.",
        "department": "Professional & Future Skills",
        "category": "AI Literacy",
        "skill": "AI Literacy",
        "level": "Beginner",
        "provider": "Microsoft",
        "duration": "Self-paced",
        "url": "https://learn.microsoft.com/en-us/training/ai/"
    },
    {
        "title": "Communication Skills",
        "description": "Develop communication and presentation skills.",
        "department": "Professional & Future Skills",
        "category": "Essential Skills",
        "skill": "Communication",
        "level": "Beginner",
        "provider": "Microsoft",
        "duration": "Self-paced",
        "url": "https://learn.microsoft.com/en-us/training/"
    },

    # =========================================================
    # ADDITIONAL COMPUTER SCIENCE & IT
    # =========================================================

    {
        "title": "Algorithms",
        "description": "Learn algorithmic problem solving and common algorithms.",
        "department": "Computer Science & IT",
        "category": "Algorithms",
        "skill": "Algorithms",
        "level": "Intermediate",
        "provider": "W3Schools",
        "duration": "Self-paced",
        "url": "https://www.w3schools.com/dsa/"
    },

    {
        "title": "Object Oriented Programming",
        "description": "Learn classes, objects, inheritance and polymorphism.",
        "department": "Computer Science & IT",
        "category": "Programming Fundamentals",
        "skill": "OOP",
        "level": "Intermediate",
        "provider": "W3Schools",
        "duration": "Self-paced",
        "url": "https://www.w3schools.com/java/java_oop.asp"
    },

    {
        "title": "PostgreSQL",
        "description": "Learn PostgreSQL relational database concepts and SQL.",
        "department": "Computer Science & IT",
        "category": "Databases",
        "skill": "PostgreSQL",
        "level": "Intermediate",
        "provider": "PostgreSQL",
        "duration": "Self-paced",
        "url": "https://www.postgresql.org/docs/"
    },

    {
        "title": "SQLite",
        "description": "Learn SQLite lightweight relational database development.",
        "department": "Computer Science & IT",
        "category": "Databases",
        "skill": "SQLite",
        "level": "Beginner",
        "provider": "SQLite",
        "duration": "Self-paced",
        "url": "https://www.sqlite.org/docs.html"
    },

    {
        "title": "Software Testing",
        "description": "Learn software testing fundamentals and testing practices.",
        "department": "Computer Science & IT",
        "category": "Software Engineering",
        "skill": "Software Testing",
        "level": "Intermediate",
        "provider": "Microsoft",
        "duration": "Self-paced",
        "url": "https://learn.microsoft.com/en-us/training/"
    },

    {
        "title": "Debugging",
        "description": "Learn debugging techniques for software development.",
        "department": "Computer Science & IT",
        "category": "Software Engineering",
        "skill": "Debugging",
        "level": "Beginner",
        "provider": "Microsoft",
        "duration": "Self-paced",
        "url": "https://learn.microsoft.com/en-us/training/"
    },

    # =========================================================
    # ADDITIONAL WEB & FULL STACK
    # =========================================================

    {
        "title": "Responsive Web Design",
        "description": "Learn responsive layouts and modern web design.",
        "department": "Web & Full-Stack Development",
        "category": "Frontend",
        "skill": "Responsive Web Design",
        "level": "Beginner",
        "provider": "W3Schools",
        "duration": "Self-paced",
        "url": "https://www.w3schools.com/css/"
    },

    {
        "title": "Tailwind CSS",
        "description": "Learn utility-first CSS development.",
        "department": "Web & Full-Stack Development",
        "category": "Frontend",
        "skill": "Tailwind CSS",
        "level": "Intermediate",
        "provider": "Tailwind CSS",
        "duration": "Self-paced",
        "url": "https://tailwindcss.com/docs"
    },

    {
        "title": "Next.js",
        "description": "Learn React-based full-stack development using Next.js.",
        "department": "Web & Full-Stack Development",
        "category": "Frontend",
        "skill": "Next.js",
        "level": "Intermediate",
        "provider": "Next.js",
        "duration": "Self-paced",
        "url": "https://nextjs.org/learn"
    },

    {
        "title": "Angular",
        "description": "Learn Angular for modern web applications.",
        "department": "Web & Full-Stack Development",
        "category": "Frontend",
        "skill": "Angular",
        "level": "Intermediate",
        "provider": "Angular",
        "duration": "Self-paced",
        "url": "https://angular.dev/tutorials"
    },

    {
        "title": "Vue.js",
        "description": "Learn Vue.js for frontend web application development.",
        "department": "Web & Full-Stack Development",
        "category": "Frontend",
        "skill": "Vue.js",
        "level": "Intermediate",
        "provider": "Vue.js",
        "duration": "Self-paced",
        "url": "https://vuejs.org/tutorial/"
    },

    {
        "title": "Express.js",
        "description": "Learn backend API development using Express.js.",
        "department": "Web & Full-Stack Development",
        "category": "Backend",
        "skill": "Express.js",
        "level": "Intermediate",
        "provider": "Express",
        "duration": "Self-paced",
        "url": "https://expressjs.com/en/starter/installing.html"
    },

    {
        "title": "REST API Development",
        "description": "Learn REST APIs, HTTP methods and API design.",
        "department": "Web & Full-Stack Development",
        "category": "Backend",
        "skill": "REST APIs",
        "level": "Intermediate",
        "provider": "Microsoft",
        "duration": "Self-paced",
        "url": "https://learn.microsoft.com/en-us/training/"
    },

    {
        "title": "PHP Web Development",
        "description": "Learn PHP programming and server-side web development.",
        "department": "Web & Full-Stack Development",
        "category": "Backend",
        "skill": "PHP",
        "level": "Beginner",
        "provider": "W3Schools",
        "duration": "Self-paced",
        "url": "https://www.w3schools.com/php/"
    }
]


def seed_courses():

    db = SessionLocal()

    added = 0
    skipped = 0

    try:

        for data in courses:

            existing = (
                db.query(Course)
                .filter(Course.title == data["title"])
                .first()
            )

            if existing:
                skipped += 1
                continue

            course = Course(**data)

            db.add(course)
            added += 1

        db.commit()

        total = db.query(Course).count()

        departments = (
            db.query(Course.department)
            .distinct()
            .count()
        )

        print("=" * 60)
        print("SkillBridge AI Course Database")
        print("=" * 60)
        print(f"Courses added   : {added}")
        print(f"Courses skipped : {skipped}")
        print(f"Total courses   : {total}")
        print(f"Branches covered: {departments}")
        print("=" * 60)

    except Exception as e:

        db.rollback()
        print("ERROR:", e)

    finally:
        db.close()


if __name__ == "__main__":
    seed_courses()