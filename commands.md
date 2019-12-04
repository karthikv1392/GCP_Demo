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
3. sudo apt-get install vim
