pipeline {
    agent any

    stages {
        stage('Hello, World!') {
            steps {
                script {
                    timestamps {
                        script {
                             sh"""
                                echo "Hello, World!" 
                            """
                        }
                    }
                }
            }
        }
    }
}
