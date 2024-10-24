import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


list_of_pro_names = ["Data Engineer", "Machine Learning Engineer",  "Business Intelligence (BI) Developer", "Business Analyst", "Data Modeler",
                     "Quantitative Analyst", "Machine Learning Scientist", "Data Architect", "Data Analyst", "AI specialist", "Data Storyteller", "Data Scientist"]

col_names = ["Job_title", 'Company_name', 'Location', 'Salary_fork', 'Rating', 'Company_Overview', 'Job_description', 'Avg_base_salary']
place = "usa"
with open("parsed_job_data.csv", "a", newline="", encoding="utf8") as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(col_names)
    options = Options()

    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36")


    with webdriver.Chrome(r"D:\chromedriver.exe", chrome_options=options) as wb:


        wb.maximize_window()
        wb.get('https://www.glassdoor.com/member/home/index.htm')
        time.sleep(2)

        wb.find_element(By.ID, 'inlineUserEmail').send_keys("kostinantonii@mail.ru")
        wb.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/form/div[2]/button/span').click()
        time.sleep(3)
        wb.find_element(By.ID, "inlineUserPassword").send_keys('567A123qwe567A')
        time.sleep(3)
        wb.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/form/div[2]/button/span").click()

        time.sleep(15)
        for job_name in list_of_pro_names:
            wb.find_element(By.CSS_SELECTOR, "#sc\.keyword").send_keys(Keys.BACK_SPACE * 50 + job_name)
            time.sleep(3)
            wb.find_element(By.CSS_SELECTOR, '#sc\.location').send_keys(Keys.BACK_SPACE * 30 + place)
            time.sleep(10)
            wb.find_element(By.XPATH, '/html/body/header/nav[1]/div/div/div/div[4]/div[2]/form/div/button').click()
            time.sleep(6)

            time.sleep(5)
            if job_name == "Data Engineer":

                wb.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div[1]/div[3]/a").click()
            time.sleep(5)

            page_amount = int(wb.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/section/article/div[2]/div/div[2]").text.split()[-1])

            for k in range(1, page_amount + 1):

                j = 0
                time.sleep(4)

                while True:
                    j += 1

                    try:
                        wb.find_element(By.XPATH, f'/html/body/div[2]/div/div/div/div/div[2]/section/article/div[1]/ul/li[{j}]/div/div').click()


                    except:
                        break

                    while True:
                        try:
                            wb.find_element(By.CSS_SELECTOR, "#JobDescriptionContainer > div.css-t3xrds.e856ufb4")
                            break
                        except:
                            pass
                    wb.find_element(By.CSS_SELECTOR, "#JobDescriptionContainer > div.css-t3xrds.e856ufb4").click()
                    time.sleep(0.5)

                    Job_title = wb.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[2]').text
                    Company_name = wb.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[1]/div").text.split("\n")[0]
                    Location = wb.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[3]').text
                    try:
                        Salary_fork = wb.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[4]/span").text
                    except:
                        Salary_fork = -1
                    try:
                        wb.find_element(By.CSS_SELECTOR, "#CompanyContainer")
                        Company_Overview = wb.find_element(By.CSS_SELECTOR, "#CompanyContainer").text

                    except:
                        Company_Overview = -1

                    try:
                        Rating = wb.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[1]/div/div/div/div/div[1]/div[1]/div/span").text
                    except:
                        Rating = -1
                    try:
                        wb.find_element(By.XPATH, '//*[@id="JDCol"]//*[@class="salaryTab tabSection p-std"]')
                        Avg_base_salary = wb.find_element(By.XPATH, '//*[@id="JDCol"]//*[@class="salaryTab tabSection p-std"]').text
                    except:
                        Avg_base_salary = -1
                    job_description = " ".join([i.text for i in wb.find_elements(By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[2]/div[1]/div[1]/div/div[1]/div//*")])
                    writer.writerow([Job_title, Company_name, Location, Salary_fork, Rating, Company_Overview, job_description, Avg_base_salary])

                next_page = wb.find_element(By.CSS_SELECTOR, '#MainCol > div.tbl.fill.px.my.d-flex > div > div.pageContainer > button.nextButton.job-search-1iiwzeb.e13qs2072').click()
