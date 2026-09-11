from database import SessionLocal
from models.roadmap import Skill
from models.course import Course


# ============================================================
# SkillBridge AI - Complete Learning Resource Seeder
# ============================================================

# Specific high-quality resources for important skills.
# Existing courses are never deleted or modified.
RESOURCE_MAP = {

    # ---------------- COMPUTER SCIENCE ----------------
    "Programming Logic": (
        "Programming Logic",
        "Learn programming logic, variables, conditions, loops and problem solving.",
        "https://www.w3schools.com/programming/"
    ),
    "Data Structures": (
        "Data Structures Tutorial",
        "Learn arrays, stacks, queues, linked lists, trees and other data structures.",
        "https://www.w3schools.com/dsa/"
    ),
    "Algorithms": (
        "Algorithms Tutorial",
        "Learn algorithms and algorithmic problem solving.",
        "https://www.w3schools.com/dsa/dsa_algo_intro.php"
    ),
    "Object Oriented Programming": (
        "Object Oriented Programming",
        "Learn object oriented programming concepts.",
        "https://www.w3schools.com/java/java_oop.asp"
    ),
    "DBMS": (
        "DBMS and SQL",
        "Learn database concepts and SQL.",
        "https://www.w3schools.com/sql/"
    ),
    "Operating Systems": (
        "Operating Systems",
        "Study operating system fundamentals.",
        "https://www.geeksforgeeks.org/operating-systems/"
    ),
    "Computer Networks": (
        "Computer Networks",
        "Learn networking fundamentals and protocols.",
        "https://www.geeksforgeeks.org/computer-network-tutorials/"
    ),
    "Software Engineering": (
        "Software Engineering",
        "Learn software development and engineering concepts.",
        "https://www.geeksforgeeks.org/software-engineering/"
    ),
    "Git": (
        "Git Tutorial",
        "Learn Git version control.",
        "https://www.w3schools.com/git/"
    ),
    "GitHub": (
        "GitHub Skills",
        "Learn GitHub and collaborative development.",
        "https://skills.github.com/"
    ),
    "Software Testing": (
        "Software Testing",
        "Learn software testing fundamentals.",
        "https://www.geeksforgeeks.org/software-testing-tutorial/"
    ),
    "Debugging": (
        "Debugging",
        "Learn debugging techniques and problem solving.",
        "https://www.geeksforgeeks.org/debugging-in-programming/"
    ),

    # ---------------- PROGRAMMING ----------------
    "Python": ("Python Tutorial", "Learn Python programming.", "https://www.w3schools.com/python/"),
    "Java": ("Java Tutorial", "Learn Java programming.", "https://www.w3schools.com/java/"),
    "JavaScript": ("JavaScript Tutorial", "Learn JavaScript.", "https://www.w3schools.com/js/"),
    "TypeScript": ("TypeScript Tutorial", "Learn TypeScript.", "https://www.w3schools.com/typescript/"),
    "C": ("C Tutorial", "Learn C programming.", "https://www.w3schools.com/c/"),
    "C++": ("C++ Tutorial", "Learn C++ programming.", "https://www.w3schools.com/cpp/"),
    "C#": ("C# Tutorial", "Learn C# programming.", "https://www.w3schools.com/cs/"),
    "Go": ("Go Tutorial", "Learn Go programming.", "https://www.w3schools.com/go/"),
    "Rust": ("Rust Learning", "Learn Rust programming.", "https://www.rust-lang.org/learn"),
    "Kotlin": ("Kotlin Tutorial", "Learn Kotlin.", "https://www.w3schools.com/kotlin/"),
    "Swift": ("Swift Documentation", "Learn Swift programming.", "https://www.swift.org/documentation/"),
    "Dart": ("Dart Documentation", "Learn Dart programming.", "https://dart.dev/guides"),
    "PHP": ("PHP Tutorial", "Learn PHP development.", "https://www.w3schools.com/php/"),
    "Ruby": ("Ruby Documentation", "Learn Ruby programming.", "https://www.ruby-lang.org/en/documentation/"),
    "R": ("R Tutorial", "Learn R programming.", "https://www.w3schools.com/r/"),
    "SQL": ("SQL Tutorial", "Learn SQL.", "https://www.w3schools.com/sql/"),

    # ---------------- DATABASES ----------------
    "PostgreSQL": ("PostgreSQL Tutorial", "Learn PostgreSQL.", "https://www.postgresql.org/docs/"),
    "MySQL": ("MySQL Tutorial", "Learn MySQL.", "https://www.w3schools.com/mysql/"),
    "MongoDB": ("MongoDB University", "Learn MongoDB.", "https://learn.mongodb.com/"),
    "Redis": ("Redis University", "Learn Redis.", "https://university.redis.io/"),
    "SQLite": ("SQLite Documentation", "Learn SQLite.", "https://www.sqlite.org/docs.html"),
    "Firebase": ("Firebase Documentation", "Learn Firebase.", "https://firebase.google.com/docs"),
    "Elasticsearch": ("Elastic Learning", "Learn Elasticsearch.", "https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html"),

    # ---------------- WEB ----------------
    "HTML": ("HTML Tutorial", "Learn HTML.", "https://www.w3schools.com/html/"),
    "CSS": ("CSS Tutorial", "Learn CSS.", "https://www.w3schools.com/css/"),
    "React": ("React Documentation", "Learn React.", "https://react.dev/learn"),
    "Next.js": ("Next.js Documentation", "Learn Next.js.", "https://nextjs.org/learn"),
    "Angular": ("Angular Tutorial", "Learn Angular.", "https://angular.dev/tutorials"),
    "Vue": ("Vue Documentation", "Learn Vue.", "https://vuejs.org/guide/introduction.html"),
    "Svelte": ("Svelte Tutorial", "Learn Svelte.", "https://svelte.dev/tutorial"),
    "Tailwind CSS": ("Tailwind CSS Documentation", "Learn Tailwind CSS.", "https://tailwindcss.com/docs"),
    "Node.js": ("Node.js Documentation", "Learn Node.js.", "https://nodejs.org/en/learn"),
    "Express": ("Express.js Documentation", "Learn Express.js.", "https://expressjs.com/"),
    "FastAPI": ("FastAPI Documentation", "Learn FastAPI.", "https://fastapi.tiangolo.com/"),
    "Django": ("Django Documentation", "Learn Django.", "https://docs.djangoproject.com/"),
    "Spring Boot": ("Spring Boot Documentation", "Learn Spring Boot.", "https://spring.io/projects/spring-boot"),
    ".NET": (".NET Learning", "Learn .NET development.", "https://dotnet.microsoft.com/learn"),
    "Laravel": ("Laravel Documentation", "Learn Laravel.", "https://laravel.com/docs"),

    # ---------------- AI / ML ----------------
    "AI Concepts": ("AI Fundamentals", "Learn artificial intelligence fundamentals.", "https://developers.google.com/machine-learning/crash-course"),
    "Search": ("AI Search", "Learn search techniques in artificial intelligence.", "https://www.geeksforgeeks.org/artificial-intelligence-tutorial/"),
    "Reasoning": ("AI Reasoning", "Learn reasoning concepts in AI.", "https://www.geeksforgeeks.org/artificial-intelligence-tutorial/"),
    "Knowledge Representation": ("Knowledge Representation", "Learn knowledge representation in AI.", "https://www.geeksforgeeks.org/knowledge-representation-in-ai/"),
    "AI Ethics": ("AI Ethics", "Learn responsible and ethical AI.", "https://ai.google/responsibility/principles/"),

    "Supervised Learning": ("Supervised Learning", "Learn supervised machine learning.", "https://developers.google.com/machine-learning/crash-course"),
    "Unsupervised Learning": ("Unsupervised Learning", "Learn unsupervised machine learning.", "https://developers.google.com/machine-learning/crash-course"),
    "Regression": ("Regression", "Learn regression algorithms.", "https://developers.google.com/machine-learning/crash-course"),
    "Classification": ("Classification", "Learn classification algorithms.", "https://developers.google.com/machine-learning/crash-course"),
    "Clustering": ("Clustering", "Learn clustering algorithms.", "https://scikit-learn.org/stable/modules/clustering.html"),
    "Feature Engineering": ("Feature Engineering", "Learn machine learning feature engineering.", "https://developers.google.com/machine-learning/crash-course"),
    "Model Evaluation": ("Model Evaluation", "Learn how to evaluate machine learning models.", "https://scikit-learn.org/stable/modules/model_evaluation.html"),

    "Neural Networks": ("Neural Networks", "Learn neural networks and deep learning.", "https://www.tensorflow.org/learn"),
    "CNN": ("Convolutional Neural Networks", "Learn CNNs for computer vision.", "https://www.tensorflow.org/tutorials/images/cnn"),
    "RNN": ("Recurrent Neural Networks", "Learn recurrent neural networks.", "https://www.tensorflow.org/guide/keras/working_with_rnns"),
    "LSTM": ("LSTM Networks", "Learn LSTM neural networks.", "https://www.tensorflow.org/guide/keras/working_with_rnns"),
    "Transformers": ("Transformers", "Learn transformer architectures.", "https://huggingface.co/learn/nlp-course/chapter1/4"),

    "PyTorch": ("PyTorch Tutorials", "Learn PyTorch.", "https://pytorch.org/tutorials/"),
    "TensorFlow": ("TensorFlow Tutorials", "Learn TensorFlow.", "https://www.tensorflow.org/tutorials"),
    "Keras": ("Keras Guides", "Learn Keras.", "https://keras.io/guides/"),
    "Scikit-learn": ("Scikit-learn Tutorials", "Learn machine learning with Scikit-learn.", "https://scikit-learn.org/stable/getting_started.html"),
    "XGBoost": ("XGBoost Documentation", "Learn XGBoost.", "https://xgboost.readthedocs.io/"),

    "LLMs": ("LLM Course", "Learn large language models.", "https://huggingface.co/learn/llm-course/chapter1/1"),
    "Prompt Engineering": ("Prompt Engineering", "Learn prompt engineering.", "https://www.promptingguide.ai/"),
    "Embeddings": ("Embeddings", "Learn embeddings for AI applications.", "https://huggingface.co/docs/transformers/main/en/tasks/feature_extraction"),
    "RAG": ("RAG Tutorial", "Learn Retrieval Augmented Generation.", "https://python.langchain.com/docs/concepts/rag/"),
    "Vector Databases": ("Vector Databases", "Learn vector databases.", "https://www.pinecone.io/learn/vector-database/"),
    "AI Agents": ("AI Agents", "Learn AI agent concepts.", "https://huggingface.co/learn/agents-course/unit0/introduction"),
    "Multimodal AI": ("Multimodal AI", "Learn multimodal artificial intelligence.", "https://huggingface.co/learn"),
    "Function Calling": ("Function Calling", "Learn function calling for AI applications.", "https://platform.openai.com/docs/guides/function-calling"),
    "Fine-tuning": ("Fine-tuning", "Learn model fine-tuning.", "https://huggingface.co/docs/transformers/training"),
    "LangChain": ("LangChain Documentation", "Learn LangChain.", "https://python.langchain.com/docs/introduction/"),
    "LlamaIndex": ("LlamaIndex Documentation", "Learn LlamaIndex.", "https://docs.llamaindex.ai/"),
    "Hugging Face": ("Hugging Face Course", "Learn Hugging Face tools.", "https://huggingface.co/learn"),
    "MLflow": ("MLflow Documentation", "Learn MLflow and ML lifecycle management.", "https://mlflow.org/docs/latest/ml/"),
    "Model Serving": ("Model Serving", "Learn how to deploy machine learning models.", "https://mlflow.org/docs/latest/ml/deployment/"),
    "AI APIs": ("AI APIs", "Learn how to build AI applications using APIs.", "https://huggingface.co/docs/api-inference/index"),

    # ---------------- DATA ----------------
    "Excel": ("Excel Tutorial", "Learn Excel for data analysis.", "https://www.w3schools.com/excel/"),
    "Statistics": ("Statistics", "Learn statistics fundamentals.", "https://www.khanacademy.org/math/statistics-probability"),
    "Probability": ("Probability", "Learn probability fundamentals.", "https://www.khanacademy.org/math/statistics-probability"),
    "Data Cleaning": ("Data Cleaning", "Learn data cleaning techniques.", "https://pandas.pydata.org/docs/user_guide/missing_data.html"),
    "Data Visualization": ("Data Visualization", "Learn data visualization.", "https://matplotlib.org/stable/tutorials/"),
    "Business Intelligence": ("Business Intelligence", "Learn business intelligence concepts.", "https://learn.microsoft.com/en-us/training/powerplatform/power-bi/"),
    "Power BI": ("Power BI Learning", "Learn Power BI.", "https://learn.microsoft.com/en-us/training/powerplatform/power-bi/"),
    "Tableau": ("Tableau Learning", "Learn Tableau.", "https://www.tableau.com/learn"),
    "Looker Studio": ("Looker Studio", "Learn Looker Studio.", "https://support.google.com/looker-studio/"),
    "Google Sheets": ("Google Sheets Training", "Learn Google Sheets.", "https://support.google.com/a/users/answer/9282720"),
    "NumPy": ("NumPy Documentation", "Learn NumPy.", "https://numpy.org/learn/"),
    "Pandas": ("Pandas Documentation", "Learn Pandas.", "https://pandas.pydata.org/docs/getting_started/"),
    "Matplotlib": ("Matplotlib Tutorials", "Learn Matplotlib.", "https://matplotlib.org/stable/tutorials/"),
    "Seaborn": ("Seaborn Documentation", "Learn Seaborn.", "https://seaborn.pydata.org/tutorial.html"),
    "Apache Spark": ("Apache Spark", "Learn Apache Spark.", "https://spark.apache.org/docs/latest/"),
    "Hadoop": ("Apache Hadoop", "Learn Hadoop.", "https://hadoop.apache.org/docs/"),
    "Kafka": ("Apache Kafka", "Learn Apache Kafka.", "https://kafka.apache.org/documentation/"),
    "Databricks": ("Databricks Learning", "Learn Databricks.", "https://www.databricks.com/learn"),
    "Snowflake": ("Snowflake Learning", "Learn Snowflake.", "https://learn.snowflake.com/"),
    "BigQuery": ("Google BigQuery", "Learn BigQuery.", "https://cloud.google.com/bigquery/docs"),
    "ETL": ("ETL Concepts", "Learn ETL data processing.", "https://www.ibm.com/think/topics/etl"),
    "ELT": ("ELT Concepts", "Learn ELT data processing.", "https://www.ibm.com/think/topics/etl"),
    "Data Pipelines": ("Data Pipelines", "Learn data pipeline development.", "https://airflow.apache.org/docs/"),
    "Data Warehouses": ("Data Warehousing", "Learn data warehouse concepts.", "https://www.ibm.com/think/topics/data-warehouse"),
    "Data Lakes": ("Data Lakes", "Learn data lake architecture.", "https://aws.amazon.com/big-data/datalakes-and-analytics/"),
    "Airflow": ("Apache Airflow", "Learn workflow orchestration with Airflow.", "https://airflow.apache.org/docs/"),
    "dbt": ("dbt Learn", "Learn dbt data transformation.", "https://docs.getdbt.com/docs/introduction"),

    # ---------------- CYBERSECURITY ----------------
    "Networking": ("Networking Fundamentals", "Learn networking fundamentals.", "https://www.cisco.com/c/en/us/training-events/training-certifications/training/training-services/courses/networking-basics.html"),
    "Linux": ("Linux Tutorial", "Learn Linux.", "https://www.linux.org/pages/download/"),
    "Cryptography": ("Cryptography", "Learn cryptography fundamentals.", "https://www.khanacademy.org/computing/computer-science/cryptography"),
    "Authentication": ("Authentication", "Learn authentication and identity concepts.", "https://owasp.org/www-community/controls/Authentication"),
    "Access Control": ("Access Control", "Learn access control concepts.", "https://owasp.org/www-community/Access_Control"),
    "Security Principles": ("Security Principles", "Learn cybersecurity principles.", "https://www.nist.gov/cyberframework"),

    "Kali Linux": ("Kali Linux Documentation", "Learn Kali Linux.", "https://www.kali.org/docs/"),
    "Nmap": ("Nmap Documentation", "Learn network scanning with Nmap.", "https://nmap.org/book/"),
    "Wireshark": ("Wireshark Documentation", "Learn packet analysis with Wireshark.", "https://www.wireshark.org/docs/"),
    "Burp Suite": ("Burp Suite Academy", "Learn web security testing.", "https://portswigger.net/web-security"),
    "OWASP ZAP": ("OWASP ZAP", "Learn web application security testing.", "https://www.zaproxy.org/docs/"),
    "Metasploit": ("Metasploit Documentation", "Learn the Metasploit framework.", "https://docs.metasploit.com/"),
    "SIEM": ("SIEM Fundamentals", "Learn security information and event management.", "https://www.ibm.com/think/topics/siem"),
    "Splunk": ("Splunk Training", "Learn Splunk.", "https://education.splunk.com/"),
    "Wazuh": ("Wazuh Documentation", "Learn Wazuh security monitoring.", "https://documentation.wazuh.com/"),

    "Threat Detection": ("Threat Detection", "Learn cybersecurity threat detection.", "https://www.nist.gov/cyberframework"),
    "Incident Response": ("Incident Response", "Learn incident response.", "https://www.nist.gov/privacy-framework/nist-sp-800-61"),
    "Cloud Security": ("Cloud Security", "Learn cloud security.", "https://cloud.google.com/security"),
    "IAM": ("Identity and Access Management", "Learn IAM.", "https://aws.amazon.com/iam/"),
    "Zero Trust": ("Zero Trust", "Learn Zero Trust security.", "https://www.nist.gov/publications/zero-trust-architecture"),
    "Identity Security": ("Identity Security", "Learn identity security.", "https://www.nist.gov/identity-access-management"),
    "Application Security": ("Application Security", "Learn application security.", "https://owasp.org/www-project-top-ten/"),
    "API Security": ("API Security", "Learn API security.", "https://owasp.org/API-Security/"),
    "Digital Forensics": ("Digital Forensics", "Learn digital forensics.", "https://www.nist.gov/itl/ssd/digital-forensics"),
    "Threat Hunting": ("Threat Hunting", "Learn threat hunting.", "https://www.cisa.gov/topics/cyber-threats-and-advisories"),
    "Threat Intelligence": ("Threat Intelligence", "Learn threat intelligence.", "https://www.cisa.gov/topics/cyber-threats-and-advisories"),
    "Nessus": ("Tenable Nessus", "Learn vulnerability scanning with Nessus.", "https://docs.tenable.com/nessus/"),
    "Risk Management": ("Cybersecurity Risk Management", "Learn cybersecurity risk management.", "https://www.nist.gov/cyberframework"),
    "DevSecOps": ("DevSecOps", "Learn security in DevOps.", "https://owasp.org/www-project-devsecops-guideline/"),
    "AI Security": ("AI Security", "Learn AI security concepts.", "https://owasp.org/www-project-top-10-for-large-language-model-applications/"),

    # ---------------- CLOUD ----------------
    "EC2": ("AWS EC2", "Learn Amazon EC2.", "https://docs.aws.amazon.com/ec2/"),
    "S3": ("AWS S3", "Learn Amazon S3.", "https://docs.aws.amazon.com/s3/"),
    "Lambda": ("AWS Lambda", "Learn serverless computing with Lambda.", "https://docs.aws.amazon.com/lambda/"),
    "RDS": ("AWS RDS", "Learn Amazon RDS.", "https://docs.aws.amazon.com/rds/"),
    "VPC": ("AWS VPC", "Learn Amazon VPC networking.", "https://docs.aws.amazon.com/vpc/"),
    "CloudWatch": ("AWS CloudWatch", "Learn monitoring with CloudWatch.", "https://docs.aws.amazon.com/cloudwatch/"),

    "Azure VM": ("Azure Virtual Machines", "Learn Azure VMs.", "https://learn.microsoft.com/en-us/azure/virtual-machines/"),
    "Azure Functions": ("Azure Functions", "Learn Azure serverless functions.", "https://learn.microsoft.com/en-us/azure/azure-functions/"),
    "Azure Storage": ("Azure Storage", "Learn Azure Storage.", "https://learn.microsoft.com/en-us/azure/storage/"),
    "Azure SQL": ("Azure SQL", "Learn Azure SQL.", "https://learn.microsoft.com/en-us/azure/azure-sql/"),
    "Entra ID": ("Microsoft Entra ID", "Learn identity and access management.", "https://learn.microsoft.com/en-us/entra/"),

    "Compute Engine": ("Google Compute Engine", "Learn Google Compute Engine.", "https://cloud.google.com/compute/docs"),
    "Cloud Storage": ("Google Cloud Storage", "Learn Google Cloud Storage.", "https://cloud.google.com/storage/docs"),
    "Cloud Run": ("Google Cloud Run", "Learn Cloud Run.", "https://cloud.google.com/run/docs"),
    "Vertex AI": ("Vertex AI", "Learn Google Vertex AI.", "https://cloud.google.com/vertex-ai/docs"),

    "Cloud Architecture": ("Cloud Architecture", "Learn cloud architecture.", "https://aws.amazon.com/architecture/"),
    "Serverless": ("Serverless Computing", "Learn serverless architecture.", "https://aws.amazon.com/serverless/"),
    "Containers": ("Containers", "Learn container technology.", "https://www.docker.com/101-tutorial/"),
    "Cloud Databases": ("Cloud Databases", "Learn cloud database concepts.", "https://cloud.google.com/learn/products/databases"),

    # ---------------- DEVOPS ----------------
    "Kubernetes": ("Kubernetes Documentation", "Learn Kubernetes.", "https://kubernetes.io/docs/tutorials/"),
    "CI/CD": ("CI/CD", "Learn continuous integration and delivery.", "https://docs.github.com/en/actions"),
    "Jenkins": ("Jenkins Documentation", "Learn Jenkins.", "https://www.jenkins.io/doc/"),
    "GitHub Actions": ("GitHub Actions", "Learn GitHub Actions.", "https://docs.github.com/en/actions"),
    "GitLab CI": ("GitLab CI/CD", "Learn GitLab CI/CD.", "https://docs.gitlab.com/ee/ci/"),
    "Terraform": ("Terraform Documentation", "Learn Terraform.", "https://developer.hashicorp.com/terraform/docs"),
    "Ansible": ("Ansible Documentation", "Learn Ansible.", "https://docs.ansible.com/"),
    "Prometheus": ("Prometheus Documentation", "Learn Prometheus.", "https://prometheus.io/docs/"),
    "Grafana": ("Grafana Documentation", "Learn Grafana.", "https://grafana.com/docs/"),
    "Monitoring": ("Monitoring", "Learn infrastructure monitoring.", "https://prometheus.io/docs/introduction/overview/"),
    "Observability": ("Observability", "Learn observability.", "https://opentelemetry.io/docs/"),
    "Infrastructure as Code": ("Infrastructure as Code", "Learn IaC.", "https://developer.hashicorp.com/terraform/tutorials"),

    # ---------------- MOBILE ----------------
    "Android Studio": ("Android Developers", "Learn Android development.", "https://developer.android.com/courses"),
    "Jetpack Compose": ("Jetpack Compose", "Learn modern Android UI.", "https://developer.android.com/develop/ui/compose"),
    "SwiftUI": ("SwiftUI", "Learn SwiftUI.", "https://developer.apple.com/tutorials/swiftui"),
    "Xcode": ("Xcode", "Learn Apple development with Xcode.", "https://developer.apple.com/xcode/"),
    "Flutter": ("Flutter Documentation", "Learn Flutter.", "https://docs.flutter.dev/"),
    "React Native": ("React Native", "Learn React Native.", "https://reactnative.dev/docs/getting-started"),

    # ---------------- UI/UX ----------------
    "Figma": ("Figma Learn", "Learn UI/UX design using Figma.", "https://help.figma.com/hc/en-us/categories/360002051613"),
    "Typography": ("Typography", "Learn typography fundamentals.", "https://www.interaction-design.org/literature/topics/typography"),
    "Color": ("Color in Design", "Learn color theory and design.", "https://www.interaction-design.org/literature/topics/color-theory"),
    "Layout": ("Layout Design", "Learn layout and visual hierarchy.", "https://www.interaction-design.org/literature/topics/visual-hierarchy"),
    "Design Systems": ("Design Systems", "Learn design systems.", "https://www.figma.com/community"),
    "Accessibility": ("Accessibility", "Learn accessible design.", "https://www.w3.org/WAI/fundamentals/accessibility-intro/"),
    "User Research": ("User Research", "Learn user research methods.", "https://www.nngroup.com/articles/user-research-methods/"),
    "Personas": ("User Personas", "Learn persona development.", "https://www.nngroup.com/articles/persona/"),
    "User Journeys": ("User Journeys", "Learn customer and user journey mapping.", "https://www.nngroup.com/articles/journey-mapping-101/"),
    "Wireframes": ("Wireframing", "Learn wireframing.", "https://www.figma.com/resource-library/what-is-a-wireframe/"),
    "Prototyping": ("Prototyping", "Learn interface prototyping.", "https://www.figma.com/resource-library/what-is-prototyping/"),
    "Usability Testing": ("Usability Testing", "Learn usability testing.", "https://www.nngroup.com/articles/usability-testing-101/"),
    "Information Architecture": ("Information Architecture", "Learn information architecture.", "https://www.nngroup.com/articles/definition-information-architecture/"),
    "Product Thinking": ("Product Thinking", "Learn product thinking.", "https://www.productplan.com/glossary/product-thinking/"),
    "Product Strategy": ("Product Strategy", "Learn product strategy.", "https://www.productplan.com/glossary/product-strategy/"),
    "UX Writing": ("UX Writing", "Learn UX writing.", "https://www.nngroup.com/articles/ux-writing-study-guide/"),
    "Product Analytics": ("Product Analytics", "Learn product analytics.", "https://www.productplan.com/glossary/product-analytics/"),

    # ---------------- ENGINEERING / GENERAL ----------------
    "AutoCAD": ("AutoCAD Learning", "Learn AutoCAD.", "https://www.autodesk.com/learn/ondemand"),
    "MATLAB": ("MATLAB Tutorials", "Learn MATLAB.", "https://www.mathworks.com/learn/tutorials/matlab-onramp.html"),
    "Simulink": ("Simulink Tutorials", "Learn Simulink.", "https://www.mathworks.com/learn/tutorials/simulink-onramp.html"),
    "SolidWorks": ("SOLIDWORKS Learning", "Learn SOLIDWORKS.", "https://my.solidworks.com/"),
    "CATIA": ("CATIA Learning", "Learn CATIA.", "https://www.3ds.com/edu/education/students"),
    "Creo": ("Creo Learning", "Learn PTC Creo.", "https://www.ptc.com/en/academic-program/k-12"),
    "ANSYS": ("Ansys Learning", "Learn engineering simulation.", "https://www.ansys.com/academic/learning-resources"),
    "Fusion 360": ("Fusion 360 Learning", "Learn Autodesk Fusion.", "https://www.autodesk.com/learn/ondemand"),
    "Siemens NX": ("Siemens NX Learning", "Learn Siemens NX.", "https://www.siemens.com/global/en/products/software/design-simcenter/nx.html"),
    "Revit": ("Revit Learning", "Learn Autodesk Revit.", "https://www.autodesk.com/learn/ondemand"),
    "SketchUp": ("SketchUp Campus", "Learn SketchUp.", "https://learn.sketchup.com/"),
    "Blender": ("Blender Tutorials", "Learn Blender.", "https://www.blender.org/support/tutorials/"),

    # ---------------- ROBOTICS / EMBEDDED ----------------
    "Arduino": ("Arduino Documentation", "Learn Arduino.", "https://docs.arduino.cc/"),
    "ESP32": ("ESP32 Documentation", "Learn ESP32 development.", "https://docs.espressif.com/projects/esp-idf/en/latest/esp32/"),
    "STM32": ("STM32 Learning", "Learn STM32 microcontrollers.", "https://www.st.com/content/st_com/en/stm32-education.html"),
    "Raspberry Pi": ("Raspberry Pi Documentation", "Learn Raspberry Pi.", "https://www.raspberrypi.com/documentation/"),
    "ROS": ("ROS Documentation", "Learn Robot Operating System.", "https://www.ros.org/"),
    "ROS/ROS2": ("ROS 2 Documentation", "Learn ROS 2.", "https://docs.ros.org/en/rolling/"),
    "Computer Vision": ("Computer Vision", "Learn computer vision.", "https://opencv.org/university/"),
    "OpenCV": ("OpenCV Tutorials", "Learn OpenCV.", "https://docs.opencv.org/"),
    "NVIDIA Jetson": ("NVIDIA Jetson", "Learn edge AI with NVIDIA Jetson.", "https://developer.nvidia.com/embedded/learn"),
    "Gazebo": ("Gazebo Documentation", "Learn robot simulation with Gazebo.", "https://gazebosim.org/docs"),

    # ---------------- BIOTECH ----------------
    "Molecular Biology": ("Molecular Biology", "Learn molecular biology.", "https://www.khanacademy.org/science/biology/macromolecules"),
    "Genetics": ("Genetics", "Learn genetics.", "https://www.khanacademy.org/science/biology/classical-genetics"),
    "Bioinformatics": ("Bioinformatics", "Learn bioinformatics.", "https://www.ncbi.nlm.nih.gov/education/"),
    "Biostatistics": ("Biostatistics", "Learn biostatistics.", "https://www.coursera.org/learn/biostatistics"),
    "Computational Biology": ("Computational Biology", "Learn computational biology.", "https://www.ncbi.nlm.nih.gov/education/"),
    "BLAST": ("NCBI BLAST", "Learn sequence analysis with BLAST.", "https://blast.ncbi.nlm.nih.gov/"),
    "Bioconductor": ("Bioconductor", "Learn bioinformatics with Bioconductor.", "https://bioconductor.org/learn/"),
    "Galaxy": ("Galaxy Training", "Learn Galaxy bioinformatics.", "https://training.galaxyproject.org/"),
    "Bioinformatics Databases": ("NCBI Resources", "Learn biological databases.", "https://www.ncbi.nlm.nih.gov/"),
    "Biomedical Data Science": ("Biomedical Data Science", "Learn biomedical data science.", "https://www.ncbi.nlm.nih.gov/education/"),
    "AI for Healthcare": ("AI for Healthcare", "Learn applications of AI in healthcare.", "https://www.nibib.nih.gov/science-education/science-topics/artificial-intelligence"),
    "Genomics": ("Genomics", "Learn genomics.", "https://www.genome.gov/about-genomics"),
    "Drug Discovery": ("Drug Discovery", "Learn computational approaches to drug discovery.", "https://www.ebi.ac.uk/training/"),

    # ---------------- BUSINESS ----------------
    "Requirements Gathering": ("Requirements Gathering", "Learn business requirements gathering.", "https://www.atlassian.com/agile/project-management/requirements"),
    "Process Mapping": ("Process Mapping", "Learn business process mapping.", "https://www.lucidchart.com/pages/process-mapping"),
    "Documentation": ("Technical Documentation", "Learn documentation practices.", "https://www.atlassian.com/software/confluence/guides"),
    "Agile": ("Agile", "Learn Agile methodology.", "https://www.atlassian.com/agile"),
    "Scrum": ("Scrum Guide", "Learn Scrum.", "https://scrumguides.org/"),
    "Jira": ("Jira Learning", "Learn Jira project management.", "https://www.atlassian.com/software/jira/guides"),
    "Stakeholder Management": ("Stakeholder Management", "Learn stakeholder management.", "https://www.pmi.org/"),
    "Project Management": ("Project Management", "Learn project management.", "https://www.pmi.org/learning"),
    "Product Management": ("Product Management", "Learn product management.", "https://www.atlassian.com/agile/product-management"),
    "Operations": ("Operations Management", "Learn operations management.", "https://www.coursera.org/browse/business/operations"),
    "Strategy": ("Business Strategy", "Learn business strategy.", "https://www.coursera.org/browse/business/strategy"),
    "Leadership": ("Leadership", "Learn leadership skills.", "https://www.coursera.org/browse/business/leadership-and-management"),

    # ---------------- FINANCE ----------------
    "Accounting": ("Accounting", "Learn accounting fundamentals.", "https://www.khanacademy.org/economics-finance-domain/core-finance/accounting-and-financial-statements"),
    "Financial Analysis": ("Financial Analysis", "Learn financial analysis.", "https://www.investopedia.com/financial-analysis-4689817"),
    "Financial Modeling": ("Financial Modeling", "Learn financial modeling.", "https://www.wallstreetprep.com/knowledge/financial-modeling/"),
    "Investment": ("Investment Fundamentals", "Learn investment fundamentals.", "https://www.investor.gov/introduction-investing"),
    "Risk": ("Financial Risk", "Learn risk management.", "https://www.investopedia.com/terms/r/riskmanagement.asp"),
    "Budgeting": ("Budgeting", "Learn budgeting.", "https://www.investor.gov/financial-tools-calculators/calculators/compound-interest-calculator"),
    "FinTech": ("FinTech", "Learn financial technology.", "https://www.coursera.org/browse/business/fintech"),
    "Blockchain": ("Blockchain", "Learn blockchain fundamentals.", "https://ethereum.org/en/learn/"),
    "Digital Payments": ("Digital Payments", "Learn digital payment technology.", "https://www.rbi.org.in/"),
    "AI in Finance": ("AI in Finance", "Learn AI applications in finance.", "https://www.coursera.org/"),

    # ---------------- HR ----------------
    "Recruitment": ("Recruitment", "Learn recruitment fundamentals.", "https://www.coursera.org/learn/recruiting-hiring-onboarding-employees"),
    "Talent Acquisition": ("Talent Acquisition", "Learn talent acquisition.", "https://www.coursera.org/"),
    "Performance Management": ("Performance Management", "Learn performance management.", "https://www.coursera.org/"),
    "Employee Engagement": ("Employee Engagement", "Learn employee engagement.", "https://www.coursera.org/"),
    "Payroll": ("Payroll Fundamentals", "Learn payroll fundamentals.", "https://www.coursera.org/"),
    "HR Operations": ("HR Operations", "Learn HR operations.", "https://www.coursera.org/"),
    "HR Analytics": ("HR Analytics", "Learn HR analytics.", "https://www.coursera.org/"),
    "HRIS": ("HRIS", "Learn human resources information systems.", "https://www.coursera.org/"),
    "People Analytics": ("People Analytics", "Learn people analytics.", "https://www.coursera.org/"),
    "AI Recruitment": ("AI Recruitment", "Learn AI applications in recruitment.", "https://www.coursera.org/"),
    "Workforce Analytics": ("Workforce Analytics", "Learn workforce analytics.", "https://www.coursera.org/"),

    # ---------------- MARKETING ----------------
    "SEO": ("SEO", "Learn search engine optimization.", "https://developers.google.com/search/docs"),
    "SEM": ("Search Engine Marketing", "Learn search engine marketing.", "https://skillshop.withgoogle.com/"),
    "Social Media": ("Social Media Marketing", "Learn social media marketing.", "https://www.coursera.org/browse/business/marketing"),
    "Email Marketing": ("Email Marketing", "Learn email marketing.", "https://academy.hubspot.com/courses/email-marketing"),
    "Content Marketing": ("Content Marketing", "Learn content marketing.", "https://academy.hubspot.com/courses/content-marketing"),
    "Affiliate Marketing": ("Affiliate Marketing", "Learn affiliate marketing.", "https://www.coursera.org/"),
    "Performance Marketing": ("Performance Marketing", "Learn performance marketing.", "https://skillshop.withgoogle.com/"),
    "Google Analytics": ("Google Analytics", "Learn Google Analytics.", "https://analytics.google.com/analytics/academy/"),
    "Search Console": ("Google Search Console", "Learn Google Search Console.", "https://search.google.com/search-console/about"),
    "Meta Ads": ("Meta Ads", "Learn Meta advertising.", "https://www.facebook.com/business/learn"),
    "Google Ads": ("Google Ads", "Learn Google Ads.", "https://skillshop.withgoogle.com/"),
    "Marketing Dashboards": ("Marketing Dashboards", "Learn marketing dashboards.", "https://lookerstudio.google.com/"),
    "AI Content": ("AI Content", "Learn AI-assisted content creation.", "https://www.coursera.org/"),
    "AI Research": ("AI Research", "Learn AI-assisted research.", "https://www.coursera.org/"),
    "Marketing Automation": ("Marketing Automation", "Learn marketing automation.", "https://academy.hubspot.com/"),
    "Personalization": ("Marketing Personalization", "Learn personalization.", "https://academy.hubspot.com/"),
    "AI-assisted Advertising": ("AI Advertising", "Learn AI-assisted advertising.", "https://skillshop.withgoogle.com/"),

    # ---------------- CREATOR ----------------
    "YouTube": ("YouTube Creator Academy", "Learn YouTube content creation.", "https://creatoracademy.youtube.com/"),
    "Instagram": ("Instagram for Creators", "Learn Instagram content creation.", "https://creators.instagram.com/"),
    "LinkedIn": ("LinkedIn Learning", "Learn professional content creation.", "https://www.linkedin.com/learning/"),
    "Blogging": ("Blogging", "Learn blogging and content creation.", "https://www.w3schools.com/"),
    "Copywriting": ("Copywriting", "Learn copywriting.", "https://www.coursera.org/"),
    "Scriptwriting": ("Scriptwriting", "Learn scriptwriting.", "https://www.coursera.org/"),
    "Storytelling": ("Storytelling", "Learn storytelling.", "https://www.coursera.org/"),

    "DaVinci Resolve": ("DaVinci Resolve Training", "Learn video editing with DaVinci Resolve.", "https://www.blackmagicdesign.com/products/davinciresolve/training"),
    "Premiere Pro": ("Adobe Premiere Pro Tutorials", "Learn video editing with Premiere Pro.", "https://helpx.adobe.com/premiere-pro/tutorials.html"),
    "CapCut": ("CapCut Tutorials", "Learn video editing with CapCut.", "https://www.capcut.com/"),
    "After Effects": ("Adobe After Effects Tutorials", "Learn motion graphics with After Effects.", "https://helpx.adobe.com/after-effects/tutorials.html"),
    "Canva": ("Canva Design School", "Learn Canva.", "https://www.canva.com/designschool/"),
    "Photoshop": ("Adobe Photoshop Tutorials", "Learn Photoshop.", "https://helpx.adobe.com/photoshop/tutorials.html"),
    "Illustrator": ("Adobe Illustrator Tutorials", "Learn Illustrator.", "https://helpx.adobe.com/illustrator/tutorials.html"),
    "Maya": ("Autodesk Maya Learning", "Learn Autodesk Maya.", "https://www.autodesk.com/learn/ondemand"),
    "Unreal Engine": ("Unreal Engine Learning", "Learn Unreal Engine.", "https://dev.epicgames.com/community/unreal-engine/learning"),

    # ---------------- FREELANCING ----------------
    "Finding Clients": ("Finding Freelance Clients", "Learn how to find freelance clients.", "https://www.upwork.com/resources/how-to-find-freelance-work"),
    "Proposal Writing": ("Proposal Writing", "Learn freelance proposal writing.", "https://www.upwork.com/resources/how-to-write-a-proposal"),
    "Pricing": ("Freelance Pricing", "Learn freelance pricing strategies.", "https://www.upwork.com/resources/how-to-set-freelance-rates"),
    "Negotiation": ("Negotiation", "Learn negotiation skills.", "https://www.coursera.org/learn/negotiation-skills"),
    "Client Communication": ("Client Communication", "Learn professional client communication.", "https://www.coursera.org/"),
    "Portfolio Building": ("Portfolio Building", "Learn how to build a professional portfolio.", "https://www.coursera.org/"),
    "Personal Branding": ("Personal Branding", "Learn personal branding.", "https://www.coursera.org/"),
    "Contracts": ("Freelance Contracts", "Learn freelance contract fundamentals.", "https://www.upwork.com/resources/freelance-contract"),
    "Invoicing": ("Freelance Invoicing", "Learn invoicing fundamentals.", "https://www.upwork.com/resources/freelance-invoice"),

    "WordPress": ("WordPress Learn", "Learn WordPress.", "https://learn.wordpress.org/"),
    "Shopify": ("Shopify Academy", "Learn Shopify.", "https://www.shopify.com/learn"),
    "HTML/CSS": ("HTML and CSS", "Learn HTML and CSS.", "https://www.w3schools.com/html/"),
    "Hosting": ("Web Hosting", "Learn web hosting fundamentals.", "https://www.cloudflare.com/learning/"),
    "APIs": ("APIs", "Learn API development and integration.", "https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps/Introduction"),

    "AI Automation": ("AI Automation", "Learn AI automation.", "https://www.coursera.org/"),
    "Chatbots": ("Chatbots", "Learn chatbot development.", "https://www.ibm.com/think/topics/chatbots"),
    "Workflow Automation": ("Workflow Automation", "Learn workflow automation.", "https://zapier.com/learn/automation/"),
    "AI Integration": ("AI Integration", "Learn AI application integration.", "https://huggingface.co/learn"),

    # ---------------- PROFESSIONAL SKILLS ----------------
    "Communication": ("Communication Skills", "Improve professional communication.", "https://www.coursera.org/browse/personal-development/communication"),
    "English": ("English Learning", "Improve English communication.", "https://learnenglish.britishcouncil.org/"),
    "Critical Thinking": ("Critical Thinking", "Develop critical thinking.", "https://www.coursera.org/"),
    "Problem Solving": ("Problem Solving", "Develop problem-solving skills.", "https://www.coursera.org/"),
    "Creativity": ("Creativity", "Develop creativity and innovation.", "https://www.coursera.org/"),
    "Collaboration": ("Collaboration", "Develop teamwork and collaboration.", "https://www.coursera.org/"),
    "Time Management": ("Time Management", "Improve time management.", "https://www.coursera.org/"),
    "Presentation": ("Presentation Skills", "Improve presentation skills.", "https://www.coursera.org/"),
    "Adaptability": ("Adaptability", "Develop adaptability and workplace skills.", "https://www.coursera.org/"),
    "Resume": ("Resume Building", "Learn how to build a strong resume.", "https://www.indeed.com/career-advice/resumes-cover-letters"),
    "Portfolio": ("Portfolio Building", "Learn how to build a professional portfolio.", "https://www.coursera.org/"),
    "Interview Skills": ("Interview Skills", "Learn interview preparation skills.", "https://www.indeed.com/career-advice/interviewing"),
    "AI Tools": ("AI Tools", "Learn modern AI tools.", "https://www.coursera.org/"),
    "Prompting": ("Prompting", "Learn effective AI prompting.", "https://www.promptingguide.ai/"),
    "AI Productivity": ("AI Productivity", "Learn how AI can improve productivity.", "https://www.coursera.org/"),
    "AI Verification": ("AI Verification", "Learn how to verify AI-generated information.", "https://www.nist.gov/itl/ai-risk-management-framework"),
}


