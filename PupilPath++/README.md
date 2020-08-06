# PupilPath++ 
# Author's Comments
    
  It was a major project for me. I haven't done any big projects with GUI interface, so this was definitely challenging. 
  Will be honest, creating just the script without any GUI took me only 2 hours. And although
  adding GUI with Tkinter had given me a hard time because of the bugs I had to face constantly 
  and the time I spent to add all the widgets and pictures(4 days) to make the program look nice and neat, I still enjoyed 
  working on the project and truly got a chance to implement the knowledge I gained from the GUI courses I watched. Also I had to learn how to use python virtual environments in order to make an executable out of my python script via pyinstaller which didn't support my python version. 

# Description
    1) Shows the login window where the user is asked for his login information to PupilPath.com
    2) After the login button is clicked the credentials are being written to a seperate file, 
       credentials.txt and through selenium and webdriver-manager the program logs into the platform
       and downloads the main page containing all the grades. 
    3) After the login is completed successfully the login window is being replaced with the parser window,
       which holds the grades-parser button, gpa-parser button, and done button. 
    4) Grades button will parse the grades from the html file with beautifulsoup and output them to a textbox.
    5) Done button will delete the html file(to always display up-to-date grades) and exit the program.
    6) NEXT TIME.
       When the program is closed through clicking done the user will not have to type the login information again,
       and when he clicks grades the program will see that the html file is gone, 
       thus it will open the browser in a 'headless' mode to download the new html file and output the up-to-date grades to the textbox.
# Usage 
    1) Open and type in your PupilPath login information.
    2) Wait for the program to login.
    3) Click grades and after you are done just click done. 
