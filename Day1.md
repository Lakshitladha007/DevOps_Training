Firstly, GIT should be configured in your System, if not then configure:

1. install git to your system

2. check in terminal whether Git has been installed or not, using command:

          git --version

3. configure by adding user-name and user-email using command:

          git config --global user.name "Your Name"
          git config --global user.email "your.email@example.com"

Steps to add a file to remote repository:

1. create a repository that we want git to track

2. initialize the repository by using command:

           git init

3. make the changes to the repository, and add it to staging area using command:

          git add <filename>

4. commit the changes and add a commit message:

         git commit -m "type your message"

5. create a remote repository where we want to push the changes from local repository(example=> You can create a repository on GitHub)

6. add this remote repository using command:

        git remote add origin <remote-repository-URL>

7. finally, push the changes to remote repository using command:

        git push origin master
