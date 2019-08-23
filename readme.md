# Running the test project locally
1. Clone repository (git clone ...)
2. Setup python virtualenv (virtualenv ...)
3. Get require python packages (pip install -r requirements.txt)
4. Migrate django db from new virtualenv (python manage.py migrate)
5. Collect static files  (python manage.py collectstatic --noinput)
5. Collect NPM packages (npm install)
6. Start webpack dev server (npm run dev)
7. Start the django dev server (python manage.py runserver --nostatic)
8. Open localhost:8000 in web browser


# Notes
- The django / python setup is for creating and requesting data from an api endpoint
- Went doing frontend developing do it in the src folder using VueJS
- Webpack is setup to automatically update the webpage when you save a change in VueJS (if currently being viewed in browser)


# Setup Virtualenv Instructions
1. Make sure you have python installed
2. pip install virtualenv
3. virtualenv venv (`venv` is whatever env name you want)


# Important URLS
- http://localhost:8000 - main dev site url
- http://localhost:8000/api/ - api main url
- http://localhost:8080/ - the webpack dev server
- http://localhost:8000/workflow/1/ - demo of system we need redone in VueJS


# Project Details
In this project we are merely trying to convert our current workflow system into vuejs.
We would like the new system to look like the current but instead of being integrated into django we
will use the new apis I have created in this project to populate the vusjs interface.

![screenshot step 1 example](https://drive.google.com/open?id=1PsfG4LdY8Is1MJUoltP8c7BFWixW9AUA)
![screenshot step 2 example](https://drive.google.com/open?id=1-734_e9srlO5-oLEwthM3yK2W9c76goO)
