TODO
  - Results page needs to be either a separate html page or we need to async load data with angular
  - Cache user answers in cookie / POST to URL

QUESTIONS
  - Hardcode or dynamically load questions?
  - How are keywords assigned to answers?  

DEV SETUP
  1) pull the repo
  2) Create and activate a python virtual environment https://virtualenv.pypa.io/en/stable/userguide/
<<<<<<< HEAD
=======
      $ virtualenv myenv
      $ source myenv/bin/activate
      (myenv) $ pip install flask_sqlalchemy
      $pip install sqlalchemy
>>>>>>> c6c79b1648a4c7cc1910dd6113e23d296b8a877c
  3) run the command ```pip install -r requirements.txt```
  4) run ```python app.py``` to startup local server, needs to be restarted after each change


*If you get the error "port already in use" use ```lsof -i:5000``` to get the PID then ```kill -9 <PID>```
<<<<<<< HEAD
=======




>>>>>>> c6c79b1648a4c7cc1910dd6113e23d296b8a877c
