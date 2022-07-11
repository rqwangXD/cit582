from web3 import Web3
from web3.contract import Contract
from web3.providers.rpc import HTTPProvider
import requests
import json
import time

bayc_address = "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D"
contract_address = Web3.toChecksumAddress(bayc_address)

#You will need the ABI to connect to the contract
#The file 'abi.json' has the ABI for the bored ape contract
#In general, you can get contract ABIs from etherscan
#https://api.etherscan.io/api?module=contract&action=getabi&address=0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D
with open('/home/codio/workspace/abi.json', 'r') as f:
	abi = json.load(f) 

############################
#Connect to an Ethereum node
api_url = f"https://mainnet.infura.io/v3/8c6e4512e14b41dd9c9834718bc487a0"
provider = HTTPProvider(api_url)
web3 = Web3(provider)
assert web3.isConnected(), f"Failed to connect to provider at {api_url}"

def query_ipfs(appID):
	response = requests.post(f'https://ipfs.infura.io:5001/api/v0/cat?arg=QmeSjSinHpPnmXmspMjwiXyN6zS4E9zccariGR3jxcaWtq/{appID}', auth=('2AUFQZb3zJvb5wfKG0rF0PyAqRS','7c2302ec2af25ed8b95bd8e796304126'))
	#print(response.text)
	data = json.loads(response.text)
	return data

def get_ape_info(apeID):
	assert isinstance(apeID,int), f"{apeID} is not an int"
	assert 1 <= apeID, f"{apeID} must be at least 1"

	data = {'owner': "", 'image': "", 'eyes': "" }

	contract = web3.eth.contract(address=contract_address, abi=abi)
	data['owner'] = contract.functions.ownerOf(apeID).call()
	ipfs_res = query_ipfs(apeID)
	data['image'] = ipfs_res['image']
	for pair in ipfs_res['attributes']:
		if pair['trait_type'] == 'Eyes':
			data['eyes'] = pair['value']
			break

	assert isinstance(data,dict), f'get_ape_info{apeID} should return a dict' 
	assert all( [a in data.keys() for a in ['owner','image','eyes']] ), f"return value should include the keys 'owner','image' and 'eyes'"
	return data