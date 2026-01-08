pipeline {
    agent {
        docker {
            image 'python:3.13-alpine'
            args '-u root'
        }
    }

    environment {
        SONARQUBE = 'Jenkins-sonar-server'
        SCANNER_HOME = '/opt/sonar-scanner'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                  apk add --no-cache openjdk17 curl unzip
                  
                  curl -L https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-5.0.1.3006-linux.zip -o sonar-scanner.zip
                  unzip sonar-scanner.zip
                  mv sonar-scanner-* /opt/sonar-scanner
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv("${SONARQUBE}") {
                    sh '''
                      ${SCANNER_HOME}/bin/sonar-scanner \
                        -Dsonar.projectKey=JanDevopsPython \
                        -Dsonar.projectName="Jan DevOps Python" \
                        -Dsonar.sources=. \
                        -Dsonar.sourceEncoding=UTF-8
                    '''
                }
            }
        }
    }
}
