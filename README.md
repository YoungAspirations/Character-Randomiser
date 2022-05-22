# Character-Randomiser README
[Presentation](Post URL here)

## Introduction<a name= "header1"></a>
This README.md is documentation for my DevOps core fundamental project where I was tasked to create a
functional random alignment application that will return a calculated result from randomly selected inputs. It must utilise the specified tools and skills prior to starting the project.

## Table of Contents
1. [Introduction](#header1)
2. [Requirements](#header2)
3. [Installation](#header3)
4. [My Approach](#header4)
5. [Architecture Evolution](#header5)
6. [CI Pipeline](#header6)
7. [Jira Board](#header7)
8. [Risk Assessment](#header8)
9. [Testing](#header9)
10. [Front-End Design](#header10)
11. [Feature-Branch](#header11)
12. [Troubleshooting](#header12)
13. [Additional Improvements](#header13)
14. [Known Issues](#header14)
15. [Acknowledgements](#header15)
16. [Contributors](#header16)
17. [Author](#header17)
15. [Licensing](#header18)


I will detail all phases of the project, from why specific tools were used sudh as Jenkins for software
automation and testing, upto Ansible and Docker for configuration and deployment respectively. In addition, some additional thoughts for extra improvements will be stated towards the
end of the document.

## Requirements<a name= "header2"></a>
[//]: # "Add requirements to run app "
Here is a brief section on the skills and output requirements of the project that were not mentioned in the introduction.

### Skills
- Project Management - Planning, time management, and agile working
- Python Fundamentals - Advanced Python skills
- Python Testing - To check if the code works how we expect it to before build
- Git - Version Control
- Basic Linux - Commands to operate Linux machines
- Python Web Development - To build a web-based application
- Continuous Integration (CI) - CI through Jenkins 
- Cloud Fundamentals - The ability to use and configure Google Cloud Platforms (GCP) to generate virtual machines (VM) and databases
- Ansible - Configuration of Virtual Machines and deployment
- Nginx - Load balancing between VMs

### Output
- Risk Assessment - An analysis on potential risk factors in the project
- Front-end website - Functional front-end website that uses Flask's integrated API's
- Jira - Project management tool to aid in agile working
- Architecture - Relationship between VMs and user experience
- Automated test suite - A test suite that runs automatically with Git webhooks 
- Feature-Branch Model - Use of Git branching feature throughout development cycle
- Ansible - Configuration and Deployment of app
- Jenkins - Jenkins pipline
- Docker - Containerisation 
- Docker Swarm - Ochestration tool
- Rolling update - Change the function of the app without affecting user experience
- Service orientated architecture- Build app with various services

## Installation<a name= "header3"></a>
[//]: # "Add installation procedure and alternatives to run app"

This section will detail the installation process of the application. If any issues arise make sure you check out the troubleshooting section first.

1. Create VMs with the following names: ansible, manager-1, worker-1, nginx 

2. Next, enter the following command on all VMs, this will make sure all linux operating systems are up to date.

       sudo apt update

3. After, create an ssh key on the ansible VM, press enter on all prompts and add it to your other VMs on GCP or AWS. The creation of the key and viewing can be done through the following command.

        ssh-keygen
        cat ~/.ssh/id_rsa.pub

4. Fork the repository so that it is connected to your account. This will be necessary if you wish to work on this project and use Jenkins web-hook. Otherwise, clone through SSH.

5. Click the green code button, choose SSH or http depending on your needs, and copy the text.

6. Go to ansible VM and clone repository.

7. Go to manager VM and install docker-compose, write the proceeding code to a .sh file and run it by entering . ./[name of file].sh.

        sudo apt update
        sudo apt install -y curl jq
        version=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r '.tag_name')
        sudo curl -L "https://github.com/docker/compose/releases/download/${version}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
        sudo chmod +x /usr/local/bin/docker-compose
        
8. Now, go to nginx VM, install nginx and configure it
        sudo apt install -y nginx

After this, enter the following command so that you can edit nginx.conf to set up your load balancer.
        sudo vim /etc/nginx/nginx.conf
Insert the following code with the private ip addresses of the worker-1 and manager-1 machines.
```
    events{}
        http{
            upstream lb-application {
                server [private-ip-of-host-1]:80;
                server [private-ip-of-host-2]:80;
            }
            server {
                location / {
                    proxy_pass http://lb-application;
                }
            }
        }
```

9. Go to the ansible machine again and execute this line to get ansible to configure and run the app

        ansible-playbook -i inventory.yaml playbook.yaml

The app should now be running and confired the respective VMs with docker, docker swarm and requirements. But, if any issues persist, check out the troubleshooting section.

## My Approach<a name= "header4"></a> 

My approach to the assignment of creating a flask application that generates random objects to be used to return a defined output was a simplified character alignment application. This application would generate random races and roles with predefined values to deduce a individuals moral compass. The README.d will outline how I went about doing that, my deliverables and the refactoring that took place.

I was instructed to build the app over 4 services and they are as follows;

### Service 1

Service 1 is the only service that acts as a bridge between all 4 services to collect all the information and post it to the end user. It uses the http get method to receive data from service 2 and service 3 and the post method to send data to service 4.

### Service 2

Service 2 uses a random function to pick from a list of dictionary race items and then it returns a dictionary as an output.

### Service 3

Service 3 follows the same logic as service 2 but does this for the roles variable instead and returns a dictionary item.

### Service 4

Service 4 receives the posted data from service 1 then starts to run some python logic. The values are extracted from the dictionaries that it recieves and they are summed together. It is then run through some python condtional statements that will calculatee the characters alignment. The result will then be returned to service 1 to be posted to the html page. 

## Architecture Evolution<a name= "header5"></a>

### User Journey

This is a brief section that will show the planned user experience and the final user experience.

This is the planned version for my user journey:

![Imgur](https://imgur.com/h0F0aFF.png)

This is the final version of my user journey:

![Imgur](https://imgur.com/vYyMc2C.png)

### Planned database
Here is the architecture of the app functionality that I wished to create for the users in addition to the evolution of the project as it progressed.

Proposed database model that were drafted but eventually scraped in order meet minimum viable product.

- Races:
    - Race id (primary key)
    - Race  
    - Affinity 

- Roles:
    - Role id (primary key)
    - Role
    - Affinity

- Alignment:
    - Alignment (primary key) 
    - Race id (foreign key)
    - Role id (foreign key)
    - Alignment
    - Moral compass

Users would be able to to view previously generated characters and use all other aspects of CRUD functionality but was ultimately scraped as time was running out.

### ERD Representation

Here is a diagram show the above database relation. 

As shown by the cardinality lines, I was aiming to create a 1 mandatory to many mandatory relational database. However, due to time contrainst I was not able to complete this task.

![Imgur](https://imgur.com/ihfE8u3.png)

Here is the architecture of the VM services at the beginning and end of the project.

Start of the project: 

![Imgur](https://imgur.com/cURGtPv.png)

End of the project:

![Imgur](https://imgur.com/xbXxw8j.png)



## CI Pipeline<a name= "header6"></a>

Below is a repesentation of the continuous integration pipeline that I used throughout the project.

![Imgur](https://imgur.com/tBABqgz.png)

## Jira Board<a name= "header7"></a>
[//]: # "Trello board defining tasks"
Below is a Jira board that I used for project management throughout the project.

![Imgur](https://imgur.com/rami4sQ.png)

The board was created to help with the development cycle while completing the project. The board follows a linear progression of the project from left to right with the following lists;

* To Do - Tasks to do
* Epic - The overall goal of the project
* Project Requirements - MVP of the assignment
* User Story - Thoughts told by the end user of any functionality that they want in the product and why they may desire it
* Dropped - Features I had to drop due time constraints
* In Progress - Where aspects of the project are being implementation in to the project
* Testing - Check to see if code from the previous section works within the constraints of the build
* Done - This list shows all of the completed tasks

## Risk Assessment<a name= "header8"></a>
[//]: # "Self explanitory"
Here is an image of my risk assessment detailing the internal and external risk factors to the project. The risk assessment has been updated throughout the sprint in order to fit the new situation. On the right there is an updates section.

![Imgur](https://imgur.com/fgcs9jf.png)

## Testing<a name= "header9"></a>
The testing on the application was done using unit testing to check specific outcomes. In addition, pytest-cov was used to give coverage reports for the application to see how much of the application was tested. My results are shown below are for the pytest results for service 1, service 2, service 3 and service 4 respectively. Just to mention briefly each test would show 100% if the "if __name__ == '__main__':" statement executes but it does not. In my previous project this was mitigated by having it another file and then importing the object.


Service 1:

![Imgur](https://imgur.com/VNGThCo.png)

For this test I had mocked the get request from services 2 and 3 and the post request from service 4. Then I asserted if specified variables were in the page.

Service 2:

![Imgur](https://imgur.com/ZgU23w2.png)

For service 2 I had asserted that a get request would return a reponse code 200 and I patched some some data to see if the code would still run and give a specified output.

Service 3:

![Imgur](https://imgur.com/GbGgJa3.png)

Service 3 follows the same logic as service 2 as they are pretty much identical.

Service4:

![Imgur](https://imgur.com/zfEGfpV.png)

For service 4 I had asserted that a post request would return a reponse code 200 and I patched some some data to see if the code would still run and give a specified output when different conditions were met as there were quite a few conditional statements.


Taking all the tests into account it accounts for a 93.5% average coverage but if not for the small issue stated earlier it should be 100%

## Front-End Design<a name= "header10"></a>

Here is a look at the html page that I created with its output show the two randomly selected variables and the calculated output.

![Imgur](https://imgur.com/MvMinn7.png)

Also, clicking on the buttons or refreshing the page will give a new output.

## Feature-Branch<a name= "header11"></a>
Here is an image of the project network showing that I used the feature-branch model for code development. This was taken slightly before the end of the project and shows the branches that I used; Dev, feature/README, feature/test, feature/ansible and feature/Docker then pulled the updates into main.

![Imgur](https://imgur.com/XG5wynY.png)

## Troubleshooting<a name= "header12"></a>
[//]: # "Any issues that can be troubleshooted should be listed here"
Here I will state any issues that I had regarding this project that may be applicable to you too.

### Connect machine to your Github account if forking:

1. First open up a terminal in VS Code or in another place
2. Enter the first line just underneath and click enter until all prompts are gone. Next, enter the second line to view the public key and copy everything.
  
        ssh-keygen
        cat ~/.ssh/id_rsa.pub

3. Now, sign in to your Github and go to settings.
4. Finally, move to SSH and GPG keys under access and create new SSH key with a suitable name. You should receive an email.  

Configuration of global name and email on bash for Github usage:

Use the command below to set up global name and user when using Git for the first time on a new system.

    git config --global user.name "Your name"  
    git config --global user.email "Your_email@example.com" 

### Connecting to VM error:

If you follow best practices and delete a VM whenever you are finished for the day, then you may run into an error where you cannot connect to hosts after changing the external IP in the config file. A solution to this can be to view known hosts in the .ssh directory and delete the values. The command can be seen below. 

    rm ~/.ssh/known_hosts

Next, attempt to connect to remote host again and the problem should be solved.

Note: This can also happen whenever a VM is turned off.  

### Syntax:

Make sure that you use correct indentation and spell everything correctly as incorrect syntax or spelling may not show up as issue leading to a long troubleshooting session.

### Docker:

#### Docker Build:
After a while I found that docker would take upwards of 8 minutes to build my images.

A solution that I found for this was to set up a new VM and follow the installation steps again. Or, I found that the following command would help to decrease the time but it is still long.

        sudo apt install haveged

#### Docker Login/Push Failure
If you receive a failure here, try using sudo before every statement to run the command as the root user.

Also, to verify that Docker is installed type the following

        docker --version

This logic also be applied to other installed functions to verify they are installed. 

## Additional Imporovements<a name= "header13"></a>

- Implement CRUD functionality and add a database to persist data
- Get Jenkins to run ansible to configure and deploy the app
- Add a home page and do an overhaul of the user interface
- Include more complex code that uses problem to a more diverse generator
- Code more variables to add to the complexity of the random generator 
- Add a user login so people can store their randomly generated characters
- Run on stronger VMs so I do not have to make new ones because it is running slow
- Overwrite nginx.conf through a bind mount

## Known Issues<a name= "header14"></a>
[//]: # "Known issues of the project"
Issues known to be causing complications for the app:

- There is no CRUD or database functionality as I had originally wanted
- The VMs can take a very long time when building images (a fresh VM would be best but I do not want to take the risk of my app not functioning again)
- Jenkins gets permission when trying to run ansible even after installing the ansible plugin and adding a Jenkins SSh key
- In testing, the if statement "if __name__ == '__main__'" does not run and lowers test score.

## Acknowledgements<a name= "header15"></a>
[//]: # "Acknowledge contributors to the project; Victoria, Ryan, Harry etc."

I would like to acknowledge Ryan Wright, Harry Volker, Victoria Sacre, and Luke Benson for their teachings and support leading into and throughout this project.

Thank you Ryan for your Git, Jenkins, Nginx, Docker and Ansible training. Victoria for your Python knowledge. Harry for the Flask skills while Ryan was sick. And, lastly Luke for your amazing support and problem solving skills throughout the project week.

Without their support this project would not have been a success.

## Contributors<a name= "header16"></a>

The contributor to this project is Christopher Pierre-Samuel with a link given below. 

<a href="https://github.com/YoungAspirations/QA-Projects/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=YoungAspirations/QA-Projects" />
</a>

## Author<a name= "header17"></a>

Christopher Pierre-Samuel <c.pierre-samuel@hotmail.co.uk> 

## Licensing & Copyright<a name= "header18"></a>

© Christopher Pierre-Samuel, QA Academy

The DevOps Core Foundational Project is licensed under the [MIT License](LICENSE).
