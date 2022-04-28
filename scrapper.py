"""
--- Introduction ---

This module is responsible for liking the comments Blow
the post accounts are collected from the user's following.
This app is a scrapper to do some things on the Instagram website.

--- How does the program work? --- 

This app will receive your Instagram account username and password.
Then it enters your account for the first time and receives and saves
the list of all your followings and then leaves your account.

It will then login to your account again and receive the last 24 hours
of posts from each user (your followings). It then checks to see if the
comment is below the posts and then it likes all the comments below the
post by your account. 
It does this enough to like all the comments below the received posts.
After finishing the work, it rests for 15 minutes and then activates automatically.
It then checks again to see if there is a new post and if there is a comment
below the posts, It likes them. Also, if a new comment is placed below previous posts,
it recognizes them and likes them again. 
Note: Every post whose comments are liked, the post itself is liked


--- Abilities ---

This program is tested only on Windows operating system and works completely and without bugs, on Windows operating system.
so if you are Linux or Mac, etc., please customize the source code.
In future updates, I promise to synchronize the program with other operating systems.

- Displays all your logs in a cmd window in Windows
- If you wish, you can see all the steps and operation of the robot in a browser
- The program performs its activities completely automatically, and after finishing its work, it rests for 15 minutes and then restarts
- After each restart, it will check your recent 24 hour posts and all followins, and if it sees anything new, it will perform the desired operations
- Receives all comments below each post
- Every post whose comments are liked, the post itself is liked
- Various methods are designed for the robot to function properly and your account not to be blocked. So the program works completely and automatically and there is no problem for your Instagram accounts
- If you have a specific idea or option, let me know by email so I can add them to the robot
- Updates are provided to the app on an ongoing basis



--- Introducing the tool ---

This program is provided in the form of Python source code, and in this section we will introduce
the folders and tools available in the program.
The first folder is plugin, Where the webdriver of the browser is located (to run programs and scraper, we need this software).
In this program, we use Firefox as a browser for scraping. So you need to download the latest version of Firefox and WebDriver from the following links:

{Firefox download link: https://www.mozilla.org/en-US/firefox/download/thanks/}
{Webdriver download link: https://github.com/mozilla/geckodriver/releases}

Install Firefox from the link above and download the 'geckodriver-[xxxx]-win[xx].zip' file from the second link and place it in the plugin folder.
The next folder is the software, where we usually put the software needed in the Windows operating system so that you can install them if needed.


--- Prerequisites ---

This program is written with Python 3.9 but supports Python 3 and all versions.
The required modules of this program are located in the 'prerequisites' file in the plugin folder, and you can install the required modules with the following command:

{python -m pip install --upgrade pip}
{python -m pip install -r plugin\\prerequisites.txt}

In this program, we use Firefox as a browser for scraping. So you need to download the latest version of Firefox and WebDriver from the following links:

{Firefox download link: https://www.mozilla.org/en-US/firefox/download/thanks/}
{Webdriver download link: https://github.com/mozilla/geckodriver/releases}

Install Firefox from the link above and download the 'geckodriver-[xxxx]-win[xx].zip' file from the second link and place it in the plugin folder.


--- About the author ---

This program was written by a young Iranian and this person tries to keep his GitHub programs always up to date.
If would you like to contact me, you can send a message to my personal email:

{mohammadmahyarkermani@gmail.com}

You can also see my resume at the following link:

{}


--- Report bugs ---

Since this program is written as a scraper and with a small change on Instagram,it may crash,
Please if you have any problems with how the program runs and works, please publish your error in the issue section of GitHub
or send it to my email to fix the bugs of the program as soon as possible. Thank you for your cooperation :)

"""

# Import modules
# Get information from targets
from instaloader import Instaloader, Profile
# Perform the operation
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
# Display mode
import time, datetime, os
from colorama import init, Style, Fore
from platform import system


