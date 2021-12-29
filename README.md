# :exclamation::exclamation::exclamation: DISCLAIMER :exclamation::exclamation::exclamation:
This project is an intellectual and practical project that I do to improve myself, learn new things and satisfy my curiosity. Although some parts have been tried to test, since I do not find it ethical, it has not been tried to add everything that needs to be added and get results.

# :man_technologist: TryHackMe AdventOfCyber3 Bot :man_technologist:
This project opens a new account on the TryHackMe site and participates in the raffle for the AdventOfCyber 3 event by answering all the questions.

# About the Project :blue_book:
The project has been prepared using Selenium, request and bs4 libraries.

In the project, one user-agent is taken from the user-agent list, and with the help of Selenium and geckodriver, go to the tryhackme site and register. Then the cookie and csrf tokens are set. Fills the questions in the specified room (adventofcyber3) by pulling the data from the json file obtained from a previously filled account with the help of api (Check the address from an account where questions are resolved: https://tryhackme.com/api/tasks/adventofcyber3). It also saves the entered id and password information in the specified form. It does this as an endless loop. 

# What You Need to Set Before RUN
:warning: For Geckodriver to work, you must have firefox installed on your computer.

:warning: On line 17 you have to give the geckodriver directory.

:warning: On line 27, you must give the directory of the json file you have taken with the api.

:warning: If you are going to fill in another room, you should change the variable name on line 28 with the name of that room in the url.

:warning: You can change the name and password algorithm, it's obvious that it's random.

:warning: Enter the google form url you created in the formUrl variable on line 80.

:warning: Accordingly, you should edit the entry ids on line 81.


# What Needs to Be Added by the Exploiter to Develop and Get Results
This idea first started with a mouse clicker, then I added a keyboard feature and then I started using Selenium IDE. Then I switched to python and continued with Selenium. Later, I started to fill out the questions with request after registering because Selenium works slowly and has some limits. From here on;

:open_book: `YOU NEED VPN OR PROXY. YOUR IP ADDRESS MUST CHANGE EVERY CYCLE.`

You definitely need a Proxy for the project to be perfect and run successfully. In the current situation, although the time varies according to the connection location, you need to solve a recaptcha every 10 minutes on average. You can solve this problem by using the listen feature of recaptcha, download the file, and then get the result with one of the speech-to-text applications. However, the problem here is that after a certain number of times, the recaptcha realizes that you are a bot and does not allow you to solve the recaptcha. You need to change your IP.

In addition, although this time varies depending on the intensity (15mins to few hours), TryHackMe's cloudflare catches you for making constant requests and bans your thread after an average of half an hour. For this scenario, I think you can solve the problem by increasing the request time a bit and setting things like cookie, header, csrf more accurately. However, time is very important for this project and you have to send fast requests when you don't have enough machines to run the code. In this case, you should have a VPN or proxy that you can change ip without worrying about the ip ban.

Another problem is that they can check the records made for the same ip, user-agent, or other parameters while the last raffle was made. So you have to be careful that everything is unique. At this point you again need a proxy or vpn.

:open_book: `NAMES, PASSWORDS AND EMAILS MUST BE UNIQUE.`

Uniqueness is very important, so you should have a good name and password algorithm so you don't encounter similar or related results when looking from database or lottery results.
I don't know if they checked while the raffle was being made. However, for the final result, the accounts can be approved by using temp-mail with the help of api. However, I recommend using hotmail or gmail, as email hosts will raffle attention after a certain number of times.
