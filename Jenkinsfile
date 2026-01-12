pipeline {
    agent any

    environment {
        SCANNER_HOME = tool 'sonar-scanner'
        SONARQUBE = 'Jenkins-Sonar-Server'
        DOCKER_IMAGE = 'addition1905/jandevopstwo:latest'
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out code from repository...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building the project...'
                // sh 'npm install'
                // sh 'python3 setup.py build'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                // sh 'npm test'
                // sh 'pytest'
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
                          -Dsonar.sourceEncoding=UTF-8
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
                    def img = docker.build("${DOCKER_IMAGE}")
                    docker.withRegistry('https://index.docker.io/v1/', 'sonar-tokenJ') {
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
            echo 'Pipeline failed. Check the logs for details.'
        }
        always {
            echo 'Pipeline execution finished.'
        }
    }
}
