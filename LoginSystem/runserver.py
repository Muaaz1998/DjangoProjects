import os

def runserver():
    os.environ['DJANGO_RUNSERVER_URL'] = 'http://127.0.0.1:8000/login'
    os.system('python manage.py runserver')

if __name__ == '__main__':
    runserver()