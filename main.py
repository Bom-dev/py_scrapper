from extractors.rok import extract_rok_jobs
from extractors.wwr import extract_wwr_jobs

keyword = input("What do you want to search for?")

rok = extract_rok_jobs(keyword)
wwr = extract_wwr_jobs(keyword)

jobs = rok + wwr

for job in jobs:
    print(job)
    print("/////\n/////")
