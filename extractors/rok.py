from bs4 import BeautifulSoup
import requests


def extract_rok_jobs(term):
    url = f"https://remoteok.com/remote-{term}-jobs"
    results = []
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        tr_jobs = soup.find_all("tr", class_='job')
        for tr_job in tr_jobs:
            position = tr_job.find_all(attrs={'itemprop': 'title'})
            company = tr_job.find_all(attrs={'itemprop': 'name'})
            location = tr_job.find_all("div", class_='location')

            job_data = {
                "position": position[0].string.replace(","," "),
                "company": company[0].string.replace(","," "),
                "location": location[0].string.replace(","," ")
            }

            results.append(job_data)

    else:
        print("Can't get jobs.")

    return results