# ============================================================
# Department fallback resources
# ============================================================

DEPARTMENT_RESOURCES = {
    "Computer Science & IT":
        "https://www.w3schools.com/",
    "Web & Full-Stack Development":
        "https://developer.mozilla.org/en-US/docs/Learn",
    "AI & ML":
        "https://developers.google.com/machine-learning/crash-course",
    "Data Science & Analytics":
        "https://www.kaggle.com/learn",
    "Cybersecurity":
        "https://www.nist.gov/cyberframework",
    "Cloud Computing":
        "https://aws.amazon.com/training/",
    "DevOps & SRE":
        "https://kubernetes.io/docs/tutorials/",
    "Mobile Development":
        "https://developer.android.com/courses",
    "UI/UX & Product Design":
        "https://www.figma.com/resources/learn-design/",
    "Civil Engineering":
        "https://www.nptel.ac.in/courses",
    "Mechanical Engineering":
        "https://www.nptel.ac.in/courses",
    "Electrical Engineering":
        "https://www.nptel.ac.in/courses",
    "Electronics & Communication":
        "https://www.nptel.ac.in/courses",
    "Architecture":
        "https://www.nptel.ac.in/courses",
    "Robotics & Automation":
        "https://www.ros.org/",
    "Biotechnology":
        "https://www.ncbi.nlm.nih.gov/education/",
    "Chemical Engineering":
        "https://www.nptel.ac.in/courses",
    "Business & Management":
        "https://www.coursera.org/browse/business",
    "Finance & Accounting":
        "https://www.investor.gov/",
    "HR & People":
        "https://www.coursera.org/browse/business/human-resources",
    "Marketing & Digital Marketing":
        "https://skillshop.withgoogle.com/",
    "Content & Creator Skills":
        "https://creatoracademy.youtube.com/",
    "Freelancing":
        "https://www.upwork.com/resources",
    "Entrepreneurship":
        "https://www.coursera.org/browse/business/entrepreneurship",
    "Professional & Future Skills":
        "https://www.coursera.org/browse/personal-development",
}


