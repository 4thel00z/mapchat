from flask import Flask
from flask import make_response
import request

class Server:
    app = Flask(__name__)
    
    @app.route('post/', methods=[GET])
    def start(self,host):
        self.host = 'localhost:8080'
        return('page') 

    def shutdown(error):
        return make_response({'error': 'Service unavailable'}, 503)

if __name__ == '__main__':
    app.run(debug=True)
