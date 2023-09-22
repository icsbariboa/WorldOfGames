FROM python:3
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD constants.py /
ADD MainScores.py /
ADD Scores.txt /
CMD ["python3", "./MainScores.py"]