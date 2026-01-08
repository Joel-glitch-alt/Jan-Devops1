pipeline {
    agent any
    
    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out code from repository...'
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo 'Hello World!'
            }
        }

        // stage('Hello') {
        //     steps {
        //         echo 'Hello World!'
        //     }
        // }
    }
}