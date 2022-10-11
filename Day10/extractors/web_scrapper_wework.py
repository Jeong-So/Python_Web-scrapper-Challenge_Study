from requests import get
from bs4 import BeautifulSoup

def extract_wwr_jobs(keyword):
  base_url = "https://weworkremotely.com/remote-jobs/search?term="
  
  response = get(f"{base_url}{keyword}")
  if response.status_code != 200:
    print("Can't request website")
  else:
    results = []
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all('section', class_= "jobs")  #find_all 은 list로 반환
    for job_section in jobs:
      job_posts = job_section.find_all('li')
      job_posts.pop()  # li의 마지막 항목 제거
      for post in job_posts:
        anchors = post.find_all('a')
        anchor = anchors[1]
        link = anchor['href']  # bs4는 html을 dictionary 형태로 받음
        company, kind, location = anchor.find_all('span', class_="company")
        title = anchor.find('span', class_='title')  # find는 결과를 가져옴
        # print(f" company name : {company.string}\n what kind of job : {kind.string}\n where is the company : {location.string}\n capability : {title.string}") # .string : 태그제외하고 가져옴
        job_data = {
          'link' : f"https://weworkremotely.com{link}",
          'company' : company.string.replace(","," "),
          'location' : location.string,
          'position' : title.string.replace(","," ")
        }
        results.append(job_data)
    return results
