pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Pulling framework files from GitHub...'
            }
        }

        stage('Install Environment & Run Tests') {
            steps {
                echo 'Setting up project environment and running Playwright scripts...'
                bat '''
                pip install -r requirements.txt
                pytest --alluredir=allure-results
                '''
            }
        }
    }

    post {
        always {
            // This builds the dashboard webpage directly from your results folder
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
}