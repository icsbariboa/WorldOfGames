from flask import Flask, request, render_template

app = Flask("ScoreServer")


@app.route('/Score', methods=['GET', 'POST'])
def score_server():

    if request.method == 'GET':
        score_file = open("Scores.txt")
        current_score = score_file.read()
        score_file.close()
        return render_template("scores_page.html", current_score=current_score)


app.run(host="0.0.0.0", port=5001, debug=False)
