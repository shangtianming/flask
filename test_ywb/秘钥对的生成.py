from Crypto.PublicKey import RSA
from Crypto import Random
RANDOM_GENERATOR = Random.new().read
rsa = RSA.generate(1024, RANDOM_GENERATOR)
# 秘钥对的生成
PRIVATE_PEM = rsa.exportKey()
with open('master-private.pem', 'w') as f:
    f.write(PRIVATE_PEM.decode('utf-8'))
PUBLIC_PEM = rsa.publickey().exportKey()
with open('master-public.pem', 'w') as f:
    f.write(PUBLIC_PEM.decode('utf-8'))
