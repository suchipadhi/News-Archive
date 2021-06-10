# Getting Started with Python app for developing a database for articles.

Creating an application to create a database for new articles by following the below steps:
* [Crawl url: https://www.spiegel.de/international/]
* [Extract News-Entries from HTML]
* [Store these entries in a suitable database]
* [Run automatically every 15minutes]
* [Add update_time to existing collections]


## Prerequisites

You'll need the following:
* [Python (3.7)]
* [Docker ]
* [MongoDB]
* [Scrapy]


## Steps to load and run the project

1. Below I have mentioned the link to my Github repo:
* [https://github.com/suchipadhi/News-Archive] 
  
2. First, you have to install the dependencies listed in the [requirements.txt] to run it locally. It is advisable to 
creat a virtual env first .
  ```
pip install -r requirements.txt
  ```

3. The used database is MongoDB and data can be validated in the Mongodb Compass localhost.

* [Download mongodb compass: https://www.mongodb.com/try/download/compass]

Run the below commands in the terminal to access the mongodb port inside docker:
* [docker pull mongo]
* [docker run -d  --name mongo-on-docker  -p 27888:27017 -e MONGO_INITDB_ROOT_USERNAME=mongoadmin -e MONGO_INITDB_ROOT_PASSWORD=secret mongo]
* [docker ps]
* [docker exec -it 470834db1503 /bin/bash]
* [mongo]

Access the server giving the URI in the compass
```
mongodb://mongoadmin:secret@localhost:27888/?authSource=admin] 
```

* Incase the above process does not work, please set up a localhost in mongodb compass and execute the program.


Below is the output after the website has been crawled. There are total [9980] records in the "news" collections 
in the "News_Archive" database. Each document is indexed with ID.

1. The collection before re-run:

```
{
  "_id":{"$oid":"60c1c5daf7ec2b4fd3ab1048"},
  "title":"\nA Country in Flames\n",
  "sub-title":"Complacency and Government Failures Fueled India’s COVID Disaster",
  "abstract":"India’s health care system and hospitals are on the verge of collapse and crematoriums are overloaded. The country got through the first wave of the coronavirus relatively unscathed, but the second has been a catastrophe, the product of inconceivable mistakes by the government.",
  "download_time":"10/06/2021 09:57:14"
  }
 ``` 

2. The Collection after re-run:
  ```
  
  {
  "_id":{"$oid":"60c1c5daf7ec2b4fd3ab1046"},
  "title":"\nA Fateful Election in Scotland\n",
  "sub-title":"After Brexit Could Come Scexit",
  "abstract":"Scottish voters are electing a new parliament this week, and again the pro-independence party SNP is expected to win. The vote could lead the way to the disintegration of the United Kingdom.",
  "download_time":"10/06/2021 09:57:14",
  "update_time":"10/06/2021 13:39:14"
  }
  
  ```
