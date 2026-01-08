pipeline {
    agent any
    
    environment {
        SCANNER_HOME = tool 'sonar-scanner' // UNCOMMENTED - Jenkins > Global Tool Configuration > SonarScanner name
        SONARQUBE = 'Jenkins-sonar-server'  // Jenkins > Configure System > SonarQube server name
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
                // Add your build commands here
                // For Python: sh 'python3 setup.py build'
                // For Node.js: sh 'npm install'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                // Add your test commands here
                // For Python: sh 'python3 -m pytest'
                // For Node.js: sh 'npm test'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                // FIXED: Changed 'sonar-scanner' to match SONARQUBE variable
                withSonarQubeEnv("${SONARQUBE}") {
                    sh '''
                        ${SCANNER_HOME}/bin/sonar-scanner \
                          -Dsonar.projectKey=my_project_key \
                          -Dsonar.projectName="My Project" \
                          -Dsonar.sources=. \
                          -Dsonar.sourceEncoding=UTF-8
                    '''
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 10, unit: 'MINUTES') {
                    script {
                        def qg = waitForQualityGate()
                        if (qg.status != 'OK') {
                            echo "Quality Gate failed: ${qg.status}"
                            // Change to 'true' to fail the pipeline on quality gate failure
                            // abortPipeline: false means it will continue
                        }
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