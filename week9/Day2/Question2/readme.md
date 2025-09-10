### Create an Azure Container Registry (ACR)

Steps:

1. go to your Azure account and create a container registry.
![alt text](Screenshots/1.png) 

2. Once the registry is created go to Access Policy(IAM), click on "+add", and assign required permissions to the user.

3. Use the folowing command to connect to your Azure Account:
```bash
az login
```
![alt text](Screenshots/2.png) 

4. Login to you container registry, using the command:
```bash
docker login myregistry.azurecr.io
```
The above command returns Login Succeeded.
![alt text](Screenshots/3.png) 


3. Create an alias of the any image that is present on your local system, tag that image using the follwoing command:
```bash
docker tag nginx myregistry.azurecr.io/samples/nginx
```
![alt text](Screenshots/4.png)

4. Now, push the follwoing image to azure conatiner registry.
```bash
docker push myregistry.azurecr.io/samples/nginx
```
 ![alt text](Screenshots/5.png) 
5. Go to the Azure console and verify whether the image has been successfully pushed or not.
![alt text](Screenshots/6.png) 

6. Now, pull the image from Azure and run the conatiner and expose the ports to access on browser.
```bash
docker pull myAzureRegistry.azurecr.io/samples/my-static-page
docker run -it --rm -p 8880:80  myAzureRegistry.azurecr.io/samples/my-static-page
```
![alt text](Screenshots/7.png) 
![alt text](Screenshots/8.png) 

7. Now, open your browser and verify whether the nginx sever is running or not.
![alt text](Screenshots/9.png)

### Custom IAM Role that provides access to manage ACRs in a Resource Group.

Steps:

1. Go to your azure portal and navigate to Subscriptions, in the search bar, type "Subscriptions" and click on it.
Select the subscription where your resource group and ACR exist.
![alt text](Screenshots/10.png) 

2. Go to “Access control (IAM)”, click on Access control (IAM), Click the “+ Add” dropdown and then select “Add custom role”.
![alt text](Screenshots/11.png) 

3. Create a role with suitable name, choose scope as "resource group" and give the minimum permissions as required.
Click Create.
![alt text](Screenshots/12.png) 

4. Assign the Custom Role to a User or Service Principal. Navigate to your resource group (the one you selected in the scope).
Go to Access control (IAM). Click “+ Add” > “Add role assignment”. Select the custom role you just created.
Click Next. Choose the user, group, or service principal to assign. Click Review + assign. And, finally we are done with assigning permission to a particular group.
![alt text](Screenshots/13.png)