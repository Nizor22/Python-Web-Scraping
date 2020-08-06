import os
import threading
import time
# import pkg_resources.py2_warn
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from tkinter import messagebox, ttk
from tkinter import *
from PIL.ImageTk import PhotoImage, Image
from win10toast import ToastNotifier


# Clears out all the unnecessary files and exits the program
def done():
	try:
		os.remove('PupilPath.html')
		sys.exit()
	except FileNotFoundError:
		sys.exit()


# Calculates and outputs the current GPA.
def gpa_parser():
	messagebox.showinfo('COMING SOON', 'The feature will be available in the next update..')


# Prints out the grades from the list to the textbox for user to see.
def output_grades(grade_list):
	honors = []
	not_honors = []
	textbox.delete('1.0', 'end')
	textbox.insert(INSERT, 'PUPILPATH GRADES\n\n')
	for grade in grade_list:
		if grade >= 91:
			honors.append(grade)
		else:
			not_honors.append(grade)

	textbox.insert(INSERT, '===============HONORS===============\n')
	for grade in honors:
		textbox.insert(INSERT, f'{grade}\n')
	textbox.insert(INSERT, '===============NOT HONORS===========\n')
	for grade in not_honors:
		textbox.insert(INSERT, f'{grade}\n')

	textbox.insert(INSERT, '\nEND')


'''Parses the grades from the html file. 
   If the credentials had been saved to auto-login 
   the program will perform a hidden sign_in to show the latest up-to-date grades.
'''
def grade_parser(username, password):
	# Checks if the html file is there
	# (generally after the user is done, he should delete it by clicking done.)
	if not os.path.isfile('PupilPath.html'):
		# if it doesn't exist a hidden sign_in is performed to get a new html file.
		options = webdriver.ChromeOptions()
		options.add_argument('--headless')
		driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
		driver.get('https://pupilpath.skedula.com/')
		time.sleep(1)
		driver.find_element_by_id('sign_in').click()
		driver.find_element_by_id('user_username').send_keys(str(username))
		driver.find_element_by_id('sign_in').click()
		time.sleep(1)
		driver.find_element_by_id('user_password').send_keys(str(password))
		driver.find_element_by_id('sign_in').click()
		time.sleep(1)
		driver.find_element_by_class_name('ui-button-text').click()
		html = driver.page_source
		driver.close()
		with open('PupilPath.html', 'w', encoding='utf-8') as file:
			file.write(html)
	grade_list = []
	# parses the grades from the html file.
	with open('PupilPath.html', 'r') as html_file:
		soup = BeautifulSoup(html_file, 'html.parser')
		# table = soup.find('tbody')
		grades = soup.find('tbody').find_all('span')
		for grade in grades:
			grade_list.append(float(grade.contents[1].strip()))
	output_grades(grade_list)


# Window to display the results of parsing with friendly user interface.
def parser_gui(username, password):
	# Working Frame
	main_frame2 = Frame(root)
	main_frame2.place(relwidth=1, relheight=1)

	# Background
	img = PhotoImage(Image.open(os.path.join(os.getcwd(), r'img\after_login_back.png')))
	background = Label(main_frame2, image=img)
	background.place(relwidth=1, relheight=1)
	background.image = img

	# Button img
	grades_button_img = PhotoImage(Image.open(os.path.join(os.getcwd(), r'img\Grades_button.png')))
	gpa_button_img = PhotoImage(Image.open(os.path.join(os.getcwd(), r'img\GPA_button.png')))
	done_button_img = PhotoImage(Image.open(os.path.join(os.getcwd(), r'img\Done.png')))

	# Buttons
	grades_button = Button(main_frame2, image=grades_button_img, bg='#4a6eb5', bd=0,
	                       command=lambda: grade_parser(username, password))
	grades_button.place(relx=0.15, rely=0.43)
	grades_button.image = grades_button_img

	gpa_button = Button(main_frame2, image=gpa_button_img, bg='#4a6eb5', bd=0, command=gpa_parser)
	gpa_button.place(relx=0.15, rely=0.53)
	gpa_button.image = gpa_button_img

	done_button = Button(main_frame2, image=done_button_img, bg='#4a6eb5', bd=0, command=done)
	done_button.place(relx=0.18, rely=0.68)
	done_button.image = done_button_img
	# Screen for output
	# noinspection PyGlobalUndefined
	global textbox
	textbox = Text(main_frame2, font=('Arial', 9, 'bold'), fg='#1a1a1a', bg='#f2f2f2')
	textbox.insert(INSERT, '\n When you are done with the program\n please press done before closing.')
	textbox.place(relx=0.48, rely=0.43, relwidth=0.4, relheight=0.35)


