from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
search_url = "https://itdashboard.gov"
driver.get(search_url)
driver.page_source
#driver.find_element(By.LINK_TEXT, "DIVE IN").click()
driver.execute_script("window.scrollTo(0, 900)")
time.sleep(10)

elements = driver.find_elements(By.TAG_NAME, 'a')
ls = []
for e in elements:
  if "\n" in e.text:
    ls.append(e.text)
nls=[]
for el in ls:
  nls.append(el.replace("\n", " ").replace("Total FY2021", "  ").replace("Spending:", "   ").strip())
fd = [[],[]]
for i in nls:
  fd[0].append(i[-6:])
  fd[1].append(i[0:-6])
fd[0].pop(0)
fd[1].pop(0)
df = pd.DataFrame(fd).T
df.to_excel(excel_writer = "data.xlsx")
driver.quit()
