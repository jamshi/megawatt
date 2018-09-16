# Code Challenge

Please see the solution code. The major highlight of this challenge the aggregation part is implemented in django custom model manager as per the django standard.
Custom model manager code is in `core/managers.py` file.

#### Project Dependency
    - Python 3+
    - Django 2+

#### Steps to run solution


    - pip install -r requirements.txt
    - python manage.py migrate
    - # Load dumped data to database
    - python manage.py loaddata core/fixtures/fixtures.json
    - python manage.py runserver
    
#### Step to run test suite

    - python manage.py test
