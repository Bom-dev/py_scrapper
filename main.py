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

from flask import Flask, render_template, request, redirect, send_file
from extractors.rok import extract_rok_jobs
from extractors.wwr import extract_wwr_jobs
from file import save_to_file

app = Flask("Scrapper")

db = {}


@app.route("/")
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run()


@app.route("/jobs")
def jobs():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else:
        rok = extract_rok_jobs(keyword)
        wwr = extract_wwr_jobs(keyword)
        jobs = rok + wwr
        db[keyword] = jobs
    return render_template("jobs.html", keyword=keyword, jobs=jobs)


@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword, db[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True)