Kalia - Masters Degree and Job Recommendation System

DEV SETUP
  1) pull the repo
  2) Install virtualenv https://virtualenv.pypa.io/en/stable/userguide/
  3) Run the following
      ```
      $ virtualenv <your-env-foldername>
      $ source <your-env-foldername>/bin/activate
      (<env-foldername>) $ pip install -r requirements.txt
      $ pip install sqlalchemy
      ```
  4) run ```python app.py``` to startup local server, needs to be restarted after each change


*If you get the error "port already in use" use ```lsof -i:5000``` to get the PID then ```kill -9 <PID>```
