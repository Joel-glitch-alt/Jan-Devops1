pipeline {
    agent any

    environment {
        SCANNER_HOME = tool 'sonar-scanner'
        SONARQUBE = 'Jenkins-Sonar-Server'
        DOCKER_IMAGE = 'addition1905/jandevopstwo'
        DOCKER_TAG = "${env.BUILD_NUMBER}"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building the project...'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh '''
                pip install -r requirements.txt
                pytest --cov=. --cov-report=xml
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv("${SONARQUBE}") {
                    sh """
                        ${SCANNER_HOME}/bin/sonar-scanner \
                          -Dsonar.projectKey=jan_devops_key \
                          -Dsonar.projectName=JanDevOps1 \
                          -Dsonar.sources=. \
                          -Dsonar.sourceEncoding=UTF-8 \
                          -Dsonar.python.coverage.reportPaths=coverage.xml
                    """
                }
            }
        }

        // stage('Quality Gate') {
        //     steps {
        //         timeout(time: 10, unit: 'MINUTES') {
        //             script {
        //                 def qg = waitForQualityGate()
        //                 if (qg.status != 'OK') {
        //                     error "Quality Gate failed: ${qg.status}"
        //                 }
        //             }
        //         }
        //     }
        // }

        stage('Docker Build & Push') {
            steps {
                script {
                    def img = docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                    docker.withRegistry(
                        'https://index.docker.io/v1/',
                        'docker-hub-credentials'
                    ) {
                        img.push()
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs for details.'
        }
        always {
            echo 'Pipeline execution finished.'
        }
    }
}
