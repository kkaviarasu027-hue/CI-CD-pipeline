pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
                echo 'Code pulled from GitHub successfully!'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Preparing environment...'
                // If you have a requirements file in your repo:
                // bat 'pip install -r requirements.txt'
            }
        }

        stage('Execute Test Suite') {
            steps {
                echo 'Running local test automation...'
                // bat 'pytest'
            }
        }
    }
}
