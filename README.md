# IndianPoliticiansDatabase
Project similar to IMDB using Python Django REST Framework . (backend only)
A Politician rating system 

Features -
1. New User Registration
   Create Account
   Editing details
   Deleting account
   Rate a politician
   Rate a party
   Rate politician's work
 
2. New Politician Registration  (Requires to enter party when registering)
   Create Politician Account
   Edit Details
   Delete Account
   Add work
   
3. New Party Registration (To be registered before politician registration)
  Create Party Account
  Politicians belonging to party are added automatically when they register
  
Ratings of Parties and Politicians start with 10(max), which are then increased/decreased based on user ratings.
   
   
  


To Install -

1.Clone the project using:  git clone https://github.com/AyanF/IndianPoliticiansDatabase.git
2.Install Django: pip install Django
3.Install Rrest Framework: pip install djangorestframework 
4.Migrate the already created models: python manage.py migrate

Running the application
1.In VsCode/Pycharm terminal : python manage.py runserver
2.Click on the link displayed in the terminal or enter your ip adress in browser.
3.Add '/api' at the end to display all api's



API Documentation -

1./api/users

Displays user accounts, works with GET as well as POST request. (can be used to read and write data)

b)/api/users/pk

pk refers to the primary key , add the primary key at the end of the url to send DELETE/PUT/PATCH requests or view details.



2./api/parties

Displays parties, works with GET as well as POST request. (can be used to read and write data)

b)/api/parties/pk

pk refers to the primary key , add the primary key at the end of the url to send DELETE/PUT/PATCH requests or view details.



3./api/politicians

Displays politicians accounts , works with GET as well as POST request. (can be used to read and write data)

b)/api/politicians/pk

pk refers to the primary key , add the primary key at the end of the url to send DELETE/PUT/PATCH requests or view details.



4./api/partyRating

Displays all the ratings given to parites by indvidual users with GET request & inserts ratings when used with POST request. (can be used to read and write data)

b)/api/partyRating/pk

pk refers to the primary key , add the primary key at the end of the url to send DELETE/PUT/PATCH requests or view details.




5./api/politiciansRating

Displays all the ratings given to politicians by indvidual users with GET request & inserts ratings when used with POST request. (can be used to read and write data)

b)/api/politiciansRating/pk

pk refers to the primary key , add the primary key at the end of the url to send DELETE/PUT/PATCH requests or view details.




6./api/politiciansWork

Displays all the work entries by the politicians with total ratings  with GET request & inserts new work entries when used with POST request. (can be used to read and write data)

b)/api/politiciansWork/pk

pk refers to the primary key , add the primary key at the end of the url to send DELETE/PUT/PATCH requests or view details.




7./api/politiciansWorkRatings

Displays work ratings of all works by all politicians with GET request & inserts new work ratings when used with POST request. (can be used to read and write data)

b)/api/politiciansWorkRatings/pk

pk refers to the primary key , add the primary key at the end of the url to send DELETE/PUT/PATCH requests or view details.


