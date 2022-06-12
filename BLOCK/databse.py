
import sqlite3
import random
import binascii
#import block as blk

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
    def __init__(self):
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
        self.conn_ = sqlite3.connect('BLOCK/database/keys.db')

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


class get_in_data():
    def __init__(self):
        self.conn_ = sqlite3.connect('BLOCK/database/data.db')

    def insert(self, token, password, firstname, lastname, address, country, state, zip_code, phone_no, status, date): #random_verifying_code
        if 1==1:#try:
            cursor = self.conn_.cursor()
            
            #cursor.execute(
            #    'create table health_concern (token text not null, password text not null, firstname text not null, lastname text not null, address text not null, country text not null, state text not null, zip_code text not null, phone_no text not null, status text not null, date text not null)'
            #)

            cursor.execute(
                "insert into health_concern values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                (token, password, firstname, lastname, address, country, state, zip_code, phone_no, status, date)
            )
            self.conn_.commit()
            self.conn_.close()
            return True
        
        #except: return False

    def load(self):
        try:
            cursor = self.conn_.cursor()
            cursor.execute("select * from health_concern")
            data = cursor.fetchall()
            self.conn_.close()
            if len(data) != 0:
                return data
            
            else: return False

        except: return None

        
    def update(self, phone_no, field, new_value):
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

class user_api():
    def __init__(self):
        self.conn_ = sqlite3.connect('BLOCK/database/api.db')

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
#print(get_in_data().insert('rfewfcesv32rdwffw32d', password, 'harry', 'poter', 'New Delhi Sector 4', 'India', 'New Delhi', '7353', '99999999999', True, str(tmt)))
#print(get_in_data().load())

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
