# flask-sse-poc
A demo using SSE to create an event stream from a flask application

To get started, run pip install

```sh
pip install -r requirements.txt
```

And start an instance of Redis. If you have Docker installed, you can start a local Redis server with:

``` sh
docker run --name redis-sse -p 6379:6379 -d redis
```

Next, start up the main web server:

```sh
gunicorn run:app --worker-class gevent --bind 127.0.0.1:5000
```
or
```
python run.py
```

In terminal windows start the event emitter.

```sh
python events.py
```

And listen the event open the browser and hit with this url

```sh
http://127.0.0.1:5000/stream/<transcript_id>
```

## Reference

[Link](https://flask-sse.readthedocs.io/en/latest/)
