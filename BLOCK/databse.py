
import sqlite3
import random
import binascii
from hmac import compare_digest
import block as blk

class create_api():
    def api(self):
        random_string = ''
 
        for _ in range(64):
            # Considering only upper and lowercase letters
            random_integer = random.randint(97, 97 + 26 - 1)
            flip_bit = random.randint(0, 1)
            # Convert to lowercase if the flip bit is on
            random_integer = random_integer - 32 if flip_bit == 1 else random_integer
            # Keep appending random characters using chr(x)
            random_string += (chr(random_integer))
        
        return blk.hash256(random_string)

class token():
    def get(self):
        random_string = ''
 
        for _ in range(64):
            # Considering only upper and lowercase letters
            random_integer = random.randint(97, 97 + 26 - 1)
            flip_bit = random.randint(0, 1)
            # Convert to lowercase if the flip bit is on
            random_integer = random_integer - 32 if flip_bit == 1 else random_integer
            # Keep appending random characters using chr(x)
            random_string += (chr(random_integer))
        
        return blk.hash256(random_string)

class get_key():
    def __init__(self):
        self.conn_ = sqlite3.connect('backend/BLOCK/database/keys.db')

    def insert(self, token, pub, priv):
        try:
            cursor = self.conn_.cursor()
            #cursor.execute(
            #    'create table user_keys (token text not null, pub text not null, priv text not null)'
            #)

            cursor.execute(
                "insert into user_keys values(?, ?, ?)", 
                (token, pub, priv)
            )
            self.conn_.commit()
            self.conn_.close()
            return True
        except: return False

    def get_pub(self, token):
        try:
            cursor = self.conn_.cursor()
            cursor.execute("select * from user_keys where token = (?)", (token, ))
            data = cursor.fetchall()
            self.conn_.close()
            
            if len(data) != 0:
                return data[0][1]

            else: return None
        
        except: return False

class get_in_data_user():
    def __init__(self):
        self.conn_ = sqlite3.connect('backend/BLOCK/database/data_user.db')

    def insert_patient(self, dsakey, api, token, password, firstname, lastname, address, country, state, zip_code, phone_no, status, date): #random_verifying_code
        try:
            cursor = self.conn_.cursor()
            
            #cursor.execute(
            #    'create table hc_patient (dsakey text not null, api text not null, token text not null, password text not null, firstname text not null, lastname text not null, address text not null, country text not null, state text not null, zip_code text not null, phone_no text not null, status text not null, date text not null)'
            #)

            cursor.execute(
                "insert into hc_patient values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                (dsakey, api, token, password, firstname, lastname, address, country, state, zip_code, phone_no, status, date)
            )
            self.conn_.commit()
            self.conn_.close()
            return True
        
        except: return False

    def check_patient_info(self, phone, passwd):
        try:
            cursor = self.conn_.cursor()
            com = "select * from hc_patient where phone_no = " + phone
            cursor.execute(com)
            data = cursor.fetchall()
            self.conn_.close()
            
            if len(data) != 0:
                data = data[0]
                old_passwd = data[3]
            
                if self.validate(passwd, old_passwd) is True:
                    return {
                        'dsakey': data[0],
                        'api': data[1],
                        'token': data[2],
                        'name' : data[4] + ' ' + data[5]
                    }

            
            else: return False

        except: return False
    
    def update_patient(self, phone_no, field, new_value):
        """
        update selected field
        :return: True|False
        """
        try:
            sql = "UPDATE health_concern SET " + field + "=" + new_value + " WHERE phone_no = " + phone_no
            print(sql)
            cursor = self.conn_.cursor()
            cursor.execute(sql)
            self.conn_.commit()
            self.conn_.close()
            return True

        except: return False
    
    def insert_doctor(self, dsakey, api, token, email, password, firstname, lastname, address, country, state, zip_code, phone_no, about, specialist_in, status, date): #random_verifying_code
        try:
            cursor = self.conn_.cursor()
            
            #cursor.execute(
            #    'create table hc_doctor (dsakey text not null, api text not null, token text not null, email text not null, password text not null, firstname text not null, lastname text not null, address text not null, country text not null, state text not null, zip_code text not null, phone_no text not null , about text not null, specialist_in text not null, status text not null, date text not null)'
            #)

            cursor.execute(
                "insert into hc_doctor values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                (dsakey, api, token, email, password, firstname, lastname, address, country, state, zip_code, phone_no, about, specialist_in, status, date)
            )
            self.conn_.commit()
            self.conn_.close()
            return True
        
        except: return False

    def get_doctor(self):
        try:
            cursor = self.conn_.cursor()
            cursor.execute('select token, firstname, lastname, country, specialist_in, about from hc_doctor')
            data = cursor.fetchall()
            self.conn_.close()

            if len(data) != 0:
                all_therapist = {}
                for i in data:
                    tokn = i[0]
                    user = {tokn: {
                        'name': i[1]+' '+i[2],
                        'country': i[3],
                        'specialist': i[4],
                        'about': i[5]
                    }}
                    all_therapist.update(user)
                return all_therapist

        except:
            return False

    def check_doctor_info(self, passwd, email=None, phone=None):
        if email is None: com = "select * from hc_doctor where phone_no = " + phone
        
        elif phone is None: com = "select * from hc_doctor where email = '" + email + "'"
        
        else: com = ""
        
        try:
            cursor = self.conn_.cursor()
            cursor.execute(com)
            data = cursor.fetchall()
            self.conn_.close()

            if len(data) != 0:
                data = data[0]
                old_passwd = data[4]
            
                if self.validate(passwd, old_passwd) is True:
                    return {
                        'dsakey': data[0],
                        'api': data[1],
                        'token': data[2],
                        'name' : data[5] + ' ' + data[6],
                        'specialist': data[13]
                    }

            
            else: return False

        except: return False

    def validate(self, passwd, old_passwd):
        return compare_digest(passwd, old_passwd)


