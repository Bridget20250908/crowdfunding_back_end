release: python crowdfunding/crowdfunding/manage.py migrate
web: gunicorn --pythonpath crowdfunding/crowdfunding crowdfunding.wsgi --log-file -