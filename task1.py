import hashlib
import binascii
from bitcoin.rpc import RawProxy

p=RawProxy()

hash=raw_input("Write block hash:")

header=p.getblockheader(hash)

version=binascii.hexlify(binascii.unhexlify(str(header['versionHex']))[::-1])
prevBlockHash=binascii.hexlify(binascii.unhexlify(str(header['previousblockhash']))[::-1])
merkleRoot=binascii.hexlify(binascii.unhexlify(str(header['merkleroot']))[::-1])
time=binascii.hexlify(binascii.unhexlify(hex(header['time'])[2:])[::-1])
bits=binascii.hexlify(binascii.unhexlify(str(header['bits']))[::-1])
nonce=binascii.hexlify(binascii.unhexlify(hex(header['nonce'])[2:])[::-1])

headerHex=version+prevBlockHash+merkleRoot+time+bits+nonce

headerTemp=binascii.unhexlify(headerHex)

hash=hashlib.sha256(hashlib.sha256(headerTemp).digest()).digest()
hash=binascii.hexlify(hash)

finalResult=binascii.hexlify(binascii.unhexlify(hash)[::-1])

print(finalResult)
print(header['hash'])

if header['hash']==finalResult:
        print('Match')
else:
        print('Hash mismatch')
