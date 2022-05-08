
# genify-assign-recommender-sys

## Description
This is assignment is assigned by Genify. It requires a REST API around a machine learning model that recommends banking products.


## Software Requirements
* Python3
* Flask
* Git
* OpenAPI specification "Swagger" for documentation
* Heroku for hosting
* numpy 
* pandas 
* xgboost
* sklearn 

## Important Additions "In model.py"
    print("Saving the model..")
    joblib.dump(model,'model.pkl')
    recommend = joblib.load('model.pkl')


## To use the API
* Manually
   - git clone https://github.com/mohamedashraftaha/genify-assign-recommender-sys.git

   - source venv/bin/activate
   - pip3 install -r requirements.txt
   - python3 app.py


* Using the API hosted on Heroku
