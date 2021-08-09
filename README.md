# RestAPI
A simple REST API service serving the capitals and areas of
countries.

### Usage
The API service can be utilized by following the protocol

##### Get the list of countries, their capitals and total area
```
/countries
``` 

##### Get the capital and total area of a specific country using an index
```
/countries/<index_no>
```

##### Get the capital of a requested country
```
/countries/<index_no>/capital
```

##### Get the total area of a requested country
```
/countries/<index_no>/area
```

##### FOR DEBUG: Use /echo as a prefix to echo information of the requestor
For example:
```
echo/countries/20/area
```

### Installing the Dependencies
Using pip, install the required dependencies from `~/requirements.txt`
```
pip install -r requirements.txt
```

### Running the Application
1. Export the required environment variables. (Here we are 
exposing port 9532)
```
export FLASK_APP=restapi/app
export FLASK_RUN_PORT=9532 
``` 

2. Start the flask application from the root of the repository
```
flask run
```

### Running the Integration Tests
1. Start the application by following the above mentioned 
procedure. 

2. Run the integration tests using the command (from the root
of the repository)
```
python3 -m pytest tests/api_integration_test.py
```

