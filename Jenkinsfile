pipeline {
    agent any

    environment {
        MLFLOW_TRACKING_URI = "http://172.31.0.10:5000"
        MLFLOW_ARTIFACT_URI = "http://172.31.0.10:5000/api/2.0/mlflow-artifacts/artifacts"
        PYTHONUNBUFFERED = "1"
        VENV = ".venv"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                python3 -m venv $VENV
                . $VENV/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Experiment') {
            steps {
                sh '''
                . $VENV/bin/activate
                python experiment.py
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Experimento executado com sucesso"
        }
        always {
            cleanWs()
        }
    }
}
