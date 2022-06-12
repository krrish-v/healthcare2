
import hashlib
import ecdsa
from ecdsa import SECP256k1
import rsa as RSA
from databse import get_key


# convert to hexfily
def hexlf(msg):
    return binascii.hexlify(msg)

# base decode function
def encoded_data(msg):
    return base64.b85encode(msg)

class rsa:
    def keys(self):
        public, private = RSA.newkeys(2048)
        return str(public), str(private)

    def loadkey(self, token):
        pub, prv = self.keys()
        load = get_key().insert(token, pub, prv)
        return load
        

class DSA():

    def get_key(self):
        self.sk = ecdsa.SigningKey.generate(curve=ecdsa.BRAINPOOLP384r1, hashfunc=hashlib.sha3_384)
        self.vk_ = self.sk.get_verifying_key()
        self.private_key = self.sk.to_string().hex()
        return self.private_key

    def create_signture(self, privatekey, message: bytes):
        self.sk = ecdsa.SigningKey(_error__please_use_generate=True).from_string(bytes.fromhex(privatekey), curve=ecdsa.BRAINPOOLP384r1, hashfunc=hashlib.sha3_384)
        sig_ = self.sk.sign(hashlib.sha3_256(message).hexdigest().encode())
        sig = bytes.hex(sig_)
        public_key = bytes.hex(self.sk.get_verifying_key().to_string())
        return sig, message, public_key


class verf_DSA():
    def verify_signature(self, signature : bytes, message: bytes, public_key):
        vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(public_key), curve=ecdsa.BRAINPOOLP384r1, hashfunc=hashlib.sha3_384) # the default is sha1
        verify = vk.verify(bytes.fromhex(signature), hashlib.sha3_256(message).hexdigest().encode()) # True
        return verify

def hash384(message):
    return hashlib.sha3_384(message.encode()).hexdigest()

def hash256(message):
    return hashlib.sha3_256(message.encode()).hexdigest()


'''
c = DSA()
k = c.get_key()
print(k)
signat = c.create_signture(k, message=b'hii')
print(signat)
print(verf_DSA().verify_signature(signat[0], signat[1], signat[2]))

print(rsa().loadkey('qsfjgthfb34uifg34tr387fgvwu'))
print(get_key().get_pub('qsfjgthfb34uifg34tr387fgvwu'))

'''
