
# genify-assign-recommender-sys



## Description
This is assignment is assigned by Genify. It requires a REST API around a machine learning model that recommends banking products.

## Estimated Time to complete the assessment:
4 to 5 hrs. This is because this was my first encounter with ML models.

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
### Manually
    git clone https://github.com/mohamedashraftaha/genify-assign-recommender-sys.git
    source venv/bin/activate
    pip3 install -r requirements.txt
    python3 app.py


### Using the API hosted on Heroku

### Docker Container 
#### Build
    docker build --tag python-docker .
#### Run
    docker run python-docker 



## Example Queries (Also attached in the report)
### Example 1
#### (Query)
    Query:
    curl -X 'POST' \
    'http://10.40.60.52:5000/recommend' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
    "age": "26",
    "gender": "MALE",
    "nationality": "GERMANY",
    "seniority": "240",
    "relationship_type": "ACTIVE",
    "activity_level": "ACTIVE",
    "segment": "INDIVIDUAL",
    "income": "3023.4"
    }'
----

#### (Response)
    Response: 
    {
      "msg": "Recommendations for user generated successfully",
      "response_data": {
        "Recommended Products": [
          "Current Accounts",
          "Direct Debit",
          "Pensions",
          "Payroll Account",
          "Payroll",
          "Credit Card",
          "E-Account"
        ]
      },
      "status": "Success"
    }
---
### Screenshot
![image](https://user-images.githubusercontent.com/75078872/167313682-785caac0-930a-4962-bace-6159a33a14ac.png)

---
### Example 2
#### (Query)
    Query:
    curl -X 'POST' \
      'http://10.40.60.52:5000/recommend' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
      "age": "65",
      "gender": "FEMALE",
      "nationality": "EGYPT",
      "seniority": "500",
      "relationship_type": "ACTIVE",
      "activity_level": "INACTIVE",
      "segment": "INDIVIDUAL",
      "income": "203.4"
    }'
----

#### (Response)
    Response: 
    {
      "msg": "Recommendations for user generated successfully",
      "response_data": {
        "Recommended Products": [
          "Current Accounts",
          "Credit Card",
          "Direct Debit",
          "Pensions",
          "E-Account",
          "Particular Account",
          "Payroll Account"
        ]
      },
      "status": "Success"
    }
---
### Screenshot
![image](https://user-images.githubusercontent.com/75078872/167313889-41ce551d-3bbb-4885-a478-9f5ddd4b0082.png)
---
### Example 3
#### (Query)
    Query:
    curl -X 'POST' \
      'http://10.40.60.52:5000/recommend' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
      "age": "16",
      "gender": "MALE",
      "nationality": "FRANCE",
      "seniority": "150",
      "relationship_type": "INACTIVE",
      "activity_level": "INACTIVE",
      "segment": "UNIVERSITY",
      "income": "140"
}'
----

#### (Response)
    Response: 
    {
      "msg": "Recommendations for user generated successfully",
      "response_data": {
        "Recommended Products": [
          "Current Accounts",
          "Particular Account",
          "Direct Debit",
          "Payroll Account",
          "Junior Account",
          "E-Account",
          "Pensions"
        ]
      },
      "status": "Success"
    }
---
### Screenshot
![image](https://user-images.githubusercontent.com/75078872/167313919-df2f9672-1cfd-4400-be59-5e0d56065ce3.png)
---
### Example 4 (Validation: Missing data -> Gender)
#### (Query)
    Query:
    curl -X 'POST' \
      'http://10.40.60.52:5000/recommend' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
      "age": "16",
      "nationality": "FRANCE",
      "seniority": "150",
      "relationship_type": "INACTIVE",
      "activity_level": "INACTIVE",
      "segment": "UNIVERSITY",
      "income": "140"
    }'
----

#### (Response)
    Response: 
    {
      "msg": "Missing field",
      "response_data": null,
      "status": "Failed"
    }
---
### Screenshot
![image](https://user-images.githubusercontent.com/75078872/167314052-1508fab4-7c49-41f1-9658-129d8c371d0d.png)
## Demo Video Link uploaded on google drive

