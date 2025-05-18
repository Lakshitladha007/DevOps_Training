Steps:

1. Create an EC2 instance and install all dependencies such jdk and jenkins. also allow traffic on post 8080, allong with http, https and ssh.

2. Now, verify whether jenkins is running or not. Jenkins can be accesed on chrome using:
```bash
http://<public_ip_ec2>:8080
```
Now, add the password and create user, your jenkins setup will be completed.

3. Go to add items, create a job and configure the job, Under Source Code Management, choose Git and Paste GitHub repo URL (e.g., https://github.com/your-name/your-repo.git). And finally, 
Set the branch to build: */main or */master.

4. Under triggers, chooose: "GitHub hook trigger for GITScm polling". Now, now finally aplly and save.

5. Configure the Webhook in GitHub, Open your GitHub repo. Go to Settings → Webhooks → Add webhook.
Add the payload URL as:
http://<ec2_public_ip>:8080/<job_name>/
and choose, "Choose Just the push event".

6. Now, when you push something to Github the job is automatically triggered.
![alt text](<Screenshots/Screenshot 2025-05-17 181503.png>)

