#!groovy


pipeline {
	environment {
      branch = ${env.GIT_BRANCH}
      evni = ${env.ENVIRONMENT}
	}

	options {
		timestamps()
		lock(evni)
	}

	stages {
		stage('plan') {
			steps {
				script {
					if (branch == 'main') {
						env.ENVIRONMENT = 'production'
					} else {
						env.ENVIRONMENT = 'staging'
					}
					sh """
						echo "Hello, World!"
					"""
					// sh 'terraform init'
					// sh 'terraform plan -out myplan'
				}
			}
		}

		stage('Test') {	
			steps {
				sh """
					echo "Hello, World!"
				"""
			}
		}

		stage('Deploy') {
			steps {
				sh "terraform apply -var 'environment=${evni}' -var 'tag_name=${env.GIT_BRANCH}'"
			}
		}

	}
}
