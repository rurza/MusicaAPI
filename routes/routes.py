from flask_restplus import Resource, Namespace, fields, abort
from music_token import create_token
import json

api = Namespace('token')

token = api.model('Token', {
	'expiration_date': fields.DateTime(),
	'token': fields.String()
})

parser = api.parser()
parser.add_argument('Authentication', type=str, required=True, help='Authentication key', location='headers')
with open('config.json') as data_file:
	json_data = json.load(data_file)
authentication_key = json_data['authentication_key']

@api.route('/')
@api.response(501, 'Unauthrozied')
@api.response(201, 'Token created')
class Token(Resource):
	@api.marshal_with(token)
	@api.doc(parser=parser)
	def get(self):
		args = parser.parse_args()
		if args['Authentication'] == authentication_key:
			return create_token(), 201
		else:
			abort(501, 'Wrong Authentication key')
			
	    