Mock Image Analyzer – DevOps Pipeline Project
📌 Project Overview

This project is a Mock Image Analyzer built with Python and integrated into a complete DevOps CI/CD pipeline using Jenkins, Docker, SonarQube, and AWS EC2.

The application simulates image analysis by:

Generating a unique image ID

Assigning a random skin type

Detecting a mock skin issue

Producing a confidence score

The pipeline automates testing, code quality analysis, Docker image creation, and image push to Docker Hub.


🧱 Tech Stack

Language: Python 3

Testing: Pytest + Coverage

CI/CD: Jenkins Pipeline

Code Quality: SonarQube

Containerization: Docker



📂 Project Structure
.
├── main.py                 # Application source code
├── test_main.py            # Unit tests
├── Jenkinsfile             # Jenkins pipeline
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation


🚀 Application Features

Random image ID generation

Mock image analysis

Result persistence to file

Loading of previous analysis results

Command-line interaction

⚙️ Jenkins CI/CD Pipeline Stages

The Jenkins pipeline includes the following stages:

Checkout

Pulls source code from SCM

Build

Prepares the project environment

Test

Creates a virtual environment

Installs dependencies

Runs Pytest with coverage

SonarQube Analysis

Performs static code analysis

Uploads coverage report

Quality Gate

(Currently skipped for demo purposes)

Docker Build & Push

Builds Docker image

Pushes image to Docker Hub

🐳 Docker

Docker images are built and pushed automatically by Jenkins.

Image Format

addition1905/jandevopstwo:<BUILD_NUMBER>


☁️ AWS Deployment

Jenkins and SonarQube are hosted on AWS EC2

EC2 instance is configured with:

Docker

Jenkins

SonarQube

Docker images can be pulled and run on EC2

▶️ Run the Application
python main.py


You will be prompted to enter an image name, after which the analysis result will be generated and saved.

📈 SonarQube Metrics

Code coverage

Bugs & vulnerabilities

Code smells

Maintainability rating

🔐 Credentials & Security

Docker Hub credentials stored securely in Jenkins

SonarQube authentication handled via Jenkins environment configuration


✅ Future Improvements

Real image processing integration

Enforce SonarQube Quality Gate

Kubernetes deployment

Logging and monitoring

REST API support

👤 Author

Joel Addition
AWS | Docker | Jenkins | SonarQube | CI/CD

Cloud: AWS EC2

Version Control: Git
