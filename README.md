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

# <span style="color:red">Serve <span style="color:white">the static and media</span> <span style="color:green">on AWS S3 Storage</span></span>

### open a notebook and add the important things in it during the tutorial
#### Creating a bucket
1. amazon website > s3 > Create bucket > write a ```bucket name```(and add it to your notebook) > 
let the aws region be on default (add to notebook(ex: us-east-2)) > Uncheck ```Block all public access``` > 
check the yellow card ```I acknowlefge that the current ...``` > create bucket
---

#### Creating json policy
2. click on your bucket name which you just created > Permissions tab > scroll down on ```Bucket policy``` click on Edit >
Copy the ```Bucket ARN``` and click right on ```Policy generator``` and open in new tab(don't leave the edit page yet) >
in the new page:
```txt
1.select policy type: S3 Bucket Policy
2.effect: Allow
3.principal: *
4.Actions: GetObject
5.ARN: <paste-the-arn-from-previous-page>
6.Add Statement
7.Generate Policy
```
copy the json policy fully as exactly as is without any extra space or anything less > 
go to previous page and paste it there again be careful don't miss anything and don't add anything not
even a space > Scroll down and Save changes
---

#### Creating an IAM User
3. amazon > IAM > left navBAr click on Users > Create user > type a user name(add to notebook) > check the ```Provide user access ...``` >
select ```I want to create an IAM user``` > choose custom password > type a strong password(add to notebook) > 
uncheck ```Users must create a new password ...``` > Next > Attach policies directly > on Permissions tab search for ```AmazonS3FullAccess``` and check it >
Next > Create User > you can download .csv file too
---

#### Getting access Key
4. On the users page click on the user that you created > on the top right side click on the link ```Create access key``` >
Choose Local code > Check ```I understand the above ...``` > Next > Create access key > copy the ```Access key``` and ```Secret access key```
in your noteBook or just download .csv file > Done
---

#### Downloading CLI and Configuring it
5. Download CLI and install it > open cmd:
```shell
aws ==version
# you should see the aws has been installed

aws configure
<paste-access-key-id-from-notebook>
<paste-secret-access-key-from-notebook>
<origin-from-notebook>(ex: us-east-2)
json(doesn't matter)
```
---

#### Preparing your project
6. open your project and install these packages:
```shell
pip install django-storages
pip install install boto3
pip install django-decouple
```
go to settings.py:
```python
# Import config for virtual environment 
from decouple import config

# Add the storages to installed_apps
INSTALLED_APPS = [
        #...
        'storages',
        #...
]

# ...

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / 'static']

# Media
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# AWS S3 Configuration
# 
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID_ENV')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY_ENV')

# Storage Configuration for Amazon S3
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME_ENV')
AWS_S3_CUSTOME_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_FILE_OVERWRITE = config('AWS_S3_FILE_OVERWRITE_ENV')

STORAGES = {
    
    # Media file management
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
    },
    
    #CSS and JS file management
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
    },
}
```
Create a ```.env``` file if you don't have one and add these to it:
```text
AWS_ACCESS_KEY_ID_ENV=<access-key-id-from-noteBook>
AWS_SECRET_ACCESS_KEY_ENV=<secret-access-key-from-noteBook>
AWS_STORAGE_BUCKET_NAME_ENV=<bucket-name-from-noteBook>
AWS_S3_FILE_OVERWRITE_ENV=False
```
---

#### Final Step Collecting statics and it's done
7. in your project type this
```shell
python manage.py collectstatic
```
---

8. now you can set the debug in the settings.py to false and if you run the server you see s3 storage is serving your media and static for you:) 
---

# <span style="color:lightred"> Clean up (Don't do this if you want to keep your bucket list)</span>
# <span style="color:lightred"> This part is for people who want to get rid of unused users and bucketLists</span>
## deleting the bucket and the IAM user and Access key
Amazon > IAM > Users > user you created >  scroll down choose ```Security credentials``` tab > 
Scroll down on Access keys click on actions and choose deactivate and again Actions choose delete > add the key to the box and Delete >
Go to Buckets > click on your bucket radio button and on top choose ```Empty``` > type permanently delete > click on your bucket radio button again and delete it
go to IAM > users > checkbox on your user > and delete > type the name of your user > Delete user



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
