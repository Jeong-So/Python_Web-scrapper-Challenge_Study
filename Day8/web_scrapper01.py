from bs4 import BeautifulSoup
import requests

def extract_jobs(term):
  url = f"https://remoteok.com/remote-{term}-jobs"
  request = requests.get(url, headers={"User-Agent": "Kimchi"})
  results = []
  
  if request.status_code == 200:
    soup = BeautifulSoup(request.text, "html.parser")
    # write your ✨magical✨ code here
    jobs = soup.find_all('td', class_="company position company_and_position")
    jobs.pop(0)
    for job in jobs:
      links = job.find('a')
      link = links['href']
      job_position = links.find('h2')
      # print(job_position.string)
      company_name = job.find('h3')
      # print(company_name.string)
      details = job.find_all('div', class_="location")
      location = details[0]
      price = details[1]
      job_data = {
        'link' : f"https://remoteok.com{link}",
        'company name' : company_name.string.strip('\n'),
        'job position' : job_position.string.strip('\n'),
        'location' : location.string,
        'pay' : price.string
      }
      # print(job_data)
      # print()
      results.append(job_data)
    for result in results:
      print(result)
      print()
  else:
    print("Can't get jobs.")

extract_jobs("rust")