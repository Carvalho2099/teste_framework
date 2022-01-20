from flask import Flask
from flask_restful import Api
from resources.todo import Todos
from resources.token import Token
from flask_jwt_extended import JWTManager
import logging

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = '244466666'
app.config['SWAGGER'] = {"title": "Swagger teste", "uiversion": 1}
api = Api(app)
jwt = JWTManager(app)


api.add_resource(Todos, '/todos')
api.add_resource(Token, '/token')

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(message)s',
        filename='./log/todo.log'
    )
    app.run(debug=True)
