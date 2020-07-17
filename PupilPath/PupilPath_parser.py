from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from tkinter import *


# Logs into PupilPath and saves the page PupilPath.html
def login(user_name, password):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://pupilpath.skedula.com/')
    driver.find_element_by_id('sign_in').click()
    driver.find_element_by_id('user_username').send_keys(user_name)
    driver.find_element_by_id('sign_in').click()
    driver.find_element_by_id('user_password').send_keys(password)
    driver.find_element_by_id('sign_in').click()
    driver.find_element_by_class_name('ui-button-text').click()
    with open('PupilPath.html', 'w') as file:
        file.write(driver.page_source)


# Parses the grades from PupilPath.html and adds them to the grades list.
def parser(html_doc, grades):
    with open(html_doc) as html_file:
        soup = BeautifulSoup(html_file, 'html.parser')
        table = soup.find('tbody').find_all('span')
        for grade in table:
            grades.append(float(grade.contents[1].strip()))


def main():
    grades = []
    user_name = '242306058'
    password = 'Nizor2002'
    login(user_name, password)
    parser('PupilPath.html', grades)
    print('*_*_*_*_*_PUPILPATH GRADES_*_*_*_*_*\n')
    # Lists all the grades in the grades list.
    for grade in grades:
        if grade >= 91:
            print('===============HONORS===============')
            print(grade)
        else:
            print('===============NOT_HONORS===========')
            print(grade)


if __name__ == "__main__":
    main()
