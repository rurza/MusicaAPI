import datetime
import jwt
import json

alg = 'ES256'

def create_token():
	
	with open('config.json') as data_file:
	    json_data = json.load(data_file)
	secret = '\n'.join(['-----BEGIN PRIVATE KEY-----', json_data['key'], '-----END PRIVATE KEY-----'])
	key_id = json_data['key_id']
	team_id = json_data['team_id']
	
	assert(len(secret) > 0)
	assert(len(key_id) > 0)
	assert(len(team_id) > 0)
	
	time_now = datetime.datetime.now()
	time_expired = datetime.datetime.now() + datetime.timedelta(hours=720)

	headers = {
		'alg': alg,
		'kid': key_id
	}

	payload = {
		'iss': team_id,
		'exp': int(time_expired.strftime("%s")),
		'iat': int(time_now.strftime("%s"))
	}
	
	token = jwt.encode(payload, secret, algorithm=alg, headers=headers)
	date = time_expired
	print "curl -v -H 'Authorization: Bearer %s' \"https://api.music.apple.com/v1/catalog/us/artists/36954\" " % (token)
	return {'token': token, 'expiration_date': time_expired}
	


