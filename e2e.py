from selenium import webdriver
from constants import ipaddress_score_server, port_score_server
from selenium.webdriver.chrome.service import Service

service = Service()
options = webdriver.ChromeOptions()


def test_scores_service(app_url):
    driver1 = webdriver.Chrome(service=service, options=options)
    driver1.get(app_url)
    score = driver1.find_element("id", "score")
    return 0 <= int(score.text) <= 1000


def main_test():
    if test_scores_service(f"http://{ipaddress_score_server}:{port_score_server}/score"):
        return 0
    return -1


if __name__ == "__main__":
    main_test()
