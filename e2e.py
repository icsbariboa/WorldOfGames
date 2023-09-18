from selenium import webdriver


def test_scores_service(app_url):
    driver1 = webdriver.Chrome()
    driver1.get(app_url)
    score = driver1.find_element("id", "score")
    return 0 <= int(score.text) <= 1000


def main_test():
    if test_scores_service("http://localhost:5001/Score"):
        return 0
    return -1


if __name__ == "__main__":
    print(main_test())
