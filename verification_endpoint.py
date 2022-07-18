from flask import Flask, request, jsonify
from flask_restful import Api
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
        print('dump', json.dumps(content['payload']))
        print('signature', content['sig'])
        print('res', eth_account.Account.recover_message(json.dumps(content['payload']),signature=content['sig']))
        result = (eth_account.Account.recover_message(json.dumps(content['payload']),signature=content['sig'].hex()) == content['payload']['pk'])
    elif content['payload']['platform'] == 'Algorand':
        result = algosdk.util.verify_bytes(json.dumps(content['payload']).encode('utf-8'),content['sig'],content['payload']['pk'])
    return jsonify(result)

if __name__ == '__main__':
    app.run(port='5002')
