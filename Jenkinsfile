pipeline {
    agent any

    environment {
        DOCKER_USERNAME = "ramyareddy120"
        IMAGE_NAME = "ramyareddy120/sample-2026"
        IMAGE_TAG = "latest"
    }

    stages {

        stage('Checkout') {
            steps {
                echo "Checking out source code..."
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker Image..."
                bat "docker build -t %IMAGE_NAME%:%IMAGE_TAG% ."
            }
        }

        stage('Docker Login') {
            steps {
                echo "Logging in to Docker Hub..."
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-new',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                   powershell '$env:DOCKER_PASS | docker login -u $env:DOCKER_USER --password-stdin'
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                echo "Pushing Docker Image to Docker Hub..."
                bat "docker push %IMAGE_NAME%:%IMAGE_TAG%"
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "Deploying application to Kubernetes..."
                bat "kubectl apply -f deployment.yaml --validate=false"
                bat "kubectl apply -f service.yaml"
            }
        }

        stage('Verify Kubernetes Deployment') {
            steps {
                echo "Checking Kubernetes resources..."
                bat "kubectl get deployments"
                bat "kubectl get pods"
                bat "kubectl get services"
            }
        }
    }

    post {
        success {
            echo "PIPELINE COMPLETED SUCCESSFULLY!"
            echo "Docker Image: %IMAGE_NAME%:%IMAGE_TAG%"
            echo "Kubernetes deployment completed successfully!"
        }

        failure {
            echo "PIPELINE FAILED!"
            echo "Please check the Jenkins console output."
        }
    }
}