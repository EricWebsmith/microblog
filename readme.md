 This is a learning project, URL:
 [https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vii-error-handling](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vii-error-handling)

 https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vii-error-handling

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

# docker

```bash
docker build -t microblog:latest .
```

# elasticsearch

```
docker pull docker.elastic.co/elasticsearch/elasticsearch:8.5.2

$ docker run -d --name elasticsearch --memory="200m" -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch:8.5.2
```