from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui as pg
import time

time.sleep(3)
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://accounts.google.com/signin/oauth/identifier?access_type=offline&client_id=787721145689-0jd34d5js4su4utt48csfvokvp0dcmp9.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fedhesive.com%2Fauth%2Fgoogle_oauth2%2Fcallback&response_type=code&scope=email%20profile&state=96ee3fe838d7607be6baf1e9790bb4f0209c1bd807f6ec64&o2v=1&as=23jWWieIo6g26jAU7BOO5g&flowName=GeneralOAuthFlow')
driver.find_element_by_id("identifierId").send_keys('nfarukhzoda6058@ermurrowhs.org')
pg.write('\n')
time.sleep(7)
driver.find_element_by_name("password").send_keys('242306058')
pg.write('\n')
time.sleep(4)
pg.scroll(-200)
time.sleep(0.5)
driver.find_element_by_class_name('ic-avatar ').click()
pg.click(781, 976)
time.sleep(0.5)
pg.drag(727, 848)
time.sleep(0.5)
pg.scroll(-200)
while True:
	print(pg.position())