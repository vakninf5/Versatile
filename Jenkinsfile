pipeline {
    agent any

stage('plan') {
   steps {
      script {
         if (branch == 'main') {
            env.ENVIRONMENT = 'production'
         } else {
            env.ENVIRONMENT = 'staging'
         }
         sh 'terraform init'
         sh 'terraform plan -out myplan'
      }
   }
}

stage('Test') {
   steps {
      // test steps here
   }
}

stage('Deploy') {
   steps {
      sh "terraform apply -var 'environment=${env.ENVIRONMENT}' -var 'tag_name=${env.GIT_BRANCH}'"
   }
}










}
