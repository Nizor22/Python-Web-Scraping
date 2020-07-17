from selenium import webdriver
from bs4 import BeautifulSoup
import requests

def login:
    

# Parses the grades from PupilPath.html and adds them to the grades list.
def parser(html_doc, grades):
    with open(html_doc) as html_file:
        soup = BeautifulSoup(html_file, 'html.parser')
        table = soup.find('tbody').find_all('span')
        for grade in table:
            grades.append(float(grade.contents[1].strip()))


def main():
    grades = []
    parser('PupilPath.html', grades)
    print('*_*_*_*_*_PUPILPATH GRADES_*_*_*_*_*\n')
    for grade in grades:
        if grade >= 91:
            print('===============HONORS===============')
            print(grade)
        else:
            print('===============NOT_HONORS===========')
            print(grade)


if __name__ == "__main__":
    main()
