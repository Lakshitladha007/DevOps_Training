### Terraform Basics:
Terraform is an open-source tool by that is used for infrastructure provisioning. It enables users to create, manage, and update resources across various cloud providers and services in a consistent and automated manner.<br> 
It works in a declarative format meaning you define the desired state of your application rather than specifying the steps to achieve that state.<br>
Terraform uses HCL(Hashicorp Configuration Language). HCL is a declarative language to define the infrastructure resources to be provisioned as blocks of code.<br>

#### Why Terraform?
> It is powerful, open-source and has a large community.<br>
> Terraform has a immutable infrastructure, which basically means to recreate and reapply rather than patch.<br>
> It works on state management, keeps track of state in '.tf' file which helps in incremental updates(Only what changed is updated).<br>
> Declarative and modular.<br>

### Teraform Providers
The biggest advantage of using Terraform is its ability of provisioning infrastructure across multiple platforms.<br>
This functionality is achieved through "Terraform Providers".<br>
A provider is a plugin that allows Terraform to interact with APIs of external platforms like AWS, Azure, GCP, GitHub, etc.<br>
Providers help terraform manage third party platforms through their API's.<br>
Providers act as a bridge between the Terrafrom code and actual service you want to manage.<br>
There are 3 tiers of providers:<br>
1. Official Providers: These are owned and maintained by Hashicorp and includes ,major cloud providers such as AWS, Azure, etc.<br>

2. Verified Providers: A verified provider is owned and maintained by a 3rd party technology company that has gone through partner-provider process with Hashicorp.<br>

3. Community Providers: Providers that are published and maintained by individual contributors of Hashicorp community.<br>

The commonly used providers are available at the public registry at terraform.io.
Terraform downloads the provider during terraform init. Provider is downloaded into '.terraform' subfolder of your configurations as a default.
You define a provider using the provider block (e.g., provider "aws" { region = "us-east-1" })<br>


### Terraform State File(TF State)
A Terraform state file( .tfstate extension) is a file that stores the configurations of the infrastructure that has been created. It contains the details of terraform version, resources, outputs and others.<br>
Tracks the current state of infrastructure. Terraform records the state of infrastructure as it seen in the real world in TF state file. Based on the TF state file, terrafrom decides what actions need to be taken to update resource of a particular format to achieve desired state.<br>
It should never be modified manually.<br>

### Terraform Lock File (.terraform.lock.hcl)
The ".terraform.lock.hcl" file locks the exact versions of providers used in your Terraform project to ensure repeatable and consistent runs across different machines or teams.<br>
It Records exact versions of all provider plugins used which ensures consistent builds across all machines and team members.<br>
The ".terraform.lock.hcl" file is Automatically created or updated when we runt the command "terraform init".<br>
The file lives at the root of your Terraform project directory and should be committed to version control(e.g., Git).

##### What if Lock File is not present?
> Different team members may end up using different versions of a provider.<br>
> If a newer version has breaking changes, your infra may break.<br>
> Your pipeline might fail.<br>

### Terraform Commands 

##### 1. terraform init
Initializes the Terraform working directory. It downloads and installs plugins which are used within the configuration.
```bash
terraform init
```

##### 2. terraform fmt
This command is used in terrafrom to Format Terraform code in the current directory to a standard style.
```bash
terraform fmt
```

##### 3. terraform validate
It is mainly used to validate the configuration files for syntax and internal consistency.
```bash
terraform validate
```

##### 4. terraform plan
"terraform plan" gives the overview of what Terraform will do without actually making any changes. It is recommended to use this command before running "terraform apply" as it gives a review before applying.
```bash
terraform plan
```

##### 5. terraform apply
This commmand is used to finally provision the desired infrastructure. It applies the planned infrastructure changes.To confirm, it will gives us a prompt and we need to write "yes" to approve.
```bash
terraform apply
```

##### 6. terraform destroy
This commmand is used to delete all the infrastructure that has been provisioned to us.To confirm delete, it will gives us a prompt and we need to write "yes" to approve.
```bash
terraform destroy
```

##### 7. terraform show
This command is used to display the current state of your managed infrastructure.
```bash
terraform show
```