def show_log(message:str, status:str="notif"):
    """This function displays various reports in a window that opens in the application.
    - Parameters:
        - message: str
            - The report that each function sends of its performance.
        - status: str
            - Message sending status (notif, success or error, default: notif)."""

    try:
        # Identify message status and display output
        init() # Show color correct
        # If msg notif mode
        if status.lower() == "notif":
            print (Style.BRIGHT + Fore.BLUE + "[*] " + Style.BRIGHT + Fore.YELLOW + message + Style.RESET_ALL + Fore.RESET)

        # If msg success mode
        elif status.lower() == "success":
            print (Style.BRIGHT + Fore.BLUE + "[+] " + Style.BRIGHT + Fore.GREEN + message + Style.RESET_ALL + Fore.RESET)

        # If msg error mode
        elif status.lower() == "error":
            print (Style.BRIGHT + Fore.BLUE + "[!] " + Style.BRIGHT + Fore.RED + message + Style.RESET_ALL + Fore.RESET)

        # If the message status was unknown 
        else:
            print ("[-] " + message)
    
    # If there is an error in displaying the colored text
    except:
        print ("""[!] There are problems displaying colors.
                Please report your error via email to the developer to resolve this issue:
                    Developer Email: mohammadmahyarkermani@gmail.com\n""")
        print ("[*] " + message)

def clear_screen():
    """This module is responsible for cleaning the screen and logs"""

    try:
        # If platform and os was Windows
        if system().lower() == "windows":
            os.system("cls")
    except:
        show_log ("There was a problem cleaning the screen.", status="error")

def config_files():
    """This function sets various variables for the performance of other functions.
    Asks various questions from the user to configure files."""

    try:
        # Global and sets the required variables for use other functions
        global path_following_file, path_geckodriver, website_insta_addr, \
        input_username, input_password, button_submit,\
        option_notnow, button_accept_cookies, load_more_comments,\
        like, graphical_mode, _username, _password


        # In this section, a set of variables is set for the activity of other functions.
        # 
        path_following_file = os.path.abspath("plugin\\following.txt")
        path_geckodriver = os.path.abspath("plugin\geckodriver.exe")
        website_insta_addr = "https://www.instagram.com/"

        input_username = "input[name='username']"
        input_password = "input[name='password']"

        button_submit = "button[type='submit']"

        option_notnow = "//button[contains(text(), 'Not Now')]"

        button_accept_cookies = "//button[contains(text(), 'Allow essential and optional cookies')]"

        load_more_comments = "svg[aria-label='Load more comments']"

        like = 'svg[aria-label="Like"][color="#262626"]'
        #


        # In this section, Asks various questions from the user to configure files
        #
        print (Style.BRIGHT + Fore.WHITE) # Set colors
        _username = input("[!] What is the username of your Instagram account: ")
        _password = input("[!] What is the password of your Instagram account: ")
        graphical_mode = input("[!] Do you want to see the browser window of all the steps (y/n)? ").lower()
        print (Style.RESET_ALL + Fore.RESET)
        
        # Checks if the user has just entered the yes or no value
        while True:
            if graphical_mode != "yes" and graphical_mode != "y" and graphical_mode != "no" and graphical_mode != "n":
                graphical_mode = input("Do you want to see the browser window of all the steps? y/n").lower()
            else:
                break
        #


        # Clear display screen and display a log
        clear_screen()
        show_log("Files were configured successfully.")
    
    # If an error occurs during the program
    except:
        # Display log
        show_log("""There is a problem with the configuration files. 
            - Please check the config file in the plugin folder or
            - Please report your error via email to the developer to resolve this issue:
                Developer Email: mohammadmahyarkermani@gmail.com\n""", status="error")

