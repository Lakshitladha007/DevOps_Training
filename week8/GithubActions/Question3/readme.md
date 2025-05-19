Steps:

1. Go to your repo settings, and under Environments, create a new environment and add a reviewer before deployment.
![alt text](Screenshots/1.png)

2. Now write your cs.yml file and in deploy job, add the Environment, so that it asks for manual approval before deployment.

3. Now, push the code to github and verify the process.
> Approval needed before deployment:<br>
![alt text](Screenshots/2.png) 

> Added approval:<br>
![alt text](Screenshots/3.png) 

> Workflow successfully executed:
![alt text](Screenshots/4.png)