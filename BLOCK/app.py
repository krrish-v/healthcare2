
from flask import Flask, request, render_template, url_for, redirect, jsonify
from flask_socketio import SocketIO, join_room
from databse import get_in_data, user_api, get_key, create_api
import block as blk
import databse
import time
from model import get_

'''
try:
    file_log = open('log/web.log', 'r').close()
except:
    file_log = open('log/web.log', 'w').close()

logging.basicConfig(filename="cloud_chain/api_/web.log",
                    format='%(asctime)s %(message)s',
                    filemode='a+') #change the mode to a+ if file is present

logger = logging.getLogger()
logger.info("Started the web API")

'''

app = Flask(__name__)
sock = SocketIO(app)

@app.route('/register/phone_no=<phone>,password=<password>,country=<country>,state=<state>,zipcode=<zipcode>')
def register(phone, password, country, state, zipcode):
    phone = phone
    password = password
    country = country
    state = state
    zipcode = zipcode
    token = databse.token()
    if phone and password and country and state and zipcode == '':
        return jsonify({'error': 'Incomplete detail'})
    else:
        status = True
        date = time.ctime()
        api = create_api().api()
        ins_api_key = databse.user_api().insert(api)
        in_data = get_in_data.insert(token, password, firstname, lastname, address, country, state, zip_code, phone_no, status, date)
        
        if in_data is True and ins_api_key is True:
            return jsonify({'api': api_key})
        else:
            return jsonify({'error': 502})


@app.route('/api/ask_publickey?api=<api>,token=<token>')
def other_user_pub_key(api, token):
    chek_api = user_api().check(api)
    if chek_api is True:

        public_key = get_key().get_pub(token)
        if public_key is not None: return jsonify({'status': 200, 'public_key': public_key})
        
        elif public_key is False: return jsonify()
        
        else: return jsonify()
    else:
        return jsonify()

@app.route('/chat/symptoms=<symptoms_list>') #symptioms should be like 0,1,0,0,0,1,0........
def sym_deis(symptoms):
    return get_().pridict(symptoms)
