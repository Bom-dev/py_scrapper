from bs4 import BeautifulSoup
import requests


def extract_wwr_jobs(term):
    results = []
    url = f"https://weworkremotely.com/remote-jobs/search?utf8=✓&term={term}"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        jobs = soup.find_all('li', class_='feature')
        for job in jobs:
            position = job.find_all('span', class_='title')
            company = job.find_all('span', class_='company')
            location = job.find_all("span", class_='region company')
            
            job_data = {
                "position": position[0].string.replace(","," "),
                "company": company[0].string.replace(","," "),
                "location": location[0].string.replace(","," ")
            }

            results.append(job_data)

    else:
        print("Can't get jobs.")

    return results
