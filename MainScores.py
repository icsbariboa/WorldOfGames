from flask import Flask, request, render_template
from constants import ipaddress_score_server, port_score_server

app = Flask("ScoreServer")


@app.route('/score', methods=['GET', 'POST'])
def score_server():
    if request.method == 'GET':
        score_file = open("Scores.txt")
        current_score = score_file.read()
        score_file.close()
        return render_template("scores_page.html", current_score=current_score)


app.run(host=ipaddress_score_server, port=port_score_server, debug=False)
