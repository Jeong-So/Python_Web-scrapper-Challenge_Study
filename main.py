from Day8.web_scrapper_study import extract_wwr_jobs  # 만든 패키지 import
from Day8.web_scrapper_indeed import extract_indeed_jobs  # 만든 패키지 import


keyword = input("What do you want to search for?")

indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)
jobs = indeed + wwr

file = open(f"{keyword}.csv", "w")
file.write("Position,Company,Location,URL\n")

for job in jobs:
  file.write(f"{job['position']},{job['company']},{job['location']},{job['link']}\n")

file.close()

"""
indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)

jobs = indeed + wwr

for job in jobs:
  print(job)
  print("//////////////\n//////////////")
  """