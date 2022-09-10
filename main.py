from bs4 import BeautifulSoup
import requests


def extract_jobs(term):
    url = f"https://remoteok.com/remote-{term}-jobs"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        # write your ✨magical✨ code here
        tr = soup.find_all('td', class_="company")
        for t in tr:
            title = t.h2.get_text('h2')
            company = t.h3.get_text('h3')
            print(f"{title} @ {company}")
            print("===============================")
    else:
        print("Can't get jobs.")


extract_jobs(input("Enter your stack:"))
