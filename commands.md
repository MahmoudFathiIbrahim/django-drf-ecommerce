##This command to create or update the schema file:    
    python manage.py spectacular --file schema.yml
##To Run pytest coverage to show the missed tests
    pytest --cov
##pytest flag -s give us more info
    pytest -s