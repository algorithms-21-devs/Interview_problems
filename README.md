# Interview - Questions
This repository is dedicated to preparing aspiring programmers for a 'technical interview.' New Interview Questions are posted every week. Everyone is encouraged to contribute and submit their solutions for consideration. Rules for submitting can be found below. No particular language is mandatory.


## A. Rules for submiting solutions

### Steps
1. Name Your solution according to the File Name Convention listed below (i.e. Q1Medium_bruteforceapproach.py) .
2. Create a folder according to the Folder Name Convention below (i.e. Q1_Algorithms-21 ) .
3. Put all your files, inside the folder you created (i.e. Q1_Algorithms-21 > Q1Medium_bruteforceapproach.py) .
4. Find Your Question Folder (the folder that asks the question you are responding to. (i.e Q1))
4. Put the folder you created inside the Question folder
5. I.E Q1 > Q1_Algorithms-21 > Q1Medium_bruteforceapproach.py is an acceptable folder and file structure if you are responding to Question 1, your solution is named Q1Medium_bruteforceapproach.py, the folder you created is named Q1_Algorithms-21,and your question folder is Q1 .

<br>

###  File Naming Convention
<br> | Rules & Descriptions
------------ | -------------
Rule | You must save your solution as Q#ConditionMode_yourchoiceofwords
Q# | is the Interview Question you are answering (i.e Q1 for question 1)
ConditionMode | The difficulty of the contraints of your algorithm operates in. (i.e Easy, Medium). Find this in the text file containing the interview question.
Example 1 | Q3EASY_bruteforce.py indicates the solution is solving Question 3, conditions are EASY, through a bruteforce method and is a python file. Q3Medium_O(n) indicates the solution is solving Question 3, conditions are medium, and the time complexity of your algorithm is O(n). 
Example 2 | Q3Medium_O(n) indicates the solution is solving Question 3, conditions are medium, and the time complexity of your algorithm is O(n). 

* Thus, anything after the underscore(_) is meant as a descriptor of YOUR choice that differentiates one approach to an algorithm from another. 

<br>

###  Folder Naming Convention
<br> | Rules & Descriptions
------------ | -------------
Rule | You must create a folder named Q#_yourgithubusername
Q# | is the Interview Question you are answering (i.e Q1 for question 1)
yourgithubusername | Your github username. 
Example |Q3_algorithms-21 is an acceptable folder name if I you are answering Question 3 and your github username is algorithms-21



## B. Resources
* ### Data Structures
* ### Algorithms
* ### Git Hub Basics
##### Basic Instructions
**1. Create/Log In to your GitHub and go to the desired GitHub group open source account** 

**2. Fork**
* Click on the "Fork" button on https://github.com/algorithms-21/Interview_problems.git
  * This will produce a personal copy of someone else's project.

**3. Clone**
* Click on "Clone/Download" button and copy the github repository link 
* Go to terminal/command line and go to desired directory where you will be storing project and adding your files
* Enter the command: 
  * git clone [repository_url]
    * This will create a local directory of the repository on your computer 
    * In our case it is **git clone https://github.com/algorithms-21/Interview_problems.git** 
 
**4. Adding your files**
 * Now you can add your files and folders. Be sure to adhere to the naming conventions when adding files/folders

**5. Synchronization** 

*Before you add and commit your files, you need to be able to get the latest version of the repository*
* For the master branch: 
  * git remote -v
  * git remote add upstream copied_url
    * In our case, it is **add upstream https://github.com/algorithms-21/Interview_problems.git**
  * git remote -v
  * git fetch upstream
  * git merge upstream/master

**6. Add / Commit**

*Now that you have synchronized your local respository with the online reposity, you can add and commit your files* 
* git status 
  * This will show you new or modified files that you have not committed 
* git add -A
  * This will add all new files. If you want to add a specific file then **git add [file]** 
* git commit -m "your comment here"
  * This will commit you files with a message describing your changes 

**7. Push**

* git push origin master
  * This will push your files unto your online repository

**8. Pull Request & Revision** 

*Even though you have pushed your files to your online repository(the copy you made), only your forked reposity has changed. To make changes to the main repository (algorithms-21/Interview_problems), you need to create a pull request to synchronize your version with the original project*
  * Go to your repository and find your personal forked version of the project 
  * At the top, click on "pull request" tab and click on "New pull request" button 
  * After creating the pull request, your algorithm submission will be reviewed. If changes need to be made, you will receive an email. If not, the pull request will be accepted and merged to the main project. 


For more information on how to perform these steps, watch: https://www.youtube.com/watch?v=HbSjyU2vf6Y&feature=share
