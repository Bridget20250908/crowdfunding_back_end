release: python app/crowdfunding/manage.py migrate
web: gunicorn --pythonpath crowdfunding crowdfunding.wsgi --log-file -