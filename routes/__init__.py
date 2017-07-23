from flask_restplus import Api
from .routes import api as token

api = Api(
    title='Musica Token API',
    version='1.0'
)

api.add_namespace(token)