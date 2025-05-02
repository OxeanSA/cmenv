from flask import Flask, render_template
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

app = Flask(__name__)

# two decorators, same function
@app.route('/')
def index():
    return render_template('index.html', the_title='Oxean-SA Home')

if __name__ == '__main__':
    # Add SSL options
    ssl_options = {
        "certfile": "./osacs/static/certs/certificate.crt",
        "keyfile": "./osacs/static/certs/private.key"
    }
    server = HTTPServer(WSGIContainer(app), ssl_options=ssl_options)

    server.listen(port=5000)
    IOLoop.instance().start()