def get_department(skill):
    """
    Find the department through:
    Skill -> CareerSkill -> Career -> Department
    """
    try:
        if skill.career_links:
            for link in skill.career_links:
                if link.career and link.career.department:
                    return link.career.department.name
    except Exception:
        pass

    return None


def main():
    db = SessionLocal()

    added = 0
    skipped = 0
    fallback = 0

    try:
        skills = db.query(Skill).order_by(Skill.id).all()

        print("=" * 70)
        print("SkillBridge AI - Complete Learning Resource Seeder")
        print("=" * 70)
        print("Skills found:", len(skills))
        print()

        for skill in skills:

            # Check whether a resource already exists for this exact skill.
            existing = (
                db.query(Course)
                .filter(Course.skill.ilike(skill.name))
                .first()
            )

            if existing:
                skipped += 1
                continue

            # ------------------------------------------------
            # 1. Specific resource
            # ------------------------------------------------
            if skill.name in RESOURCE_MAP:

                title, description, url = RESOURCE_MAP[skill.name]

                department = get_department(skill)

                if not department:
                    department = "General"

                course = Course(
                    title=title,
                    description=description,
                    department=department,
                    category="Learning Resource",
                    skill=skill.name,
                    level="Beginner",
                    provider="Official / Learning Resource",
                    duration="Self-paced",
                    url=url
                )

                db.add(course)
                added += 1

            # ------------------------------------------------
            # 2. Department fallback
            # ------------------------------------------------
            else:

                department = get_department(skill)

                if department and department in DEPARTMENT_RESOURCES:

                    url = DEPARTMENT_RESOURCES[department]

                    course = Course(
                        title=f"{skill.name} - Learning Resource",
                        description=(
                            f"Learning resource for {skill.name} "
                            f"under {department}."
                        ),
                        department=department,
                        category="Learning Resource",
                        skill=skill.name,
                        level="Beginner",
                        provider="Recommended Learning Platform",
                        duration="Self-paced",
                        url=url
                    )

                    db.add(course)
                    added += 1
                    fallback += 1

        db.commit()

        total = db.query(Course).count()

        print("=" * 70)
        print("RESOURCE SEEDING COMPLETED")
        print("=" * 70)
        print("Resources added   :", added)
        print("Department fallback:", fallback)
        print("Resources skipped :", skipped)
        print("Total courses     :", total)
        print("Skills covered    :", len(skills))
        print("=" * 70)

    except Exception as e:
        db.rollback()
        print()
        print("ERROR:", e)
        raise

    finally:
        db.close()


if __name__ == "__main__":
    main()