from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Day8.web_scrapper_study import extract_wwr_jobs  # 만든 패키지 import

## Day8.web_scrapper_study 안의 extract_wwr_jobs 함수 사용
# jobs = extract_wwr_jobs("python")
# print(jobs)

## selenium으로 웹 접속하여 크롤링
options = Options()
options.add_argument("--no-sandbox")  # replit에서 selenium 작동을 위한 코드
options.add_argument("--disable-dev-shm-usage") # replit에서 selenium 작동을 위한 코드

browser = webdriver.Chrome(options=options)

browser.get("https://kr.indeed.com/jobs?q=python&limit=50")

soup = BeautifulSoup(browser.page_source, "html.parser")
job_list = soup.find('ul', class_="jobsearch-ResultsList")
jobs = job_list.find_all('li', recursive=False) # recursive=False : ul 밑에 있는 li 만 찾음
print(len(jobs))

"""
# https://kr.indeed.com/ 사이트가 크롤링 거부 --> selenium으로 브라우저 직접 작동
base_url = "https://kr.indeed.com/jobs?q="
search_term = "python"
headers = { 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',}

response = get(f"{base_url}{search_term}", headers=headers)
if response.status_code >= 400:
  print("Can't request page")
  print(response.status_code)
else:
  soup = BeautifulSoup(response.text, "html.parser")
  job_list = soup.find('ul', class_="jobsearch-ResultsList")
  jobs = job_list.find_all('li', recursive=False) # recursive=False : ul 밑에 있는 li 만 찾음
  print(len(jobs))
  """