# Machine Learning Server 

How to try it?

- Run curl -X POST -F 'csv_file=iris.csv' 'http://localhost:5000/create?target=Species'
- Run curl -X POST -F 'input_line=5.1,3.5,1.4,0.2' 'http://localhost:5000/predict'

How to test?

- Run pytest -q test_api.py
