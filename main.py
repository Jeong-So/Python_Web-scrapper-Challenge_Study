from requests import get
from bs4 import BeautifulSoup
from Day8.web_scrapper_study import extract_wwr_jobs  # 만든 패키지 import

jobs = extract_wwr_jobs("python")
print(jobs)