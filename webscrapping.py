from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import json

def wait_for_element(browser, element, by_what):
    return WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located((by_what, element)))

corpus = {}
options = Options()
options.headless = True

if __name__ == '__main__':
    start = 1
    depa = 23
    aggr = 92
    while(1):
        browser = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe", chrome_options=options)
        while(1):
            try:
                browser.get('http://books.deanza.edu/SelectTermDept.aspx')
                s19 = wait_for_element(browser,
                                       '//*[@id="ctl00_ctl00_Content_Content_courseSelect_select_term"]/option',
                                       By.XPATH)
                s19.click()
                break
            except:
                continue

        no_of_book = 9
        no_of_act_book = 0

        try:
            dep = wait_for_element(browser,f'//*[@id="ctl00_ctl00_Content_Content_courseSelect_select_dept"]/option[{depa}]',By.XPATH)
            dep.click()
        except:
            print("Done")
            break

        for j in range(start,no_of_book+start):
            try:
                crs = wait_for_element(browser,f'//*[@id="ctl00_ctl00_Content_Content_courseSelect_select_section"]/option[{j}]',By.XPATH)
                crs.click()
                no_of_act_book += 1
                end = False
            except:
                end = True
                break

        if end:
            depa += 1
            start = 1
        else:
            start += no_of_book

        add_selection = wait_for_element(browser,'//*[@id="ctl00_ctl00_Content_Content_courseSelect_btnAddCourseToList"]',By.XPATH)
        add_selection.click()

        for i in range(3):
            try:
                get_cs = wait_for_element(browser,'//*[@id="ctl00_ctl00_Content_Content_btnGetCourseMaterials"]',By.XPATH)
                get_cs.click()
            except:
                break

        for k in range(no_of_act_book):
            cs1 = wait_for_element(browser,f'//*[@id="ctl00_ctl00_Content_Content_rptCourses_ctrl{k}_lblCourseInfo"]',By.XPATH)
            # print(cs1.text)
            crs = cs1.text[22:44]
            if crs[-1] == 'I':
                crs = crs[:-1]
            corpus[crs] = []
            print(crs)
            i = 0
            while(1):
                try:
                    if i >= 10:
                        title = browser.find_element_by_xpath(f'//*[@id="ctl00_ctl00_Content_Content_rptCourses_ctrl{k}_rptItems_ctl{i}_lblItemTxtTitle"]')
                        csisbn = browser.find_element_by_xpath(f'//*[@id="ctl00_ctl00_Content_Content_rptCourses_ctrl{k}_rptItems_ctl{i}_lblItemTxtISBN"]')
                    else:
                        title = browser.find_element_by_xpath(f'//*[@id="ctl00_ctl00_Content_Content_rptCourses_ctrl{k}_rptItems_ctl0{i}_lblItemTxtTitle"]')
                        csisbn = browser.find_element_by_xpath(f'//*[@id="ctl00_ctl00_Content_Content_rptCourses_ctrl{k}_rptItems_ctl0{i}_lblItemTxtISBN"]')
                    i += 1
                    isbn = csisbn.text
                    title_of_book = title.text
                    print(title.text)
                    print(isbn)
                    corpus[crs].append([isbn,title_of_book])
                except:
                    break

        print("Dumping data")
        a = open(f"DA_Bookstore_Corpus{aggr}.json", 'w')
        json.dump(corpus, a)
        a.close()
        aggr += 1
        browser.close()
