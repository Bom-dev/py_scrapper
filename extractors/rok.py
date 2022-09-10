from bs4 import BeautifulSoup
import requests


def extract_rok_jobs(term):
    url = f"https://remoteok.com/remote-{term}-jobs"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        tr_jobs = soup.find_all("tr", class_='job')
        for tr_job in tr_jobs:
            title = tr_job.find_all(attrs={'itemprop': 'title'})
            company = tr_job.find_all(attrs={'itemprop': 'name'})
            each_location = tr_job.find_all("div", class_='location')
            print(
                f"Job: {title[0].string} @ {company[0].string}")
            if len(each_location) == 1:
                print(each_location[0].string)
            elif len(each_location) == 2:
                for n in each_location:
                    print(n.string)
            elif len(each_location) == 3:
                for n in each_location:
                    print(n.string)
            print("==========================================")

    else:
        print("Can't get jobs.")


extract_rok_jobs(input("Enter your stack:"))
