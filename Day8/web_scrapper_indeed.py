from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

## selenium으로 웹 접속하여 크롤링
options = Options()
options.add_argument("--no-sandbox")  # replit에서 selenium 작동을 위한 코드
options.add_argument("--disable-dev-shm-usage") # replit에서 selenium 작동을 위한 코드
  
browser = webdriver.Chrome(options=options)

def get_page_count(keyword):
  ## selenium으로 웹 접속하여 크롤링
  options = Options()
  options.add_argument("--no-sandbox")  # replit에서 selenium 작동을 위한 코드
  options.add_argument("--disable-dev-shm-usage") # replit에서 selenium 작동을 위한 코드
    
  browser = webdriver.Chrome(options=options)
  
  url = "https://kr.indeed.com/jobs?q="
  browser.get(f"{url}{keyword}")
  
  soup = BeautifulSoup(browser.page_source, "html.parser")
  pagination = soup.find("ul", class_="pagination-list")
  if pagination == None:
    return 1
  pages = pagination.find_all("li", recursive = False)
  count = len(pages)
  if count >= 5:
    return 5
  else:
    return count

def extract_indeed_jobs(keyword):
  pages = get_page_count(keyword)
  print("Found", pages, "pages")
  results = []
  for page in range(pages):
    base_url = "https://kr.indeed.com/jobs"
    final_url = f"{base_url}?q={keyword}&start={page*10}"
    print("Requesting", final_url)
    browser.get(final_url)
    
    soup = BeautifulSoup(browser.page_source, "html.parser")
    job_list = soup.find('ul', class_="jobsearch-ResultsList")
    jobs = job_list.find_all('li', recursive=False) # recursive=False : ul 밑에 있는 li 만 찾음
    for job in jobs:
      zone = job.find("div", class_="mosaic-zone")
      if zone == None:
        anchor = job.select_one("h2 a")
        # title = anchor['aria-label']
        title = job.select_one("h2 a span")
        link = anchor['href']
        company = job.find("span", class_="companyName")
        location = job.find("div", class_="companyLocation")
        job_data = {
          'link' : f"https://kr.indeed.com{link}",
          'company' : company.string.replace(","," "),
          'location' : location.string.replace(","," "),
          'position' : title.string.replace(","," ")
        }
        results.append(job_data)
  return results


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