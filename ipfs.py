import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	output = json.dumps(data)
	files = {
		'file': output
	}
	response = requests.post('https://ipfs.infura.io:5001/api/v0/add', files=files, auth=('2AUFQZb3zJvb5wfKG0rF0PyAqRS','7c2302ec2af25ed8b95bd8e796304126'))
	#print(response.text)
	return response.json().get('Hash')

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	params = (
		('arg', cid),
	)
	response = requests.post('https://ipfs.infura.io:5001/api/v0/cat', params=params, auth=('2AUFQZb3zJvb5wfKG0rF0PyAqRS','7c2302ec2af25ed8b95bd8e796304126'))
	#print(response.text)
	data = json.loads(response.text)
	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data

