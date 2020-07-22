from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from tkinter import *
from PIL.ImageTk import PhotoImage, Image


def gui():
    root = Tk()
    root.title('PupilPath++')

    img = PhotoImage(Image.open('back.png'))
    WIDTH = 800
    HEIGHT = 700

    canvas = Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    frame = Frame(root, bg='#6666ff')
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
    # root.geometry("%dx%d+0+0" % (w, h))
    # background = Label(root, image=img)
    # background.grid(column=0, row=1, columnspan=2)
    # background.image = img
    # parseButton = Button(root, text='Parse grades', padx=20, pady=40)
    # parseButton.grid(column=3, row=3)
    root.mainloop()


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
def parser(html_doc, grade_list):
    with open(html_doc) as html_file:
        soup = BeautifulSoup(html_file, 'html.parser')
        # table = soup.find('tbody')
        grades = soup.find('tbody').find_all('span')
        for grade in grades:
            grade_list.append(float(grade.contents[1].strip()))


def main():
    gui()
    grade_list = []
    user_name = '242306058'
    password = 'Nizor2002'
    # login(user_name, password)
    parser('PupilPath.html', grade_list)
    print('*_*_*_*_*_PUPILPATH GRADES_*_*_*_*_*\n')
    # Lists all the grades in the grades list.
    classes = ['AMER MULT LIT', ]
    for grade in grade_list:
        if grade >= 91:
            print('===============HONORS===============')
            print(grade)
        else:
            print('===============NOT_HONORS===========')
            print(grade)


if __name__ == "__main__":
    main()
