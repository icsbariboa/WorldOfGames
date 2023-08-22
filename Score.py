import os

score_file_location = "Scores.txt"


def check_if_empty():
    scores_file_data = open("Scores.txt", "a")

    if os.stat(score_file_location).st_size == 0:
        scores_file_data.write("0")
        scores_file_data.close()
    scores_file_data.close()


def read_file_content():
    scores_file_data = open("Scores.txt", "r")
    current_score = scores_file_data.readline()
    scores_file_data.close()

    return int(current_score)


def add_score(difficulty):
    win_points = (difficulty * 3) + 5

    check_if_empty()
    current_points = read_file_content()
    new_score = current_points + win_points

    scores_file_data = open("Scores.txt", "w")
    scores_file_data.write(str(new_score))
    scores_file_data.close()
