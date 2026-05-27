pipeline {
    agent any

    tools {
        // Points to the Allure configuration name we saved in Jenkins Global Tools
        allure 'allure'
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Pulling framework files from GitHub...'
            }
        }

        stage('Install Environment & Run Tests') {
            steps {
                echo 'Setting up project environment and running Playwright scripts...'
                // For Windows systems running Python Playwright:
                bat '''
                pip install -r requirements.txt
                pytest --alluredir=allure-results
                '''
            }
        }
    }

    post {
        always {
            // This reads your allure-results JSON logs and builds the dashboard webpage
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
}