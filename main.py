# from requests import get
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from file import save_to_file

# keyword = input("What do you want to search for?")

# rok = extract_rok_jobs(keyword)
# wwr = extract_wwr_jobs(keyword)

# jobs = rok + wwr

# save_to_file(keyword, jobs)

from flask import Flask, render_template, request
from extractors.rok import extract_rok_jobs
from extractors.wwr import extract_wwr_jobs

app = Flask("Scrapper")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/jobs")
def jobs():
    keyword = request.args.get("keyword")
    rok = extract_rok_jobs(keyword)
    wwr = extract_wwr_jobs(keyword)
    jobs = rok + wwr
    return render_template("jobs.html", keyword=keyword, jobs=jobs)


app.run("0.0.0.0")
