pipeline {
    agent any

    stages {
        stage('Test development version') {
            when {
                not {
                    branch 'master'
                }
            }
            steps {
                sh 'echo "running tests"'
            }
        }
        stage('Build nightly image') {
            when {
                branch 'master'
            }
            steps {
                println 'test me baby one more time'
            }
        }
    }
}
