# Django API Frontend Example

A small proof-of-concept that leverages Django and DRF to render HTML templates by default and API like responses when requested.

Create a virtualenv and install the requirements:
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Set up Django:
```
python manage.py migrate
```

Put some data to show into the database:
```
python manage.py shell
>>> from custom_renderer.models import Data
>>> d = Data(content="This is content")
>>> d.save()
>>> d2 = Data(content="This is also content")
>>> d2.save()
```

Run the server:
```
python manage.py runserver
```

... and navigate to [http://localhost:8000/](http://localhost:8000/) to look at the data in a rendered HTML template.

Alternatively query the data as a JSON like this:
```
curl -H "Accept: application/json" http://localhost:8000/
```
