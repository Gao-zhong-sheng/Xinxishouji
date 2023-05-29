from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# https://chromedriver.storage.googleapis.com/index.html
chrome_options =Options()
chrome_options.add_experimental_option('--headless')
driver = webdriver.Chrome(options=chrome_options)
url = 'htttps://ww.jd.com/'
driver.get(url)
content = driver.page_source
print(content)