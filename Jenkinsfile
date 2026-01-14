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

        // stage('Test') {
        //     steps {
        //         echo 'Running tests...'
        //         sh '''
        //         # create a virtual environment
        //         python3 -m venv venv

        //         # activate the virtual environment
        //         source venv/bin/activate

        //         # upgrade pip
        //         pip install --upgrade pip

        //         # install dependencies
        //         pip install -r requirements.txt

        //         # run tests
        //         pytest --cov=. --cov-report=xml
        //         '''
        //     }
        // }


      stage('Test') {
    steps {
        echo 'Running tests...'
        sh '''
        python3 -m venv venv
        venv/bin/pip install --upgrade pip
        venv/bin/pip install -r requirements.txt
        venv/bin/pytest --cov=. --cov-report=xml
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
