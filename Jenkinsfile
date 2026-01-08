pipeline {
    agent any
      environment {
       // SCANNER_HOME = tool 'sonar-scanner' // Jenkins > Global Tool Configuration > SonarScanner name
        SONARQUBE = 'Jenkins-sonar-server'         // Jenkins > Configure System > SonarQube server name
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
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonar-server') {
                    sh '''
                        ${SCANNER_HOME}/bin/sonar-scanner \
                          -Dsonar.projectKey=my_project_key \
                          -Dsonar.projectName="My JS Project" \
                          -Dsonar.sources=./src \
                          -Dsonar.javascript.lcov.reportPaths=coverage/lcov.info \
                          -Dsonar.sourceEncoding=UTF-8
                    '''
                }
            }
        }

       stage('Quality Gate') {
    steps {
        timeout(time: 5, unit: 'MINUTES') {
            waitForQualityGate abortPipeline: true
        }
    }
    }
    }
}