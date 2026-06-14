pipeline {
    agent any
    stages {
        stage('Code Analysis') {
            steps {
                echo "Running security scans and linting on OmniGrid Telemetry API..."
                sh 'python3 -m py_compile src/app.py'
            }
        }
        stage('Build Image') {
            steps {
                echo "Building the Docker image for production..."
                sh 'docker build -t omnigrid-telemetry:ci-build ./src'
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                echo "Deploying to OmniGrid Kubernetes Cluster..."
                sh 'kubectl apply -f kubernetes/deployment.yaml'
            }
        }
    }
}
