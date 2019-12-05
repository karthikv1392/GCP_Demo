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
    7. vim 00-default-sites.conf
    8. Inside the <Virtualhost:*80> add the following 
    
        ProxyPreserveHost On
        
        ProxyPass /getImageDetails http://localhost:8065/analyze
 
## Exercise

1. Deploy a hello world app in the app engine https://cloud.google.com/appengine/docs/standard/python/quickstart
2. Install Jupyter notebook in your instance and access it from your local machine


## References

1. https://cloud.google.com/python/docs/reference/

