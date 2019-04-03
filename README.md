# SpeakOut
A web application built using Django framework, where Users can connect to Therapists and Listeners. The User seeking help have the facility to text chat or video call any Listener or Therapist she/he wants. WebRTC is being used for peer-to-peer text chat as well as the video chat. Frontend is designed using HTML5, CSS3 and client-side is validated using JavaScript.

Follow the below steps:

1) Install Python 3.7

2) Install Django 2.0.3

3) Create a virtual Environment using 
	 pip install virtualenv name_of_virtualenv
   
4) To activate the virtual env
	 source name_of_virtualenv/bin/activate
  
5) For installing MySQL database, 
	 brew install mysql
   To start MySQL,
	 brew services start mysql
   
6) Get into the folder where the Project is located.

7) Run the following command to run the migrations
	 python3.7 manage.py makemigrations
	 python3.7 manage.py migrate
   
8) To run the local server,
	 python3.7 manage.py runserver
   
9) For any ModuleNotFound error, run the following command,
	 pip3 install Module_Name
	(Make sure to write pip3, when you are using python3.7 version)
	
NOTE: Recommended  to use Google Chrome for WebRTC.
