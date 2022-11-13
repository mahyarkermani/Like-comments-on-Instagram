# Warning

Support for this source code (repository) ended in April 2022 and this source will no longer be updated. So, the code may have bugs and you can run it and debug it (and send the modified version to my email to publish with your name) or use the forks of this repository.


# Introduction

This module is responsible for liking the comments Blow
the post accounts are collected from the user's following.
This app is a scrapper to do some things on the Instagram website.
This program receives and likes the comments below each post of the last 24 hours from your following

# How does the program work?

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


# Abilities

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


# Tested on

Currently, this program has only been tested on Windows 10, and with Python 3, and will be compatible with other operating systems in the future.
So please customize it if needed.

# Introducing the tool

This program is provided in the form of Python source code, and in this section we will introduce
the folders and tools available in the program.
The first folder is plugin, Where the webdriver of the browser is located (to run programs and scraper, we need this software).
In this program, we use Firefox as a browser for scraping. So you need to download the latest version of Firefox and WebDriver from the following links:

- Firefox download link: [Mozilla Pages](https://www.mozilla.org/en-US/firefox/download/thanks/)
- Webdriver download link: [github Pages](https://github.com/mozilla/geckodriver/releases/)

Install Firefox from the link above and download the 'geckodriver-[xxxx]-win[xx].zip' file from the second link and place it in the plugin folder.
The next folder is the software, where we usually put the software needed in the Windows operating system so that you can install them if needed.


# Prerequisites

This program is written with Python 3.9 but supports Python 3 and all versions.
The required modules of this program are located in the 'prerequisites' file in the plugin folder, and you can install the required modules with the following command:

{python -m pip install --upgrade pip}
{python -m pip install -r plugin\\prerequisites.txt}

In this program, we use Firefox as a browser for scraping. So you need to download the latest version of Firefox and WebDriver from the following links:

- Firefox download link: [Mozilla Pages](https://www.mozilla.org/en-US/firefox/download/thanks/)
- Webdriver download link: [github Pages](https://github.com/mozilla/geckodriver/releases/)

Install Firefox from the link above and download the 'geckodriver-[xxxx]-win[xx].zip' file from the second link and place it in the plugin folder.


# About the author

This program was written by a young Iranian and this person tries to keep his GitHub programs always up to date.
If would you like to contact me, you can send a message to my personal email:

- **mohammadmahyarkermani@gmail.com**

You can also see my resume at the following link:

{}


# Report bugs

Since this program is written as a scraper and with a small change on Instagram,it may crash,
Please if you have any problems with how the program runs and works, please publish your error in the issue section of GitHub
or send it to my email to fix the bugs of the program as soon as possible. Thank you for your cooperation :)
