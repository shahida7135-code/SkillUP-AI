from database import SessionLocal, Base, engine

from models.roadmap import (
    Department,
    Career,
    Skill,
    CareerSkill
)


# ============================================================
# DATABASE INITIALIZATION
# ============================================================

Base.metadata.create_all(bind=engine)


# ============================================================
# MASTER LEARNING TAXONOMY
# ============================================================

LEARNING_DATA = {

    # ========================================================
    # COMPUTER SCIENCE & IT
    # ========================================================

    "Computer Science & IT": {

        "Software Development": [
            "Programming Logic",
            "Data Structures",
            "Algorithms",
            "Object Oriented Programming",
            "DBMS",
            "Operating Systems",
            "Computer Networks",
            "Software Engineering",
            "Git",
            "GitHub",
            "Software Testing",
            "Debugging"
        ],

        "Programming Languages": [
            "Python",
            "Java",
            "JavaScript",
            "TypeScript",
            "C",
            "C++",
            "C#",
            "Go",
            "Rust",
            "Kotlin",
            "Swift",
            "Dart",
            "PHP",
            "Ruby",
            "R"
        ],

        "Databases": [
            "SQL",
            "PostgreSQL",
            "MySQL",
            "MongoDB",
            "Redis",
            "SQLite",
            "Firebase",
            "Elasticsearch"
        ]
    },


    # ========================================================
    # WEB & FULL STACK
    # ========================================================

    "Web & Full-Stack Development": {

        "Frontend Development": [
            "HTML",
            "CSS",
            "JavaScript",
            "TypeScript",
            "React",
            "Next.js",
            "Angular",
            "Vue",
            "Svelte",
            "Tailwind CSS"
        ],

        "Backend Development": [
            "Node.js",
            "Express",
            "FastAPI",
            "Django",
            "Spring Boot",
            ".NET",
            "Laravel"
        ],

        "MERN Full Stack": [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Node.js",
            "Express",
            "MongoDB"
        ],

        "PERN Full Stack": [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Node.js",
            "Express",
            "PostgreSQL"
        ],

        "Python Full Stack": [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Python",
            "FastAPI",
            "Django",
            "PostgreSQL"
        ],

        "Java Full Stack": [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Java",
            "Spring Boot",
            "PostgreSQL"
        ],

        ".NET Full Stack": [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            ".NET",
            "SQL"
        ]
    },


    # ========================================================
    # AI & MACHINE LEARNING
    # ========================================================

    "Artificial Intelligence & Machine Learning": {

        "AI Fundamentals": [
            "AI Concepts",
            "Search",
            "Reasoning",
            "Knowledge Representation",
            "AI Ethics"
        ],

        "Machine Learning": [
            "Supervised Learning",
            "Unsupervised Learning",
            "Regression",
            "Classification",
            "Clustering",
            "Feature Engineering",
            "Model Evaluation"
        ],

        "Deep Learning": [
            "Neural Networks",
            "CNN",
            "RNN",
            "LSTM",
            "Transformers"
        ],

        "Machine Learning Frameworks": [
            "PyTorch",
            "TensorFlow",
            "Keras",
            "Scikit-learn",
            "XGBoost"
        ],

        "Generative AI": [
            "LLMs",
            "Prompt Engineering",
            "Embeddings",
            "RAG",
            "Vector Databases",
            "AI Agents",
            "Multimodal AI",
            "Function Calling",
            "Fine-tuning",
            "Model Evaluation"
        ],

        "AI Engineering": [
            "LangChain",
            "LlamaIndex",
            "Hugging Face",
            "MLflow",
            "Docker",
            "Model Serving",
            "AI APIs"
        ]
    },


    # ========================================================
    # DATA SCIENCE & ANALYTICS
    # ========================================================

    "Data Science & Analytics": {

        "Data Analytics": [
            "Excel",
            "SQL",
            "Statistics",
            "Data Cleaning",
            "Data Visualization",
            "Business Intelligence"
        ],

        "Business Intelligence Tools": [
            "Power BI",
            "Tableau",
            "Looker Studio",
            "Excel",
            "Google Sheets"
        ],

        "Data Science": [
            "Python",
            "NumPy",
            "Pandas",
            "Matplotlib",
            "Seaborn",
            "Scikit-learn",
            "Statistics",
            "Probability"
        ],

        "Big Data": [
            "Apache Spark",
            "Hadoop",
            "Kafka",
            "Databricks",
            "Snowflake",
            "BigQuery"
        ],

        "Data Engineering": [
            "ETL",
            "ELT",
            "Data Pipelines",
            "Data Warehouses",
            "Data Lakes",
            "Airflow",
            "dbt"
        ]
    },


    # ========================================================
    # CYBERSECURITY
    # ========================================================

    "Cybersecurity": {

        "Cybersecurity Fundamentals": [
            "Networking",
            "Linux",
            "Cryptography",
            "Authentication",
            "Access Control",
            "Security Principles"
        ],

        "Ethical Hacking": [
            "Networking",
            "Linux",
            "Kali Linux",
            "Nmap",
            "Wireshark",
            "Burp Suite",
            "OWASP ZAP",
            "Metasploit"
        ],

        "SOC Analyst": [
            "Networking",
            "Linux",
            "SIEM",
            "Splunk",
            "Wazuh",
            "Threat Detection",
            "Incident Response"
        ],

        "Security Engineer": [
            "Networking",
            "Linux",
            "Cryptography",
            "Authentication",
            "Access Control",
            "Security Principles"
        ],

        "Cloud Security": [
            "Cloud Security",
            "IAM",
            "Zero Trust",
            "Identity Security"
        ],

        "Application Security": [
            "Application Security",
            "API Security",
            "OWASP ZAP",
            "Burp Suite"
        ],

        "Digital Forensics": [
            "Linux",
            "Digital Forensics",
            "Incident Response"
        ],

        "Incident Response": [
            "Incident Response",
            "Threat Detection",
            "SIEM",
            "Threat Hunting"
        ],

        "Threat Intelligence": [
            "Threat Intelligence",
            "Threat Hunting",
            "Security Principles"
        ],

        "Penetration Testing": [
            "Networking",
            "Linux",
            "Kali Linux",
            "Nmap",
            "Wireshark",
            "Burp Suite",
            "Metasploit",
            "Nessus"
        ],

        "GRC": [
            "Security Principles",
            "Risk Management",
            "Access Control"
        ],

        "Modern Cybersecurity": [
            "Zero Trust",
            "Cloud Security",
            "Identity Security",
            "API Security",
            "DevSecOps",
            "AI Security",
            "Threat Hunting"
        ]
    },


    # ========================================================
    # CLOUD
    # ========================================================

    "Cloud Computing": {

        "AWS Cloud": [
            "EC2",
            "S3",
            "Lambda",
            "RDS",
            "IAM",
            "VPC",
            "CloudWatch"
        ],

        "Microsoft Azure": [
            "Azure VM",
            "Azure Functions",
            "Azure Storage",
            "Azure SQL",
            "Entra ID"
        ],

        "Google Cloud": [
            "Compute Engine",
            "Cloud Storage",
            "Cloud Run",
            "BigQuery",
            "Vertex AI"
        ],

        "Cloud Engineering": [
            "Cloud Architecture",
            "Networking",
            "IAM",
            "Serverless",
            "Containers",
            "Cloud Security",
            "Cloud Databases"
        ]
    },


    # ========================================================
    # DEVOPS
    # ========================================================

    "DevOps & SRE": {

        "DevOps Engineering": [
            "Linux",
            "Git",
            "GitHub",
            "Docker",
            "Kubernetes",
            "CI/CD",
            "Jenkins",
            "GitHub Actions",
            "GitLab CI",
            "Terraform",
            "Ansible"
        ],

        "Site Reliability Engineering": [
            "Linux",
            "Docker",
            "Kubernetes",
            "Prometheus",
            "Grafana",
            "Monitoring",
            "Observability"
        ],

        "Infrastructure Engineering": [
            "Terraform",
            "Ansible",
            "Infrastructure as Code",
            "Docker",
            "Kubernetes"
        ]
    },


    # ========================================================
    # MOBILE
    # ========================================================

    "Mobile Development": {

        "Android Development": [
            "Kotlin",
            "Java",
            "Android Studio",
            "Jetpack Compose"
        ],

        "iOS Development": [
            "Swift",
            "SwiftUI",
            "Xcode"
        ],

        "Cross Platform Development": [
            "Flutter",
            "Dart",
            "React Native"
        ]
    },


    # ========================================================
    # UI / UX
    # ========================================================

    "UI/UX & Product Design": {

        "UI Design": [
            "Figma",
            "Typography",
            "Color",
            "Layout",
            "Design Systems",
            "Accessibility"
        ],

        "UX Design": [
            "User Research",
            "Personas",
            "User Journeys",
            "Wireframes",
            "Prototyping",
            "Usability Testing",
            "Information Architecture"
        ],

        "Product Design": [
            "Product Thinking",
            "Product Strategy",
            "UX Writing",
            "Design Systems",
            "Product Analytics"
        ]
    },


    # ========================================================
    # CIVIL
    # ========================================================

    "Civil Engineering": {

        "Civil Engineering Fundamentals": [
            "Engineering Drawing",
            "Surveying",
            "Structural Analysis",
            "Construction Materials",
            "Soil Mechanics",
            "Hydraulics",
            "Environmental Engineering"
        ],

        "Structural Engineering": [
            "Structural Analysis",
            "Engineering Drawing",
            "ETABS",
            "STAAD.Pro",
            "SAFE"
        ],

        "Geotechnical Engineering": [
            "Soil Mechanics",
            "Engineering Drawing"
        ],

        "Transportation Engineering": [
            "Transportation",
            "Surveying",
            "Civil 3D"
        ],

        "Construction Engineering": [
            "Construction",
            "Construction Materials",
            "Primavera",
            "BIM"
        ],

        "Environmental Engineering": [
            "Environmental Engineering",
            "Water Resources"
        ],

        "Civil Engineering Software": [
            "AutoCAD",
            "Civil 3D",
            "Revit",
            "STAAD.Pro",
            "ETABS",
            "SAFE",
            "Primavera",
            "BIM"
        ]
    },


    # ========================================================
    # MECHANICAL
    # ========================================================

    "Mechanical Engineering": {

        "Mechanical Engineering Fundamentals": [
            "Engineering Mechanics",
            "Thermodynamics",
            "Fluid Mechanics",
            "Heat Transfer",
            "Manufacturing",
            "Machine Design",
            "Materials"
        ],

        "Mechanical Design": [
            "Engineering Mechanics",
            "Machine Design",
            "Materials",
            "AutoCAD",
            "SolidWorks"
        ],

        "Automotive Engineering": [
            "Automotive",
            "Manufacturing",
            "Machine Design"
        ],

        "Manufacturing Engineering": [
            "Manufacturing",
            "CAD/CAM",
            "Materials"
        ],

        "Mechatronics": [
            "Mechatronics",
            "Robotics",
            "Control Systems"
        ],

        "Aerospace Engineering": [
            "Aerospace",
            "Fluid Mechanics",
            "Thermodynamics",
            "Materials"
        ],

        "Mechanical Engineering Software": [
            "AutoCAD",
            "SolidWorks",
            "CATIA",
            "Creo",
            "ANSYS",
            "MATLAB",
            "Fusion 360",
            "Siemens NX"
        ]
    },


    # ========================================================
    # ELECTRICAL
    # ========================================================

    "Electrical Engineering": {

        "Electrical Engineering Fundamentals": [
            "Circuit Theory",
            "Electrical Machines",
            "Power Systems",
            "Control Systems",
            "Signals"
        ],

        "Power Systems": [
            "Power Systems",
            "Electrical Machines",
            "MATLAB",
            "ETAP",
            "PSCAD"
        ],

        "Renewable Energy": [
            "Renewable Energy",
            "Power Systems",
            "Power Electronics"
        ],

        "Power Electronics": [
            "Power Electronics",
            "Circuit Theory",
            "Control Systems"
        ],

        "Automation": [
            "Automation",
            "PLC",
            "SCADA",
            "Control Engineering"
        ],

        "Electrical Engineering Technologies": [
            "MATLAB",
            "Simulink",
            "ETAP",
            "PSCAD",
            "PLC",
            "SCADA",
            "AutoCAD Electrical"
        ]
    },


    # ========================================================
    # ECE
    # ========================================================

    "Electronics & Communication": {

        "Electronics Fundamentals": [
            "Analog Electronics",
            "Digital Electronics",
            "Microprocessors",
            "Microcontrollers",
            "Communication Systems"
        ],

        "Embedded Systems": [
            "Microcontrollers",
            "Arduino",
            "ESP32",
            "STM32",
            "Raspberry Pi"
        ],

        "VLSI": [
            "Verilog",
            "VHDL",
            "FPGA",
            "Digital Design",
            "ASIC"
        ],

        "PCB Design": [
            "KiCad",
            "Altium",
            "Eagle"
        ],

        "IoT & Edge Computing": [
            "IoT",
            "Edge Computing",
            "Embedded Systems",
            "ESP32",
            "Raspberry Pi"
        ],

        "Embedded AI": [
            "Embedded AI",
            "Embedded Systems",
            "Edge Computing"
        ],

        "Semiconductor Technology": [
            "Semiconductor Technology",
            "Digital Design",
            "ASIC"
        ]
    },


    # ========================================================
    # ARCHITECTURE
    # ========================================================

    "Architecture": {

        "Architecture Fundamentals": [
            "Architectural Design",
            "Building Planning",
            "Construction",
            "Structural Concepts",
            "Sustainable Design"
        ],

        "Digital Architecture": [
            "AutoCAD",
            "Revit",
            "BIM",
            "SketchUp",
            "Rhino",
            "Grasshopper"
        ],

        "Architectural Visualization": [
            "Lumion",
            "Enscape",
            "V-Ray",
            "Blender",
            "3ds Max"
        ],

        "Computational Architecture": [
            "Parametric Design",
            "Computational Design",
            "Generative Design",
            "Digital Twins",
            "Sustainable Architecture"
        ]
    },


    # ========================================================
    # ROBOTICS
    # ========================================================

    "Robotics & Automation": {

        "Robotics Fundamentals": [
            "Python",
            "C++",
            "Electronics",
            "Sensors",
            "Motors",
            "Control Systems",
            "Embedded Systems"
        ],

        "Robot Programming": [
            "Python",
            "C++",
            "ROS",
            "ROS/ROS2"
        ],

        "Computer Vision Robotics": [
            "Computer Vision",
            "OpenCV",
            "Python"
        ],

        "Robotics Technologies": [
            "ROS/ROS2",
            "Arduino",
            "Raspberry Pi",
            "ESP32",
            "NVIDIA Jetson",
            "OpenCV",
            "MATLAB",
            "Gazebo"
        ]
    },


    # ========================================================
    # BIOTECHNOLOGY
    # ========================================================

    "Biotechnology": {

        "Biotechnology Fundamentals": [
            "Molecular Biology",
            "Genetics",
            "Bioinformatics",
            "Biostatistics",
            "Computational Biology"
        ],

        "Bioinformatics": [
            "Python",
            "R",
            "BLAST",
            "Bioconductor",
            "Galaxy",
            "Bioinformatics Databases"
        ],

        "Computational Biology": [
            "Computational Biology",
            "Python",
            "R"
        ],

        "Biomedical Data Science": [
            "Biomedical Data Science",
            "Python",
            "Statistics"
        ],

        "AI for Healthcare": [
            "AI for Healthcare",
            "Genomics",
            "Drug Discovery",
            "Biomedical Data Science"
        ]
    },


    # ========================================================
    # CHEMICAL ENGINEERING
    # ========================================================

    "Chemical Engineering": {},


    # ========================================================
    # BUSINESS
    # ========================================================

    "Business & Management": {

        "Business Analytics": [
            "Excel",
            "SQL",
            "Power BI",
            "Tableau",
            "Statistics"
        ],

        "Business Analyst": [
            "Requirements Gathering",
            "Process Mapping",
            "Documentation",
            "Agile",
            "Scrum",
            "Jira",
            "Stakeholder Management"
        ],

        "Management": [
            "Project Management",
            "Product Management",
            "Operations",
            "Strategy",
            "Leadership"
        ]
    },


    # ========================================================
    # FINANCE
    # ========================================================

    "Finance & Accounting": {

        "Finance Fundamentals": [
            "Accounting",
            "Financial Analysis",
            "Financial Modeling",
            "Investment",
            "Risk",
            "Budgeting"
        ],

        "Financial Technology": [
            "Excel",
            "Power BI",
            "SQL",
            "Python",
            "Financial Modeling Tools",
            "Financial Data Analytics"
        ],

        "FinTech": [
            "FinTech",
            "Blockchain",
            "Digital Payments",
            "AI in Finance"
        ]
    },


    # ========================================================
    # HR
    # ========================================================

    "HR & People": {

        "HR Fundamentals": [
            "Recruitment",
            "Talent Acquisition",
            "Performance Management",
            "Employee Engagement",
            "Payroll",
            "HR Operations"
        ],

        "HR Technology": [
            "HR Analytics",
            "HRIS",
            "People Analytics",
            "AI Recruitment",
            "Workforce Analytics"
        ]
    },


    # ========================================================
    # MARKETING
    # ========================================================

    "Marketing & Digital Marketing": {

        "Digital Marketing": [
            "SEO",
            "SEM",
            "Social Media",
            "Email Marketing",
            "Content Marketing",
            "Affiliate Marketing",
            "Performance Marketing"
        ],

        "Marketing Analytics": [
            "Google Analytics",
            "Search Console",
            "Meta Ads",
            "Google Ads",
            "Marketing Dashboards"
        ],

        "AI Marketing": [
            "AI Content",
            "AI Research",
            "Marketing Automation",
            "Personalization",
            "AI-assisted Advertising"
        ]
    },


    # ========================================================
    # CREATOR
    # ========================================================

    "Content & Creator Skills": {

        "Content Creation": [
            "YouTube",
            "Instagram",
            "LinkedIn",
            "Blogging",
            "Copywriting",
            "Scriptwriting",
            "Storytelling"
        ],

        "Video Editing": [
            "DaVinci Resolve",
            "Premiere Pro",
            "CapCut",
            "After Effects"
        ],

        "Graphic Design": [
            "Canva",
            "Photoshop",
            "Illustrator",
            "Figma"
        ],

        "3D & Animation": [
            "Blender",
            "Maya",
            "3ds Max",
            "Unreal Engine"
        ]
    },


    # ========================================================
    # FREELANCING
    # ========================================================

    "Freelancing": {

        "Getting Started": [
            "Finding Clients",
            "Proposal Writing",
            "Pricing",
            "Negotiation",
            "Client Communication",
            "Portfolio Building",
            "Personal Branding",
            "Contracts",
            "Invoicing",
            "Project Management"
        ],

        "Freelance Web Developer": [
            "WordPress",
            "Shopify",
            "HTML/CSS",
            "JavaScript",
            "React",
            "SEO",
            "Hosting",
            "APIs"
        ],

        "AI Freelancer": [
            "Prompt Engineering",
            "AI Automation",
            "Chatbots",
            "AI Agents",
            "RAG",
            "AI APIs",
            "Workflow Automation",
            "AI Content",
            "AI Integration"
        ]
    },


    # ========================================================
    # ENTREPRENEURSHIP
    # ========================================================

    "Entrepreneurship": {},


    # ========================================================
    # PROFESSIONAL / FUTURE SKILLS
    # ========================================================

    "Professional & Future Skills": {

        "Essential Skills": [
            "Communication",
            "English",
            "Critical Thinking",
            "Problem Solving",
            "Creativity",
            "Collaboration",
            "Time Management",
            "Presentation",
            "Leadership",
            "Adaptability"
        ],

        "Career Readiness": [
            "Resume",
            "LinkedIn",
            "Portfolio",
            "Networking",
            "Interview Skills",
            "Personal Branding"
        ],

        "AI Literacy": [
            "AI Tools",
            "Prompting",
            "AI Research",
            "AI Productivity",
            "AI Verification",
            "AI Ethics"
        ]
    }
}


