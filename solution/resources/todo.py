import requests
from flask_restful import Resource
from flask_jwt_extended import jwt_required
import logging

url = 'https://jsonplaceholder.typicode.com/todos'


class Todos(Resource):

    @jwt_required()
    def get(self):
        self.log = logging.getLogger()
        try:
            response = requests.get(url)
            if 200 <= response.status_code <= 299:
                lista_retorno = response.json()[:5]
                aux = {}
                retorno = []
                for todo in lista_retorno:
                    aux['id'] = todo['id']
                    aux['title'] = todo['title']
                    retorno.append(aux.copy())
                self.log.info(f'RAW: {response.raw} - STATUS_CODE: {response.status_code}')
                return retorno, response.status_code
            else:
                self.log.info(f'{response.raw} - {response.status_code}')
                return {'error': {'Reason': response.reason}}, response.status_code
        except:
            self.log.error(f'INTERNAL SERVER ERROR 500')
            return {'error': {'Reason': 'INTERNAL SERVER ERROR'}}, 500
