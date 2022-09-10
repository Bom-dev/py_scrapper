from requests import get
from bs4 import BeautifulSoup
from extractors.rok import extract_rok_jobs
from extractors.wwr import extract_wwr_jobs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

keyword = input("What do you want to search for?")

file = open(f"{keyword}.csv", 'w')
file.write("Position,Company,Location\n")

rok = extract_rok_jobs(keyword)
wwr = extract_wwr_jobs(keyword)

jobs = rok + wwr

for job in jobs:
    file.write(
        f"{job['position']}, {job['company']}, {job['location']}\n"
    )

file.close()