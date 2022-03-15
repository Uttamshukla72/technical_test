# Problem statement

We need to write code that will query the **meta data** of an instance within **AWS/Azure/GCP** and provide a JSON formatted output. The choice of language and implementation is up to you.



Solution: Cloud provider used: AWS

AWS API for metadata of ec2 instance is : "http://169.254.169.254/latest/meta-data/"

The first call will return the top level Keys and we need to iterate the list of keys with the same API with the key amended at the end. Some of the keys may return another array of keys.

>http://169.254.169.254/latest/meta-data/{key}


pre-reqs: launch an ec2 instance in aws and download the python and git and other required dependency

  
  

Install Python 3 and git on your instance

  

>sudo yum install python3 git

clone the git repo.


Install pipenv

  

>sudo pip3 install pipenv

Go to directory **challenge#2**


>cd challenge#2

Install project dependancies

>pipenv install

# Running

Open the src folder

>cd challenges/challenge#2/src

Run whichever script you need:

>python3 metadata.py

>python3 querymetadata.py
