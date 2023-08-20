from flask import Flask, request

app = Flask("ScoreServer")


@app.route('/Score', methods=['GET', 'POST'])
def score_server():
    if request.method == 'GET':
        score_file = open("Scores.txt")
        current_score = score_file.read()
        return f"<html><head><title>Scores Game</title></head><body><h1>The score is: <div id='score'>{current_score}</div></h1></body></html>"


app.run(host="0.0.0.0", port=5001, debug=False)
