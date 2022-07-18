from flask import Flask, request, jsonify
from flask_restful import Api
from eth_account.messages import encode_defunct
import json
import eth_account
import algosdk

app = Flask(__name__)
api = Api(app)
app.url_map.strict_slashes = False

@app.route('/verify', methods=['GET','POST'])
def verify():
    content = request.get_json(silent=True)
    #Check if signature is valid
    result = False #Should only be true if signature validates
    if content['payload']['platform'] == 'Ethereum':
        signable_message = encode_defunct(text=json.dumps(content['payload']))
        if eth_account.Account.recover_message(signable_message, signature=content['sig']) == content['payload']['pk']:
            result = True
    elif content['payload']['platform'] == 'Algorand':
        if algosdk.util.verify_bytes(json.dumps(content['payload']).encode('utf-8'),content['sig'],content['payload']['pk']):
            result = True
    return jsonify(result)

if __name__ == '__main__':
    app.run(port='5002')