# ============================================================
# SEED DATABASE
# ============================================================

def seed_database():

    db = SessionLocal()

    try:

        for department_name, careers in LEARNING_DATA.items():

            # ------------------------------------------------
            # CREATE DEPARTMENT
            # ------------------------------------------------

            department = db.query(Department).filter(
                Department.name == department_name
            ).first()

            if not department:

                department = Department(
                    name=department_name,
                    description=f"Learning paths and skills for {department_name}"
                )

                db.add(department)
                db.flush()


            # ------------------------------------------------
            # CREATE CAREERS / LEARNING PATHS
            # ------------------------------------------------

            for career_name, skill_names in careers.items():

                career = db.query(Career).filter(
                    Career.name == career_name
                ).first()

                if not career:

                    career = Career(
                        name=career_name,
                        department_id=department.id
                    )

                    db.add(career)
                    db.flush()

                else:

                    career.department_id = department.id


                # --------------------------------------------
                # CREATE SKILLS
                # --------------------------------------------

                for position, skill_name in enumerate(
                    skill_names,
                    start=1
                ):

                    skill = db.query(Skill).filter(
                        Skill.name == skill_name
                    ).first()

                    if not skill:

                        skill = Skill(
                            name=skill_name,
                            description=f"Learn {skill_name} as part of the {career_name} path."
                        )

                        db.add(skill)
                        db.flush()


                    # ----------------------------------------
                    # CREATE CAREER-SKILL RELATIONSHIP
                    # ----------------------------------------

                    existing_link = db.query(CareerSkill).filter(
                        CareerSkill.career_id == career.id,
                        CareerSkill.skill_id == skill.id
                    ).first()

                    if not existing_link:

                        # First skills are treated as higher
                        # priority because they appear earlier
                        # in the learning path.

                        if position <= 3:
                            priority = "High"
                        elif position <= 6:
                            priority = "Medium"
                        else:
                            priority = "Low"

                        link = CareerSkill(
                            career_id=career.id,
                            skill_id=skill.id,
                            priority=priority,
                            order=position,
                            estimated_weeks=1
                        )

                        db.add(link)


        db.commit()

        print("==============================================")
        print("SkillBridge AI learning database seeded!")
        print("==============================================")


    except Exception as e:

        db.rollback()

        print("Database seeding failed:")
        print(e)

        raise


    finally:

        db.close()


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":
    seed_database()