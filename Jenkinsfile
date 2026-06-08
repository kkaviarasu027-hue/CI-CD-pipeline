node {
    stage('Checkout Code') {
        // This pulls your code from the GitHub repository branch
        checkout scm
        echo 'Code checked out successfully!'
    }

    stage('Install Dependencies') {
        // Runs your installation command on Windows PowerShell/CMD
        echo 'Installing required libraries...'
        bat 'pip install -r requirements.txt'
    }

    stage('Run Selenium Tests') {
        // Triggers your Selenium automated test runner
        echo 'Running automation framework...'
        bat 'pytest'
    }
}
