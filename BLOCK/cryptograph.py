
from Crypto.Cipher import AES
import hashlib
import binascii
import secrets
import os
import ecdsa
from ecdsa import SECP256k1

#padding of data
# code extarcted from open source library
def add_padding(message: bytes, target_length: int) -> bytes:\
    #target length is key.bit_length() == 256, 384, 512...
    max_msglength = target_length - 11
    msglength = len(message)

    if msglength > max_msglength:
        raise OverflowError('%i bytes needed for message, but there is only'
                            ' space for %i' % (msglength, max_msglength))

    # Get random padding
    padding = b''
    padding_length = target_length - msglength - 3

    # We remove 0-bytes, so we'll end up with less padding than we've asked for,
    # so keep adding data until we're at the correct length.
    while len(padding) < padding_length:
        needed_bytes = padding_length - len(padding)

        # Always read at least 8 bytes more than we need, and trim off the rest
        # after removing the 0-bytes. This increases the chance of getting
        # enough bytes, especially when needed_bytes is small
        new_padding = os.urandom(needed_bytes + 5)
        new_padding = new_padding.replace(b'\x00', b'')
        padding = padding + new_padding[:needed_bytes]

    assert len(padding) == padding_length

    return b''.join([b'\x00\x02',
                     padding,
                     b'\x00',
                     message])

#remove pading from decrypted message
def remove_padding(msg: bytes):
    cleartext_marker_bad = not compare_digest(msg[:2], b'\x00\x02')
    sep_idx = msg.find(b'\x00', 2)
    sep_idx_bad = sep_idx < 10
    anything_bad = cleartext_marker_bad | sep_idx_bad

    if anything_bad:
        raise DecryptionError('Decryption failed')
    return msg[sep_idx + 1:]

n_field = 39402006196394479212279040100143613805079739270465446667946905279627659399113263569398956308152294913554433653942643

class aes_():
    def __init__(self, data: bytes, password_hash): #password should be in hash form
        self.data = data
        self.password_hash = password_hash
    
    def aes_key(self):#key and hash
        self.key = secrets.randbelow(n_field)
        
        self.enc_key = hashlib.sha3_256(int.to_bytes(self.key, 256, 'big'))
        self.enc_key.update(self.password_hash.encode())
        
        return self.enc_key.digest(), self.key #password and key should always be rememberd

    def hexlfy(self, byte):
        self.byte = byte
        return binascii.hexlify(self.byte)
    
    def encrypt(self):
        self.key_, self.primary_key = self.aes_key()

        self.encrypt_mode = AES.new(self.key_, AES.MODE_GCM)
        #padding blocksize
        self.size = 256
        self.data_ = add_padding(self.data, self.size)
        self.encrypt_data = self.encrypt_mode.encrypt_and_digest(self.data_)

        #it's a iv that is used while decrypting
        self.iv = self.encrypt_mode.nonce
        # seperating data form encrypted text
        self.enc_data, self.authtab = self.encrypt_data
        #compiling all data together(encrypted_data + authtag)
        self.whole_encdata = self.hexlfy(self.enc_data) + b'  ~  ' + self.hexlfy(self.authtab)
        #key with nonce(that is iv)
        self._key_ = self.primary_key,  self.hexlfy(self.iv)

        # return a byte data contains(encrypted data, authtab, nonce) and aes key(sha3-512 user key)
        return (self.whole_encdata, self._key_)

def aes_gmc(data):
    encrypted_data = aes_(data).encrypt_aes()
    return encrypted_data

class aes_decrypt():
    def __init__(self, primary_key, nonce, password_hash, data):
        #seperate the encrypted data and authtag
        self.datta = data
        self.priv_key = primary_key
        self.hash = password_hash
        self.nonce = nonce
        self.data = tuple(map(bytes, self.datta.split(b'  ~  ')))

    def aes_key(self):
        #creating a key by required input
        self.enc_key = hashlib.sha3_256(int.to_bytes(self.priv_key, 256, 'big'))
        self.enc_key.update(self.hash.encode())
        
        return self.enc_key.digest()

    def decryption(self):
        self.authtag = binascii.unhexlify(self.data[1])
        self.enc_data = binascii.unhexlify(self.data[0])
        self.nonce = binascii.unhexlify(self.nonce)
        self.key_ = self.aes_key()
        self.decrypt_mode = AES.new(self.key_, AES.MODE_GCM, nonce=self.nonce)
        # padding block size
        self.size = 256
        self.decrypt_data = self.decrypt_mode.decrypt_and_verify(self.enc_data, self.authtag)

        return remove_padding(self.decrypt_data)

class DSA():
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

#hash = hashlib.sha3_256('password_'.encode()).hexdigest()
#a = aes_(b'data', hash)
#enc_data = a.encrypt()
#print(enc_data)

#b = aes_decrypt(enc_data[1][0], enc_data[1][1], hash, enc_data[0])
#print(b.decryption())
