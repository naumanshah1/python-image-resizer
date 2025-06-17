pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t image-resizer .'
            }
        }

        stage('Run Container (Test)') {
            steps {
                sh 'docker run -d -p 5000:5000 --name image-resizer image-resizer'
            }
        }
    }
}
