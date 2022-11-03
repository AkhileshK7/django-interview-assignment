Built on  python 3.10.7.

Setup on local host:

- Clone the repository to your local system
- Open terminal or cmd in the eLibrary folder
- Install the requirements using

```python -m pip install -r requirements.txt```

- Make migrations for the API and migrate using

```
python manage.py makemigrations
python manage.py migrate
```

- Start server using

``` python manage.py runserver```

The project will be hosted on the local server
``` http://127.0.0.1:8000/```

Find the documentation at ```http://127.0.0.1:8000/schema/swagger-ui```
