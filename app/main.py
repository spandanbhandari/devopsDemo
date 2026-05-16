from flask import Flask
from prometheus_client import make_wsgi_app, Counter
from werkzeug.middleware.dispatcher import DispatcherMiddleware

app = Flask(__name__)
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

REQUESTS = Counter('http_requests_total', 'Total HTTP Requests')

@app.route('/')
def hello():
    REQUESTS.inc()
    return "Hello, DevOps World! CI/CD with GitHub Actions is working. "

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
