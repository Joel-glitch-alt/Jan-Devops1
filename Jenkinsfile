pipeline {
    agent any
    
    environment {
        SCANNER_HOME = tool 'sonar-scanner'
        SONARQUBE = 'Jenkins-sonar-server'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
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
                          -Dsonar.language=py \
                          -Dsonar.sourceEncoding=UTF-8
                    '''
                }
            }
        }
    }
}