# Basic Git commands

1. git add (filename)
2. git commit -m"message here"
3. git push

4. git status (for the status)

5. git pull (to pull the changes)

- git clone (link) to clone the repository

# Creating a new repository using the command line
- echo "# REPOSITORY_NAME_HERE" >> README.md
- git init
- git add README.md
- git commit -m "FIRST_COMMIT_MESSAGE_HERE"
- git branch -M main
- git remote add origin https://github.com/MylesE/GIT_REPOSITORY_LINK.git
- git push -u origin main

# Pushing an existing repository from the command line:
- git remote add origin https://github.com/MylesE/GIT_REPOSITORY_LINK.git
- git branch -M main
- git push -u origin main

# Branches:
Create a new branch when wanting to change something - avoid working in main
- git branch: to view branches
- git branch new: creates a new branch with name new
- git checkout branchname: switches to branch with name branchname 
- git merge main: merges branch with name main with the current branch you are working on (usually will be merging main)

# Forking:
Forking a repository copies it to your own account/repository, of which then you can clone
