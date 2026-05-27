pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Pulling code from GitHub...'
            }
        }
        stage('Install Dependencies') {
            steps {
                echo 'Setting up environment...'
                // If you use requirements.txt later, you can add commands here
            }
        }
        stage('Run Automation') {
            steps {
                echo 'Executing python scripts...'
                // This is where your test execution command will go
            }
        }
    }
}