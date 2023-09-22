stage("Checkout"){
    checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/icsbariboa/WorldOfGames']])
}
stage("Build"){
    sh "docker build -t 'score_server' https://github.com/icsbariboa/WorldOfGames/blob/master/Dockerfile.txt"
}
stage("Run"){
    docker run --name score_server1 score_server
}
stage("Test"){
    def Test_result = sh "python e2e.py"
    if(Test_result.equals(-1){
        error "The test failed! score is not between 0 to 1000"
    }
)
stage("Finalize"){
    sh "docker stop score_server1"
    sh "docker image push icsbariboa/score_server"
}