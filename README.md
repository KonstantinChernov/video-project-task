# Demo My-Videos Project

### local dev setup

1) clone repo

```
git clone https://github.com/KonstantinChernov/test-task-milk.git
cd test-task-milk
```

2) make virtual env and activate it

```
python3 -m venv venv
source venv/bin/activate
```

3) install python requirements

```
pip install -r requirements.txt
```

4) start django dev server, again in its own terminal window with the python virtual env from step 3 activated and in the same directory as the manage.py script

```
(venv) python manage.py runserver
```

Once these are complete you should be able to point your browser to http://localhost:8000 and see the Thumbnailer application
