# Secret Santa

Necessary pip installs can be found in requirements.txt
Simple flask web application that takes in multiple users and, through admin power,
randomly choose for each user a person to be gifted. Information is sent through
email.

Database contains three columns:

Username|Email|Want
--------|-----|----
User's name :+1|User's email :+1|What the user would like :+1

Views file contains backend implementations:

Confirm|Match|EmailSecretSantas
--------|-----|----
Confirmation after each user inputs info :+1|Matching Users :+1|Emailing each user :+1

Within the templates dir can be found html files.
Within the static dir can be found css files with images and fonts.

