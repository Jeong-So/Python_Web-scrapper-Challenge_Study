from flask import Flask, render_template, request
from extractors.web_scrapper_remoteok import extract_rmo_jobs
from extractors.web_scrapper_wework import extract_wwr_jobs

app = Flask("JobScrapper")

@app.route("/")
def home():
  return render_template("home.html")

db = {}

@app.route("/search")
def search():
  keyword = request.args.get("keyword")
  if keyword in db:
    jobs = db[keyword]
  else:
    rmo = extract_rmo_jobs(keyword)
    wwr = extract_wwr_jobs(keyword)
    jobs = rmo + wwr
    db[keyword] = jobs
  return render_template("search.html", keyword = keyword, jobs = jobs)

app.run("0.0.0.0")

## 연습용
## Day10 과제로 만들었으나 Day10이라는 폴더안에서 만들어서 동작 안함 --> repl새로 다시 만듬
