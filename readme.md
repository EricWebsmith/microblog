 This is a learning project, URL:
 [https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vii-error-handling](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vii-error-handling)

 # Versions
 Python 3.10.6 \
Flask 2.2.2 \
Werkzeug 2.2.2
 # Changes

 debug mode:
 ```bash
 export FLASK_DEBUG=1
 ```

 # email server

 ```bash
 python -m smtpd -n -c DebuggingServer localhost:8025
 ```

 # translate
init
```bash
pybabel init -i messages.pot -d app/translations -l es
```

compile
```bash
pybabel compile -d app/translations
```

update
```bash
pybabel extract -F babel.cfg -k _l -o messages.pot .
pybabel update -i messages.pot -d app/translations
```