def info_connect_to_account():
    """Connect and login to the account for gather information from targets"""

    try:
        global payload, account # Global some variables to use other functions
        payload = Instaloader() # Create payload for get options
        payload.login(_username, _password) # Login to your account
        account = Profile.from_username(payload.context, _username) # Get account details
        show_log("The app was successfully logged into your account to collect information.") # Display a log
    
    # If an error occurs during the program
    except:
        show_log("""There was a problem logging to Instagram account. Please check the following:
            - Check your username and password in the config file in the plugin folder
            - Setup another account in the config file and try again with another account
            - Check your anti filter and internet
            - Your account must not have two-step verification
            - Your Instagram account should not be restricted or reported
            - Reinstall the Firefox file
            - Make sure the 'geckodriver.exe' file is in the plugin folder
            - or Please report your error via email to the developer to resolve this issue:
                    Developer Email: mohammadmahyarkermani@gmail.com\n""", status="error")

def info_save_following():
    """get and save user's following"""

    try:
        # save following list in a file
        with open(path_following_file, "w") as wf:
            for following in account.get_followees():
                wf.write(following.username + "\n")

            wf.close()

        show_log("Your following list was successfully collected.")
    
    # If an error occurs during the program
    except:
        show_log("""There was a problem saving the following list. Please check the following:
            - Restart the app
            - Use another account
            - Please report your error via email to the developer to resolve this issue:
                Developer Email: mohammadmahyarkermani@gmail.com\n""", status="error")

def info_save_post():
    """The link receives the posts of the last 24 hours each user"""

    try:
        # Global some variables for use other functions
        global following, count

        # Calculate current time
        today_time = datetime.datetime.utcnow()
        today_month = today_time.month
        today_day = today_time.day

        # Read the following list for other operations
        with open(path_following_file, "r") as rf:
            list_following = rf.read().strip().split("\n")
            rf.close()
        
        # In this section, it checks the account of each user and,
        # If there is a post in the last 24 hours, it receives the link and sends it to the operating_do_like function
        for following in list_following:
            # Get each user's account details
            user = Profile.from_username(payload.context, following)
            count = 0

            # Get all posts from each user
            # And check if the post has been published in the last 24 hours or not?
            for post in user.get_posts():
                
                # Calculate and find valid date (last 24 hours)
                post_time = post.date_utc
                post_time_month = post_time.month
                post_time_day = post_time.day

                result_time_month = today_month - post_time_month
                result_time_day = today_day - post_time_day

                # Quickly check that if the post is more than 2 days old, go to the next post
                if result_time_day >= 2:
                    break

                # If the post was published less than 24 hours ago
                if result_time_month == 0 and result_time_day == 1 or result_time_day == 0:
                    
                    # if comments was enable and exist
                    if post.comments != 0:

                        # Send post link to operating_do_like function for do the operation of liking comments
                        # Calculate the number of submitted links and display the log
                        operating_do_like("https://www.instagram.com/p/" + post.shortcode + "/")
                        count += 1
                        show_log(f"Post {count} from {following} user was completed successfully.")
           
    # If an error occurs during the program
    except:
        show_log("""There was a problem saving valid posts. Please check the following:
            - Restart the app
            - Use another account
            - Please report your error via email to the developer to resolve this issue:
                    Developer Email: mohammadmahyarkermani@gmail.com\n""", status="error")

