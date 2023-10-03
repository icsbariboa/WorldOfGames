properties([githubProjectProperty(displayName: '', projectUrlStr: 'https://github.com/icsbariboa/WorldOfGames/'), pipelineTriggers([githubPush()])])
node("prod") {
    stage("Checkout"){
        checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/icsbariboa/WorldOfGames']])
    }
    stage("Build"){
        bat "docker build -t score_server:latest https://github.com/icsbariboa/WorldOfGames.git"
    }
    stage("Run"){
        bat "docker compose up -d"
    }
    stage("Test"){
        def Test_result = bat "python e2e.py"
        if(Test_result.equals(-1)){
            error "The test failed! score is not between 0 to 1000"
        }
    }
    stage("Finalize"){
        bat "docker stop localpipelineforscore-score_server-1"
    }
}