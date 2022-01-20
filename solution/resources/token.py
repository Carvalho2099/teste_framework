from flask_restful import Resource
from flask_jwt_extended import create_access_token
import logging


class Token(Resource):
    def __init__(self):
        self.log = logging.getLogger()

    @classmethod
    def get(cls):
        cls.log = logging.getLogger(__name__)
        try:
            logging.info('RAW: - STATUS_CODE: 200')
            token_acesso = create_access_token(identity=True)
            return token_acesso, 200
        except:
            logging.error(f'INTERNAL SERVER ERROR 500')
            return {'error': {'Reason': 'INTERNAL SERVER ERROR'}}, 500
