import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from tkinter import *
from PIL.ImageTk import PhotoImage, Image
import time


def parser(username, password):
    login(username, password)
    with open('PupilPath.html', 'r') as html_file:
        soup = BeautifulSoup(html_file, 'html.parser')
        # table = soup.find('tbody')
        grades = soup.find('tbody').find_all('span')
        for grade in grades:
            grade_list.append(float(grade.contents[1].strip()))
    counter = 0
    textbox.insert(INSERT, '*_*_*_*_*_PUPILPATH GRADES_*_*_*_*_*\n\n')
    for grade in grade_list:
        if grade >= 91:
            textbox.insert(INSERT, '===============HONORS===============\n')
            textbox.insert(INSERT, f'{grade}\n')
        else:
            textbox.insert(INSERT, '===============NOT HONORS===========\n')
            textbox.insert(INSERT, f'{grade}\n')
    textbox.insert(INSERT, '\nEND')


def parser_gui(username, password):
    # Title Frame
    title_frame = Frame(root, bg='#4da6ff', bd=5)
    title_frame.place(relx=0, rely=0, relwidth=1, relheight=0.2)

    title_label = Label(title_frame, text='PUPILPATH++', font=('Ariel', 20, 'bold'), fg='WHITE', bg='#d9b3ff')
    title_label.place(relx=0.01, rely=0.05, relwidth=0.99, relheight=0.95, anchor='nw')

    # Working Frame
    main_frame2 = Frame(root, bg='#6666ff')
    main_frame2.place(relx=0.0, rely=0.2, relwidth=1, relheight=1)

    welcome = Label(main_frame2, text='Welcome to PupilPath++', font=('Ariel', 20))
    instruction = Label(main_frame2, text='To get your grades just click the button', font=('Ariel', 8))

    welcome.place(relx=0.21, rely=0.03)
    instruction.place(relx=0.21, rely=0.15)
    button = Button(main_frame2, text='Parse Grades', highlightbackground='blue', command=lambda: parser(username, password))
    button.place(relx=0.7, rely=0.15)
    global textbox
    textbox = Text(main_frame2, font=('Ariel', 12, 'bold'), fg='red', bg='black', )
    textbox.place(relx=0.050, rely=0.3, relwidth=0.9, relheight=0.45)


# saves login info to a separate file from which it will read next time.
def save_credentials(username, password):
    with open('credentials.txt', 'w') as f:
        f.write(f'{username}:{password}')


def login(username, password, checkbox=0):
    print(username)
    if checkbox:
        save_credentials(username.get(), password.get())
    # Logs in
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://pupilpath.skedula.com/')
    time.sleep(1)
    driver.find_element_by_id('sign_in').click()
    driver.find_element_by_id('user_username').send_keys(username)
    driver.find_element_by_id('sign_in').click()
    time.sleep(1)
    driver.find_element_by_id('user_password').send_keys(password)
    driver.find_element_by_id('sign_in').click()
    time.sleep(1)
    driver.find_element_by_class_name('ui-button-text').click()
    with open('PupilPath.html', 'w') as file:
        file.write(driver.page_source)
    driver.close()
    if not os.path.isfile('credentials.txt'):
        main_frame.destroy()
    parser_gui(username, password)


def login_gui():
    # Title Frame
    title_frame = Frame(root, bg='#4da6ff', bd=5)
    title_frame.place(relx=0, rely=0, relwidth=1, relheight=0.2)

    label = Label(title_frame, text='PUPILPATH++', font=('Ariel', 20, 'bold'), fg='WHITE', bg='#d9b3ff')
    label.place(relx=0.01, rely=0.05, relwidth=0.99, relheight=0.95, anchor='nw')

    # Working Frame
    global main_frame

    main_frame = Frame(root, bg='#6666ff')
    main_frame.place(relx=0.0, rely=0.2, relwidth=1, relheight=1)

    # labels for text fields
    username_label = Label(main_frame, text='Username', fg='blue')
    password_label = Label(main_frame, text='Password', fg='blue')

    username_label.place(relx=0.21, rely=0.03, relheight=0.05)
    password_label.place(relx=0.21, rely=0.1, relwidth=0.131, relheight=0.05)

    # text fields for getting data
    username = StringVar()
    username_entry = Entry(main_frame, textvariable=username)
    username_entry.place(relx=0.4, rely=0.03, relwidth=0.7, relheight=0.05)

    password = StringVar()
    password_entry = Entry(main_frame, textvariable=password)
    password_entry.place(relx=0.4, rely=0.1, relwidth=0.55, relheight=0.05)

    # save password checkbox
    value = IntVar()
    checkbox = Checkbutton(main_frame, text='Save password?', variable=value)
    checkbox.place(relx=0.45, rely=0.2, relheight=0.049)
    print(value.get())
    # button to login
    login_button = Button(main_frame, text='login', command=lambda: login(username, password, value))
    login_button.place(relx=0.7, rely=0.2, relwidth=0.2, relheight=0.05)


def main():
    global root, canvas, grade_list

    grade_list = []
    root = Tk()
    root.title('PupilPath++')
    canvas = Canvas(root, width=500, height=400)
    canvas.pack()

    if not os.path.isfile('credentials.txt'):
        login_gui()
    else:
        with open('credentials.txt', 'r') as f:
            line = f.readline().strip('\n')
            username = line.split(':')[0]
            password = line.split(':')[1]
        parser_gui(username, password)

    root.mainloop()


if __name__ == '__main__':
    main()
