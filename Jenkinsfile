pipeline {
    agent any
    stages {
        stage('Clone Repo') {
            steps {
                echo 'Cloning repository...'
            }
        }
        stage('Run Python Script') {
            steps {
                sh 'python3 main.py || python main.py'
            }
        }
    }
}
