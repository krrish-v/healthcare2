
from flask import Flask, request, render_template, url_for, redirect, jsonify 

from databse import get_in_data_user, user_api, get_key, create_api, token
import block as blk
import databse
import time
from model import get_


try:
    file_log = open('log/web.log', 'r').close()
except:
    file_log = open('log/web.log', 'w').close()

logging.basicConfig(filename="cloud_chain/api_/web.log",
                    format='%(asctime)s %(message)s',
                    filemode='a+') #change the mode to a+ if file is present

logger = logging.getLogger()
logger.info("Started the web API")


async_mode = None

app = Flask(__name__)

def insert_allapi(api):
    insert_ = user_api().insert(str(api))
    return insert_

@app.route('/')
def h():
    return render_template('index.html')


@app.route('/register/patient/firstname=<firstname>,lastname=<lastname>,phone=<phone>,password=<password>,address=<address>,country=<country>,state=<state>,zipcode=<zipcode>')
def register_patient(firstname, lastname, phone, password, address, country, state, zipcode):
    phone = phone
    password = password
    country = country
    state = state
    zipcode = zipcode
    print(firstname, lastname, phone, password, address, country, state, zipcode, token)

    status = True
    date = time.ctime()
    api = create_api().api()
    pub, prv = blk.rsa().keys()
    token = token().get()
    certificate_key = blk.DSA().get_key()
    password = blk.hash384(password) # password is stored in hash form
    
    #insert into database
    in_data = get_in_data_user().insert_patient(str(certificate_key), str(api), str(token), str(password), str(firstname), str(lastname), str(address), str(country), str(state), str(zipcode), str(phone), str(status), str(date))
    ins_key = get_key().insert(str(token), pub, prv) #insert key with token
    ins_api_key = insert_allapi(api)# insert api key all off users and docters

    print(ins_api_key, in_data, ins_key)

    if in_data is True and ins_api_key is True and ins_key is True:
        return jsonify({'api': api, 'token': token, 'private_key': prv, 'certificate': certificate_key})
    else:
        return jsonify({'error': 502})


@app.route('/login/patient/phone=<phone>,password=<password>')
def login_patient(phone, password):
    phone = phone
    password = blk.hash384(password)

    access = get_in_data_user().check_patient_info(str(phone), str(password))
    if access is not False:
        return jsonify(access)
    else:
        return jsonify('error', 'Incorrect login details')


@app.route('/login/doctor/email=<email>,phone=<phone>,password=<password>')
def login_doctor(email, phone, password):
    email = email
    phone = phone
    password = password

    if email == '0': email = None
    
    elif phone == '0': phone = None
    
    access = get_in_data_user().check_doctor_info(password, phone=phone, email=email)
    if access is not False:
        return jsonify(access)
    else:
        return jsonify('error', 'Incorrect login details')

@app.route('/register/doctor/email=<email>,phone=<phone>,password=<password>,firstname=<firstname>,lastname=<lastname>,address=<address>,country=<country>,state=<state>,zipcode=<zipcode>,about=<about>,specialist=<specialist>')
def register_threapist(email, phone, password, firstname, lastname, address, country, state, zipcode, about, specialist):
    email = email
    phone = phone
    password = password
    firstname = firstname
    lastname = lastname
    address = address
    country = country
    state = state
    zipcode = zipcode
    about = about
    specialist = specialist
    print(email, firstname, lastname, phone, password, address, country, state, zipcode, about, specialist)
    
    status = True
    date = time.ctime()
    api = create_api().api()
    pub, prv = blk.rsa().keys()
    token_ = token().get()
    certificate_key = blk.DSA().get_key()
    password = blk.hash384(password) # password is stored in hash form
    
    in_data = get_in_data_user().insert_doctor(str(certificate_key), str(api), str(token_), str(email), str(password), str(firstname), str(lastname), str(address), str(country), str(state), str(zipcode), str(phone), str(about), str(specialist), str(status), str(date))
    ins_key = get_key().insert(str(token_), pub, prv) #insert key with token
    ins_api_key = insert_allapi(api)# insert api key all off users and docters

    print(ins_api_key, in_data, ins_key)

    if in_data is True and ins_api_key is True and ins_key is True:
        return jsonify({'api': api, 'token': token_, 'private_key': prv, 'certificate': certificate_key})
    
    else: return jsonify({'error': 502})


@app.route('/api/ask_publickey/api=<api>,token=<token>')
def other_user_pub_key(api, token):
    chek_api = user_api().check(api)
    if chek_api is True:

        public_key = get_key().get_pub(token)
        if public_key is not None: return jsonify({'status': 200, 'public_key': public_key})
        
        elif public_key is False: return jsonify({'error': 502})
        
        else: return jsonify({'error': 'Incorect token found'})
    
    else: return jsonify({'error': 'Incorrect api found'})


@app.route('/chat/symptoms=<symptomslist>') #symptioms should be like 0,1,0,0,0,1,0........
def sym_deis(symptomslist):
    pridict_data = get_().pridict(symptomslist)[0]
    if pridict_data is not None:
        return jsonify({'pridicted data': str(pridict_data)})
    
    else: return jsonify({'error': 'passed data in a wwrong way'})


if __name__ == '__main__':
   app.run(host= '127.0.0.1', port=9278, debug=True)

