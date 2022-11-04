# Gamer Quiz

# Introduction

 Welcome to the Gamer Quiz, A terminal based quiz game.

 Live site link: https://gamer-quiz.herokuapp.com/

 ![Gamer Quiz techsini mockup](readme-extras/techsini-pp3.jpg)

# Table of contents

# User Experience
  ## Target Audience
  It is targeted at people that want to play a quiz game.
  ## Owner Stories
  ## User Stories
  ## Design

# Features

  ## Logo
  ## Welcome message
  ## Username
  ## Acceptable answers
  ## Questions
  ## Correct/Incorrect messages
  ## Number of questions correct
  ## specific message
  ## Play game again or quit

# Future Features

  ## More Questions
   - Add extra lot of questions to make the quiz longer.

  ## Lives
   - Add lives so that user can only get a set number of questions wrong.

  ## Scoreboard
   - Implement a spreadsheet to be used for high scores.

# Testing

  ## Browser Testing

  ## Desktop testing

  ## Validator Testing

   - Validator Installation

    - Pep8online.com website was not available
    - As instructed by Code Institute staff a pep8 validator (pycodestyle) was used in my Gitpod workspace
    - The command pip3 install pycodestyle was used but the extension was already installed
    - Press Ctrl+Shift+p to open search bar and type linter
    - Click on Python: Select Linter and then select pycodestyle.
    - Errors were underlined in red and listed in the problems tab beside the terminal
 
# Bugs

  ## Fixed Bugs
  
  ## Unfixed Bugs

# Deployment

- Before Heroku Deployment I ensured that:

   - Code is located in a run.py file
   - Code Institute template files have not been edited
   - All input statements in program code end with \n so they display on Heroku
   - Requirements.txt has been updated using the command pip3 freeze > requirements.txt

 - I then deployed my project by completing the below steps:

   - Log in to Heroku and click on create new app button
   - Enter project name, select region and and click create app
   - Click on the settings tab and click on reveal config vars
   - Add 'PORT' as a key and '8000' as a value then click add
   - Click on Add buildpack
   - Click Python and then save changes
   - Click nodejs and then save changes
   - Click on Deploy, select GitHub for the Deployment method and then select Connect to GitHub
   - Enter repository name, click Search and then Connect
   - In Manual deploy click Deploy Branch(I later went to Automatic deploys and clicked Enable Automatic Deploys to allow the app to update when i push to GitHub)
   - Click on the view button (or Open App at top of page if returning) to see the deployed project.

# Languages Used

 - Python 3

# Technologies, Frameworks and Libraries used

 - [Python template](https://github.com/Code-Institute-Org/python-essentials-template)
   - The Code Institute's Python essentials template has been used for this project

 - [Gitpod IDE](https://www.gitpod.io/)
   - All code for this project was created using Gitpod

 - [GitHub](https://github.com/)
   - All code for this project was added, commited and pushed to github

 - [Heroku](https://www.heroku.com/)
   - This project was deployed using heroku
    
 - [Techsini](https://techsini.com/multi-mockup/index.php)
   - The mockup image for the readme was created using Techsini
    
 - [TOC Generator](http://ecotrust-canada.github.io/markdown-toc/)
   - The Readme table of contents was created using the TOC Generator
   
# Credits

  ## Contents

  ## Media

  ## Acknowledgements