# Photo Album with Cloud Storage Integration

## Overview
This project is a Django-based photo album application that migrates your local photo album to cloud storage (e.g., AWS S3) for handling media files. It demonstrates how to configure external storage, update your image upload and display logic, and secure media access with proper permissions. This project is designed with beginner-friendly instructions to help you understand cloud integration with Django.

## Key Features
- **Cloud Storage Integration:** Configure Django to work with external storage services such as AWS S3.
- **Image Upload & Display:** Seamlessly upload images and display them by fetching from the cloud.
- **Media Security:** Implement secure access to media files with appropriate permissions.
- **Beginner-Friendly:** Clear documentation and setup instructions tailored for newcomers.

## Getting Started

### Prerequisites
Before getting started, ensure you have:
- **Python 3.8+**
- **Django** (latest version recommended)
- **Boto3** and **django-storages** (for AWS S3 integration)
- An **AWS account** 

# <span style="color:red">Deployment <span style="color:white">On</span> <span style="color:green">AWS EC2</span></span>

1. do everything necessary for your project and deploy it on gitHub
---

2. amazon > ec2 dashboard > instances > Launch instances > choose a name > choose ubuntu OS > 
Create security gtoup and Create SSH traffic from should be ticked > Launch instance > proceed without key pair > Launch instance
go to instances > wait for status check to becomes green > click on the checkbox on the instance that you created > click on connect
on top of the page > choose ```EC2 Instance Connect``` and click on Connect > now you are in cloudShell
---

3. Type these in couldShell
```shell
sudo apt-get update
# Copy your github Url HTTPS
git clone <your-github-link>
ls 
# You should see your project folder
cd <your-project-name>
# Create venv and isntall requirements
sudo apt install python3-pip -y
pip install -r requirements.txt
```
---

4. Go back to EC2 > instances > click on your ```instance ID``` which is a link > scroll down to and click on ```Security``` tab >
scroll down and click on ```Security groups``` which is a link > scroll down adn click on ```Edit inbound rules``` >
Add rule > set ```Port range``` on ```8000``` and ```DIDR blocks``` to ```0.0.0.0/0``` > Save rules
---

5. Go back to EC2 > instances > click on checkbox belongs to your instance > scroll down and find ```Public IPv4 address``` >
copy it 

---
6. Now you should add the ip to your ```ALLOWED_HOSTS``` that can be done either in the couldShell or in your github repository and 
then pull request from cloudShell, i will explain the cloudShell version

---
7. Head back to your cloudShell on EC2
```shell
ls 
# you should see your project detail
nano <yourProjectName>/settings.py
# Now you are in your settings.py
# Scroll down and add the ip to the Allowed_HOSTS or just type '*' in it
# which would accept any domain
# now for saving it do these combinations
# Ctrl+o     press Enter    Ctrl+x
```
---

8. run this and your server should be up
```shell
python3 manage.py runserver 0.0.0.0:8000
```
---

9. go to this page and you have your server:)
```shell
htttp://<the-ip-that-copied>:8000
```

## Contributing
Contributions are welcome! Whether you're a beginner or an experienced developer, feel free to:

- Fork the repository

- Make improvements or add features

- Submit a pull request If you encounter any issues or have suggestions, please open an issue on GitHub.

## License
This project is licensed under the MIT License.

Tags
#beginner-friendly #Django #AWS S3 #Cloud Storage #Photo Album #Media #Integration #Security #django-storages 

```vbnet
This README provides clear, step-by-step instructions, includes essential setup and deployment details, and is designed to be approachable for beginners. Enjoy building your cloud-integrated photo album!
```
