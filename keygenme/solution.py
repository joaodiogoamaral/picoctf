
import hashlib
username=b"SCHOFIELD"

key=""
# These indexes are checked (in sequence) within the check_key function of the downloaded python file
key_indexes= [4,5,3,6,2,7,1,8] 


for i in key_indexes:
    key += hashlib.sha256(username).hexdigest()[i] # This will append the sha256 of the indexes which are checked to validate the key
print(key) # On the python file, there are already the prefix and sufix, this print will show the dynamic portion

