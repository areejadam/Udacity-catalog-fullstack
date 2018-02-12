Tournament Results
This project is a part of the Full Stack Web Developer Nanodegree through Udacity.

About
This project is a website that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

Requirements
You will need these installed in your computer:

Vagrant
VirtualBox
Google Developer Account
Running The Project
Clone the repository

Navigate to the project directory

Create new project on https://console.developers.google.com/

Now you should have client Id and secret from Google project. Type ID and Secret to client_secrets.json file

Run following command to setup Vagrant.

 > $vagrant up
Run following command to login to your Vagrant VM:

 > $vagrant ssh
Run following command to change to the shared folder:

 > $cd /vagrant
Run following command to setup database schema:

 > $python database_setup.py

 > $python data_seeder.py
Run following command to run the project:

 > $python main.py
App will start running on configured port.