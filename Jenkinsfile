// @Library('testshared') _

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
                // script {
                //     buildPythonPackage()
                // }
                println "Build Python package"
            }
        }
    }
}