class user_api():
    def __init__(self):
        self.conn_ = sqlite3.connect('backend/BLOCK/database/api.db')

    def insert(self, api): #random_verifying_code
        try:
            cursor = self.conn_.cursor()
            
            #cursor.execute(
            #    'create table api_table (api text not null)'
            #)

            cursor.execute(
                "insert into api_table values(?)", 
                (api,)
            )
            self.conn_.commit()
            self.conn_.close()
            return True
        
        except: return False

    def check(self, api):
        try:
            cursor = self.conn_.cursor()
            cursor.execute("select * from api_table where api = (?)", (api,))
            data = cursor.fetchall()
            self.conn_.close()
            if len(data) != 0:
                return True
            
            else: return False

        except: return None


#import time
#tmt = time.ctime()
#password = blk.hash384('fdewf23c')

#print(get_in_data_user().insert_doctor('ewfr3283iuqw38r 2iugewhcvefir32fywejhf3r2ifyejh', 'retrdfvdsfbnythtgrferht', 'rfewfcesv32rdwffw32d', 'harry@gmail.com', password, 'harry', 'poter', 'New Delhi Sector 4', 'India', 'New Delhi', '7353', '99999999999', 'i have 2 year of experience', 'mental_health', True, str(tmt)))
#print(get_in_data_user().load_doctor())

#print(get_in_data_user().get_doctor())
#print(get_in_data_user().insert_patient('hvfyu23qwhjvcf3rg2uifekig2 fevwhfbcuduiejhi4ew', 'ehf78iu4378irewvhcig4f', 'rfewfcesv32rdwffw32d', password, 'harry', 'poter', 'New Delhi Sector 4', 'India', 'New Delhi', '7353', '99999999999', True, str(tmt)))
#print(get_in_data_user().load_patient())

#print(get_in_data_user().check_patient_info('99999999999', '8cfbace8e8c053bc56d00f97a8bb029db8b4bdae71cf31bca0b7b1ea84fdc7761f126ce3e8c014083bab43be9dec42a2'))
#print(get_in_data_user().check_doctor_info('8cfbace8e8c053bc56d00f97a8bb029db8b4bdae71cf31bca0b7b1ea84fdc7761f126ce3e8c014083bab43be9dec42a2', email='harry@gmail.com'))
#import time
#tmt = time.ctime()
#print(get_in_data().update("123","api","100"))
#print(get_in_data().load())

#ap = create_api().api()
#q = user_api().insert(ap)
#print(q)
#print(ap)
#t = user_api().check(ap)
#print(t)
