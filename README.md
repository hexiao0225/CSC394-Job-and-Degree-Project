# Kalia
### Masters Degree and Job Recommendation System :+1:

##### DEV SETUP
  1. Pull the repo
  2. Install virtualenv https://virtualenv.pypa.io/en/stable/userguide/
  3. Run the following
      ```
      $ virtualenv venv
      $ source venv/bin/activate
      $ pip install -r requirements.txt
      ```
  4. Run ```python app.py``` to startup local server

*Virtual environment should be named venv, or name it what you want and add it to the .gitignore file
*If you get the error "port already in use" use ```lsof -i:5000``` to get the PID then ```kill -9 <PID>```
