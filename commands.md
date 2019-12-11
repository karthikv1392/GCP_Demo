## Set up your GCP 

1. Use the code and sign up for a GCP account
2. Log in to the console
3. Launch an instance from Compute engine with basic 1Gb RAM, 10 GB persistence,  Ubuntu 64-bit version
4. Create set of keys by adding to the metadata of the instance in the edit option
5. ssh-keygen -t rsa
6. Paste your public key in the metadata section
7. For mac users, it will be created in cd /Users/<username>/.ssh (For windows use, puttygen)
8. ssh -i <private_key> username@instance_ip



## Install Apache web server

1. sudo apt-get update
2. sudo apt-get install apache2
3. sudo apt-get install vim (For easy editing)



## Set up the Python Environment

1. wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
2. bash <Miniconda_file>.sh
3. source ~/.bashrc (For changes to take effect)
4. pip install tornado

## Deploy a webservice in GCP compute

1. Copy the web service to your instance using scp -i key.pem -r /path to your code/ username@ipadress:/home/username/foldername/
2. Enable proxy in apache :
    1. sudo a2enmod proxy
    2. sudo a2enmod proxy_http
    3. sudo a2enmod proxy_balancer
    4. sudo a2enmod lbmethod_byrequests
    5. sudo systemctl restart apache2
    6. cd /etc/apache2/sites-available
    7. sudo vim 000-default-sites.conf
    8. Inside the <Virtualhost:*80> add the following  (press insert button to edit, for mac users, press "i")
    
        ProxyPreserveHost On
        
        ProxyPass /getImageDetails http://localhost:8065/analyze
        
        (Press "esc :wq" to save and exit vim)

### Enable Google Vision API

1. From the navigation menu in the Google Cloud Services, select "API's and Services"
2. Above will take you inside the dashboard view of API's and servies, Press "Enable APIs and Services" button (with + sign)
3. Search for "Cloud Vision API" in the search bar and press enter
4. Click on "Cloud Vision API" and click on the "Enable" button
5. Go back to the Google Cloud main console
6. Select "API's and Services" from the navigation menu on the left
7. Click on "Credentials" from the left pane
8. Press "Create Credentials" -> "API key"
9. A key will be created, Copy the key and paste it in a text in your local machine "api_key.txt"

### Starting the Service

1. Go to the directory where the code has been copied
2. Open the settings.conf using command vim settings.conf
3. Add the copied API key in the api_key field of settings.conf
4. Save and exit settings.conf (esc :wq)
5. Run the services using the command "Python Vision_Service.py"
6. You should be able to see "Starting service on Port 8065"

### Making Request to the WebService

1. Go back to your local machine and open "upload_post_server.html" from the clonned Git repository
2. Edit the line 8 of the html using text editor (This line <form enctype="multipart/form-data" action="http://localhost:8065/analyze" method="post">)
3. Replace the url in line 8 with "http://your instance ip/getImageDetails
4. Open the html in a browser, click on the upload button and select any image file
5. Click submit and check the response
    

You have successfully deployed a web service on your instance !!
 
## Exercise

1. Deploy a hello world app in the app engine https://cloud.google.com/appengine/docs/standard/python/quickstart
2. Install Jupyter notebook in your instance and access it from your local machine


# Kafka Commands

Source : https://kafka.apache.org/quickstart



Start Zookeeper

bin/zookeeper-server-start.sh config/zookeeper.properties



Start Kafka Server

bin/kafka-server-start.sh config/server.properties


Create topic

bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic test


Send Messages

bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test



Start a consumer

bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning


List topics

bin/kafka-topics.sh --list --bootstrap-server localhost:9092








## References

1. https://cloud.google.com/python/docs/reference/


For futher queries contact: karthikv1392@gmail.com
