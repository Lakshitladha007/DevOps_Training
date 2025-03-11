GIT COMMANDS

- git init : This command initializes a new Git repository and creates a hidden .git 
folder for version control and related history. 

- git clone: This command will create a local copy of a remote repository. This 
creates a copy such that it includes all branches and commit history also. 

- git status: Shows the status of files which are modified or need to be committed.

- git add [file-name.txt]: This adds the mentioned file to the staging area.

- git add . : This will add all new and changed files to the staged area. 

- git commit –m “[commit message]”: This will comment changes with a message 
whichever we enter.

- git commit --amend -m "New commit message": It is used to update the last commit messgae if we have made any typo error.

- git commit --amend : It is used to make changes to previous commit.

- git branch: This will list all the local branches. On one of the branch asterisk will 
come and that denotes the current working branch.

- git branch –a: This will list all branches and the remote branches.

- git branch [branch name]: This will create a new branch.

- git checkout [branch name]: This will switch to a specific branch.

- git merge [branch name]: This will merge the changes of the specified braanch to 
the current branch.

- git log: This will display the history of commits.

- git push origin [branch name]: This will push the local commits to the remote 
repository.

- git pull origin [branch name]: This will fetch and merge the changes from remote 
repository to local branch

- git remote add origin <url>: his command registers a remote repository (usually a GitHub, Bitbucket repository, etc) with the name origin

-git cat-file <flag> <hash>: Here, hash is the initial 5-6 characters of the commit hash. Flag can be:
  1. -p: Prints the content of the Object
  2. -t: Prints the type of the Object
