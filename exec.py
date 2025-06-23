import os
import sys
#  django-admin startapp img
if __name__ == "__main__":
    cmd = "python manage.py runserver 127.0.0.1:8000"
    print(cmd)
    os.system(cmd)