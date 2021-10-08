# creating a sample bitcoin address
# first install bitcoin using pip
# import bitcoin lib
from bitcoin import *
# create Private key
private_key = random_key()
print(private_key)
# create public key
public_key = privtopub(private_key)
print(public_key)
# create Abitcoin Address
address = pubtoaddr(public_key)
print("My Address is : " + address)
