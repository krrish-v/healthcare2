
import hashlib
import ecdsa
import rsa as RSA


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


class DSA:
    def get_key(self):
        self.sk = ecdsa.SigningKey.generate(curve=ecdsa.BRAINPOOLP384r1, hashfunc=hashlib.sha3_384)
        self.vk_ = self.sk.get_verifying_key()
        self.private_key = self.sk.to_string().hex()
        return self.private_key


def hash384(message):
    return hashlib.sha3_384(message.encode()).hexdigest()

def hash256(message):
    return hashlib.sha3_256(message.encode()).hexdigest()


'''
c = DSA()
k = c.get_key()
print(k)

print(rsa().loadkey('qsfjgthfb34uifg34tr387fgvwu'))
print(get_key().get_pub('qsfjgthfb34uifg34tr387fgvwu'))

'''
