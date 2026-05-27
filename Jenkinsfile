pipeline {
    agent any

    tools {
        // Tells Jenkins to use the Allure tool configuration we just named
        allure 'allure'
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Pulling framework files from GitHub...'
            }
        }

        stage('Run Playwright Tests') {
            steps {
                echo 'Executing test suites...'
                // If running Node-based Playwright:
                // bat 'npm install && npx playwright test'

                // If running Python-based Playwright/Pytest:
                // bat 'pip install -r requirements.txt && pytest --alluredir=allure-results'
            }
        }
    }

    post {
        always {
            // This hook reads your allure-results folder and builds the dashboard webpage
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
}