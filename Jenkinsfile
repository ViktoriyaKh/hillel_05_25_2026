pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                bat 'C:\\Users\\m-gio\\AppData\\Local\\Python\\bin\\python.exe -m venv .venv'
                bat '.venv\\Scripts\\python.exe -m pip install -r requirements.txt'
                bat '.venv\\Scripts\\python.exe -m playwright install'
            }
        }

        stage('Run tests') {
            steps {
                bat '.venv\\Scripts\\python.exe -m pytest test_registration.py --junitxml=test-results.xml'
            }
        }

        stage('Publish test results') {
            steps {
                junit 'test-results.xml'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished'
        }

        success {
            echo 'Tests passed successfully'
        }

        failure {
            echo 'Tests failed'
        }
    }
}