def operating_connect_to_account():
    """Connect and login to the account for perform the operation of liking comments"""

    try:
        # Use firefox browser to connect the instagram website
        # Global some variables
        global driver

        # Set some options for browser
        options_browser = Options()
        options_browser.add_argument("--no-sandbox")
        options_browser.add_argument("--disable-crash-reporter")
        options_browser.add_argument("--disable-extensions")
        options_browser.add_argument("--disable-logging")
        options_browser.add_argument("--log-level=3")

        # If selected by the user, the browser display window will not be displayed
        # Otherwise, if the user agrees, a browser window will open graphically and show the robot steps and process in an instant
        if graphical_mode == "no" or graphical_mode == "n":
                options_browser.add_argument("--headless")

        # Load driver, firefox and Instagram website for browser scraper
        load_driver = Service(path_geckodriver)
        driver = webdriver.Firefox(service=load_driver, options=options_browser)
        
        # Delete cookies of current browser, maximize the window and load instagram web
        driver.delete_all_cookies()
        driver.maximize_window()
        driver.get(website_insta_addr)

        # If this option to accept cookies appeared on the page
        try:
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, button_accept_cookies))).click()
            time.sleep(5)
        except:
            pass

        # Find username and password label
        username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, input_username)))
        password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, input_password)))

        # Clear the username and password label
        # Write username and password account to labels
        username.clear()
        username.send_keys(_username)

        password.clear()
        password.send_keys(_password)

        # Find and click to button submit for login to account
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, button_submit))).click()

        # Ignore pop-up and other window in operating
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, option_notnow))).click()
            time.sleep(3)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, option_notnow))).click()
        except:
            pass

        show_log("The app successfully logged into your Instagram account.")
        show_log("In a few moments, the operation of liking the comments will start.")
    
    # If an error occurs during the program
    except:
        show_log("""There was a problem logging to Instagram account. Please check the following:
            - Check your username and password in the config file in the plugin folder
            - Setup another account in the config file and try again with another account
            - Check your anti filter and internet
            - Your account must not have two-step verification
            - Your Instagram account should not be restricted or reported
            - Reinstall the Firefox file
            - Make sure the 'geckodriver.exe' file is in the plugin folder
            - or Please report your error via email to the developer to resolve this issue:
                    * Developer Email: mohammadmahyarkermani@gmail.com\n""", status="error")

def operating_do_like(_link:str):
    """Find the comments below each post and like them
    - Parameters:
        - link: str
            - link each valid post"""
        
    try:
    
        # Load and operating on any link for liking comments
        driver.get(_link)
        time.sleep(5)
        
        # If the number of comments below a post is high, Instagram only displays the first few comments,
        # and the user must click on a specific option to load more comments
        # This section loads all the comments below a post
        try:
            while True:
                driver.find_element(by=By.CSS_SELECTOR, value=load_more_comments).click()
                time.sleep(5)
        except:
            pass

        # This section receives a list of all comments below a post
        list_comments = list(driver.find_elements(by=By.CSS_SELECTOR, value=like))
        _count = 0
        
        # Reviews and likes every comment
        for comment in list_comments:
            try:
                # Likes a comment every 3 seconds
                # Calculate the number of likes and display the log
                comment.click()

                _count += 1
                show_log(f"{_count} comment from post {count} was liked in {following}'s user.", status="success")
                time.sleep(3)
            
            except:
                pass
            
            # If the comments are not fully loaded, in this section,
            # it loads the comments completely and then receives a list of new comments
            try:
                driver.find_element(by=By.CSS_SELECTOR, value=load_more_comments).click()
                for new_comment in driver.find_elements(by=By.CSS_SELECTOR, value=like):
                    if new_comment not in list_comments:
                        list_comments.append(new_comment)
                
                time.sleep(5)
                continue
            
            except:
                pass
    
    # If an error occurs during the program
    except:
        show_log("""There is a problem while liking the comments. Please check the following:
                - Check your internet
                - Run the program again
                - Use another account
                - or Please report your error via email to the developer to resolve this issue:
                        Developer Email: mohammadmahyarkermani@gmail.com\n""", status="error")

def restart():
    """After the program is fully executed, it rests for 15 minutes and then is run again by this function."""
    
    clear_screen()
    show_log("The app is restarting, please wait.")
    info_save_following()
    info_save_post()
    return

def start():
    """This function is responsible for executing the program"""

    clear_screen()
    show_log("The program is launching, please complete the configuration steps by answering the questions below." + "\n" * 5)

    config_files()

    info_connect_to_account()
    info_save_following()
    operating_connect_to_account()
    info_save_post()

    # After the program is fully executed, it rests for 15 minutes and then is run again by restart function.
    while True:
        show_log("The app processing is complete. The program restarts after a 15-minute pause.")
        time.sleep(900)
        restart()

if __name__ == "__main__":
    start()