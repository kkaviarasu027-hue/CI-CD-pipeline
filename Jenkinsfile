pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Pulling framework files from GitHub...'
            }
        }

        stage('Install Dependencies & Run Playwright Tests') {
            steps {
                echo 'Installing npm packages and executing JS automation suite...'
                // Running Windows batch commands for Node.js Playwright execution
                bat '''
                npm install
                npx playwright test --reporter=line,allure-playwright
                '''
            }
        }
    }

    post {
        always {
            // This reads your generated allure-results folder and updates your UI graphs
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
}