# saves login info so that next time the login_gui() won't be called.
def save_credentials(username, password):
	with open('credentials.txt', 'w') as f:
		f.write(f'{username}:{password}')


# Logs into the PupilPath account and downloads the html content.
def sign_in(username, password):
	# noinspection PyGlobalUndefined
	global driver
	notifier = ToastNotifier()
	notifier.show_toast('Please wait', 'Attempting a login..', duration=5,
	                    icon_path=os.path.join(os.getcwd(), r'img\icon.ico'))
	try:
		options = webdriver.ChromeOptions()
		options.add_argument('--incognito')
		driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
		driver.set_page_load_timeout(20)
		driver.get('https://pupilpath.skedula.com/')
		time.sleep(1)
		driver.find_element_by_id('sign_in').click()
		driver.find_element_by_id('user_username').send_keys(str(username))
		driver.find_element_by_id('sign_in').click()
		time.sleep(1)
		driver.find_element_by_id('user_password').send_keys(str(password))
		driver.find_element_by_id('sign_in').click()
		time.sleep(1)
		driver.find_element_by_class_name('ui-button-text').click()
		html = driver.page_source
		driver.close()
		with open('PupilPath.html', 'w', encoding='utf-8') as file:
			file.write(html)
	except TimeoutError:
		driver.execute_script("window.stop();")
	except UnicodeEncodeError:
		notifier.show_toast('Error', 'Delete PupilPath.html and restart the app', duration=10,
		                    icon_path=os.path.join(os.getcwd(), r'img\icon.ico'))


# Creates and starts threads for save_credentials and sign_in function.
def login(username, password):
	if checkbox.instate(['selected']):
		t1 = threading.Thread(target=save_credentials, args=(username.get(), password.get()))
		t1.start()
		t2 = threading.Thread(target=sign_in, args=(username.get(), password.get()))
		t2.start()
		t2.join()
	else:
		sign_in(username.get(), password.get())
	main_frame.destroy()
	parser_gui(username, password)


# The window that will take the input of the user's pupilpath information.
def login_gui():
	# Working Frame
	# noinspection PyGlobalUndefined
	global main_frame
	main_frame = ttk.Frame(root)
	main_frame.place(relwidth=1, relheight=1)

	# Background
	img = PhotoImage(Image.open(os.path.join(os.getcwd(), r'img\back.png')))
	background = Label(main_frame, image=img)
	background.place(relwidth=1, relheight=1)
	background.image = img

	# text fields for getting data
	username_entry = ttk.Entry(main_frame)
	username_entry.place(relx=0.4, rely=0.4899, relwidth=0.4, relheight=0.045)

	password_entry = ttk.Entry(main_frame, show='*')
	password_entry.place(relx=0.4, rely=0.5799, relwidth=0.4, relheight=0.045)

	# save password checkbox
	# noinspection PyGlobalUndefined
	global checkbox
	checkbox = ttk.Checkbutton(main_frame, text='Save password?')
	checkbox.state(['!alternate'])
	checkbox.place(relx=0.45, rely=0.6799, relheight=0.049)
	# button to login
	login_button = Button(main_frame, text='login', command=lambda: login(username_entry, password_entry))
	login_button.place(relx=0.65, rely=0.6799, relwidth=0.2, relheight=0.05)


# Stores the root and the canvas for the program
def main():
	# noinspection PyGlobalUndefined
	global root
	# noinspection PyGlobalUndefined
	global canvas

	root = Tk()
	root.title('PupilPath++')
	root.resizable(False, False)
	icon = PhotoImage(file='./img/icon medium.ico')
	root.tk.call('wm', 'iconphoto', root._w, icon)

	canvas = Canvas(root, width=700, height=500)
	canvas.pack()

	# If the credentials were not saved show the login form.
	if not os.path.isfile('credentials.txt'):
		login_gui()
	# Otherwise call the parser_gui with the saved credentials.
	else:
		with open('credentials.txt', 'r') as f:
			line = f.readline().strip('\n')
			username = line.split(':')[0].strip('')
			password = line.split(':')[1].strip('')
		parser_gui(username, password)

	root.mainloop()


if __name__ == '__main__':
	main()
