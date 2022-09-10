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
            title = job.find_all('span', class_='title')
            company = job.find_all('span', class_='company')
            location = job.find_all("span", class_='region company')
            link = job.find_all('a')
            # if len(title) == 1:
            #     print(f"Job: {title[0].string} @ {company[0].string}")
            # if len(each_location) == 1:
            #     print(each_location[0].string)
            # print("==========================================")
            job_data = {
                'link': f"https://weworkremotely.com/remote-jobs/{link}",
                'title': title[0].string,
                'company': company[0].string,
                'location': location[0].string
            }

            results.append(job_data)

    else:
        print("Can't get jobs.")

    return results
