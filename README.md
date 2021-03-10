# P4-Ducks Members
Navodit1603 - Navodit Maheshwari

LordRoop - Jagroop Vij

aidanlin4 - Aidan Lin

akprathipati - Ak Prathipati

# [Link to Site](http://76.176.48.196:5671)

# Project Technicals
* Register and Login
  - Login system using Get and POST as highlighed in tech talk Running Code: http://76.176.48.196:5671/login
  - Register page linked with button on Login page.
  - Use of SQLite to make database to store accounts.
  - CSS used for asthetics of background, text font and buttons functional. [code](https://github.com/LordRoop/P4-Ducks/blob/main/templates/home.html)
  - 
* Evaluation using star rating system  using Get and POST methods Running code(WOW):
* http://76.176.48.196:5671/teachers?subject=Math
  - Pulling name of teachers and their subjects from data base. [code](https://github.com/LordRoop/P4-Ducks/blob/main/templates/rating.html)
  - Using radio buttons for rating. 
  - Teacher information, login information stored in the database.  [code](https://github.com/LordRoop/P4-Ducks/blob/main/templates/rating.html)
* Web Api using twitter about the school district Running Code: http://76.176.48.196:5671/news
  - PowayUSD and DelNorte twitter accounts used for news for the school and district. [code](https://github.com/LordRoop/P4-Ducks/blob/main/templates/news.html)
* Use of CRUD operation(Algo for CB): Running code:http://76.176.48.196:5671/profile
  - Able to change and delete acount information. 
  - Signout button signs out the account and leads to the login page. 
* Home Page
  - Accessable animated buttons on home page that lead to teacher rating pages for the specific subject [code](https://github.com/LordRoop/P4-Ducks/blob/main/templates/rating.html)
  - Navigation bar contains link to important pages rearding the account
  - Easter eggs in home page 
      - [AK and Aidan's Easter egg](http://76.176.48.196:5671/)
      - [Roop and Navodit's Easter Egg](http://76.176.48.196:5671/meme)



# Summary 
We are trying to create a rating system for teachers. We will be taking data that is given by students. Later on, if we are ahead of schedule, we will also try to have the students write comments and we will have a more specific criteria so they can grade their teaching, how hard the tests are, and their knowledge on the material and so on. We will use CRUD to monitor the reviews that are given for offensive and/or hateful messages, and we will try to create a system that prevents students from commenting repeatedly to inflate or deflate any teacher’s rating. Our major goal is to have a concrete understanding on data as well as to provide teachers some constructive feedback so that they can improve their teaching. Many teachers are not that adept at teaching online, and can use this as a learning experience to improve their teaching style.   

# Links
* [Site](http://76.176.48.196:5671)
* [Project Plan](https://docs.google.com/document/d/1wxPf8kZwcLD7A78uW7GT-fFjmGbNxHtRAVDDZ21xz30/edit?usp=sharing)
* [Scrum Board](https://github.com/LordRoop/P4-Ducks/projects/1)
* [AK and Aidan's Easter egg](http://76.176.48.196:5671/)
* [Roop and Navodit's Easter Egg](http://76.176.48.196:5671/meme)

# Mini Code and Ticket Review
## Navodit
* [Login Page](http://76.176.48.196:5671/login)
* [Signup Page](http://76.176.48.196:5671/registration)
* Login and Registration page fully functional. CRUD used in these pages. 
* Used POST and app routes (functions imported on top and app routes at the end) to transfer user data through html and python file to database. [Link to register code](https://github.com/LordRoop/P4-Ducks/blob/55b92de8c86ec6f17f56529a2470460dbaf54419/templates/registration.html#L95) | [Link to login page code](https://github.com/LordRoop/P4-Ducks/blob/55b92de8c86ec6f17f56529a2470460dbaf54419/templates/login.html#L91) | [App route code](https://github.com/LordRoop/P4-Ducks/blob/main/main.py) 
* Functions made to authorize accounts [Link to code](https://github.com/LordRoop/P4-Ducks/blob/55b92de8c86ec6f17f56529a2470460dbaf54419/create.py#L49)
* Function made to make sure that every user has an unique user name [Link to code](https://github.com/LordRoop/P4-Ducks/blob/55b92de8c86ec6f17f56529a2470460dbaf54419/register.py)
* The crossover group liked the use of CRUD and mentioned that data in the data base was well organized. [Link to evaluaton](https://drive.google.com/file/d/1ZP822bQrlk-SRHX87UzAG-5tOL4vkk9g/view?usp=sharing)
* College board
  * Uses lists to store username, password and email as data
  * Data is being passed through POST from html file to the python file to go in the Database
  * Functions are used to make sure that accounts are being created correctly. One account per email and checking username and password when logging in. 

## Roop
* [Meme Page](http://76.176.48.196:5671/meme) fully completed
- for loop runs on timer cycling through images
- Meets collegeboard requirements according to [College Board requirements](https://drive.google.com/file/d/1o27CE_wJgGf1s4DooOijO3A4PqTF_bkE/view?usp=sharing)
* [Star rating System UI](http://76.176.48.196:5671/teachers?subject=Math) fully completed
## Bulls Recommendations
*Update CSS(done by AK)
*organize code (Roop and Navodit)
*Change UI for the teacher page

## Aidan
* Added Random Fact Generator Easter Egg API
* Created [Who Am I Easter Egg](http://76.176.48.196:5671/whoami)
* Implemented [Twitter WEB API](http://76.176.48.196:5671/news) to embed twitter profiles to get updated on school's twitter
* Meets [College Board requirements](https://drive.google.com/file/d/1o27CE_wJgGf1s4DooOijO3A4PqTF_bkE/view?usp=sharing)

## AK
*Added CSS to Easter egg (http://76.176.48.196:5671/)
* Created Evaluation Page [Evaluation](http://76.176.48.196:5671/Evaluate)
* Was able to add get pass data [Get and Post](https://github.com/LordRoop/P4-Ducks/commit/2a90269223a71e830d854eec6f005d4c025d299b)
* Worked on main UI:[Main CSS](http://76.176.48.196:5671/teachers?subject=Math)  
* Created comment section and drop down rating system[Evaluation](http://76.176.48.196:5671/math)
* Worked on the CSS and the esthtics of the code
* Was able to meet College Board requirements: https://drive.google.com/file/d/1o27CE_wJgGf1s4DooOijO3A4PqTF_bkE/view?usp=sharing talks about where we are 
*Able to change some CSS on teacher pages as instructed by the bulls 
# Log 
* 2/4/21: Aidan changed the code to the [Random Fact Generator easter egg](https://github.com/LordRoop/P4-Ducks/projects/1#card-53864903) so its compatible with Roop's Nas, and also added the [Who am I easter egg](https://github.com/LordRoop/P4-Ducks/projects/1#card-54301133). [Aiden's RFG] (http://76.176.48.196:5671/rfg)
* Ak: Job was to Add CSS to the API, meme page, and the Who am I page. He also had to get a head start on passing data, all he has to do is add commands in the terminal. [Big ticket for AK](https://github.com/LordRoop/P4-Ducks/projects/1#card-54306702)[Ak's CSS] (http://76.176.48.196:5671/rfg)
* Navodit: Navodit worked on the login and registration backend to be able not have multiple accounts with the same user and email.[Big Ticket for Navodit](https://github.com/LordRoop/P4-Ducks/projects/1#card-54306767) |[ Code](https://github.com/LordRoop/P4-Ducks/blob/main/register.py). He also added the meme page and was able to make it change every 5 seconds [Link to code](https://github.com/LordRoop/P4-Ducks/blob/main/templates/meme.html) | [Link to page](http://76.176.48.196:5671/meme) 


# Big Tickets 

* 1/15/21: We were able to add our diliverables that was able to corrospond to our scrum board. [Scrum Board](https://github.com/LordRoop/P4-Ducks/projects/1) One main ticket ideas were to have a much more ellegant UI, which is deliverbale three. Another main ticket idea was to have an evaluation page where people can rate the teachers, dilverable two. Finally, the last diliverable was to make sure make a login page, where it promotes the user to put username and password and we also created a sign up page as well to avoid spam ratings! Big ticket ideas planned: Comments, Liking comments, Star Reviews, Search bar feature
@ Aiden is working on the back end code. A near futrue goal is to be able to manage data in a database. It can be used to manage accounts, likes, rating and comments. 

* 1/8/21: We were able to create different pages for different departments. We then created a spreadsheet with all the teacher's names and put them in on the website. We used a card format so on each teacher card, it would display an icon related to their subject, their name and stars for rating them. Eventually, we will make them buttons that will lead to teacher's own pages for ratings and comments. We also added a background and added a dictionary. This will help us to have icons that will lead to different links like out github.   

* 12/11/20: GitHub repository set up. Updated Readme. Scrumboard Created. [Project plan](https://docs.google.com/document/d/1wxPf8kZwcLD7A78uW7GT-fFjmGbNxHtRAVDDZ21xz30/edit?usp=sharing) made 

# Run Instructions
* Click this [Link](http://76.176.48.196:5671/)
* Or Paste this link in you browser: http://76.176.48.196:5671/ 

# Deliverable 1(Front End): Login in page and username and password
* [Login Page](http://76.176.48.196:5671/login)
* Done by @Navodit
* The UI of the username and password was made and a registration page was also made.
* The code incorporated CSS and the UI is well established. 
* The sign in button leads to the homepage and the "create a new account" leads to the regisration page.
* The buttons also have a fuction in the registartion page. Sign up button leading to the home page and "I have an account" button leading to the login page.
* Futrue goal is to be able to store accounts and have real login identifications.

# Deliverable 2(Front End): Evaluation page
* [Evaluation Page](http://76.176.48.196:5671/Evaluate) 
* Done by @Ak 
* created a UI that allows the person to evealuate the teacher 
* Had a drop down menu to score them from 1 to 5
* Icorporated CSS to make it look better
* Future goal is to incorperate it with the teacher pages

# Deliverable 3(Front End): Getting CSS and perfecting the UI and making it presentable 
* [Home Page with Navigation bar that leads to all the pages](http://76.176.48.196:5671/)
* Done by @Navodit and @Ak 
* they were able to make the pages look better, make it have stars,added new routes,they were able to change the first page that was present, added pictures which corrspned to teachers, made the coard UI.
* All in all, they basically made the UI look a lot better, 

# Portforwarding
* Done by @Roop
* Project is now accessible through the internet. 
* Implementation of security measures is in progress.
  - Linux container has been put in a seperate subnet within LAN.
  - Firewall implementation in progress.
# Big Tickets 
* Ak: Job was to Add CSS to the API, meme page, and the Who am I page. He also had to get a head start on passing data, all he has to do is add commands in the terminal. [Big ticket for AK](https://github.com/LordRoop/P4-Ducks/projects/1#card-54306702)

* Navodit worked on the login and registration backend to be able not have multiple accounts with the same user and email [Code](https://github.com/LordRoop/P4-Ducks/blob/main/register.py). He also worked on the meme page easter egg by making the images change every 30 minutes. The pictures are also sized and centered.  [Meme Page]() | [Link to code](https://github.com/LordRoop/P4-Ducks/blob/main/templates/meme.html) | [Big Ticket for Navodit](https://github.com/LordRoop/P4-Ducks/projects/1#card-54306767)

* Aiden: devlop the easter egg and made the API compatiable with Roop's portforwarding.[Big Ticket for Aiden](https://github.com/LordRoop/P4-Ducks/projects/1#card-54306731)
