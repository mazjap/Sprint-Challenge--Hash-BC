import hashlib
import requests

import sys

from uuid import uuid4

from timeit import default_timer as timer

import random


def proof_of_work(last_proof):
    """
    Multi-Ouroboros of Work Algorithm
    - Find a number p' such that the last six digits of hash(p) are equal
    to the first six digits of hash(p')
    - IE:  last_hash: ...AE9123456, new hash 123456888...
    - p is the previous proof, and p' is the new proof
    - Use the same method to generate SHA-256 hashes as the examples in class
    """

    start = timer()
    print("Searching for next proof")
    proof = random_int()
    old_hash = sha(last_proof)
    hash_prime = sha(proof)
    while valid_proof(old_hash, hash_prime) is False:
        if proof % 50_000_000 is 0:
            print("changing it up")
            old_hash = sha(get_block().get('proof'))
        # proof = random_int()
        proof += 1
        hash_prime = sha(proof)
    return proof


    print("Proof found: " + str(proof) + " in " + str(timer() - start))
    return proof

def random_int():
    return random.randint(-sys.maxsize, sys.maxsize)

def sha(value):
    return hashlib.sha256(str(value).encode()).hexdigest()

def valid_proof(last_hash, hash_prime):
    """
    Validates the Proof:  Multi-ouroborus:  Do the last six characters of
    the hash of the last proof match the first six characters of the hash
    of the new proof?

    IE:  last_hash: ...AE9123456, new hash 123456E88...
    """
    if last_hash[-6:] == hash_prime[:6]:
        return True
    return False

def get_block():
    r = requests.get(url="https://lambda-coin.herokuapp.com/api" + "/last_proof")
    return r.json()

if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "https://lambda-coin.herokuapp.com/api"

    coins_mined = 0

    # Load or create ID
    f = open("my_id.txt", "r")
    id = f.read()
    print("ID is", id)
    f.close()

    if id == 'NONAME\n':
        print("ERROR: You must change your name in `my_id.txt`!")
        exit()
    # Run forever until interrupted
    while True:
        # Get the last proof from the server
        data = get_block()
        new_proof = proof_of_work(data.get('proof'))

        post_data = {"proof": new_proof,
                     "id": id}

        r = requests.post(url=node + "/mine", json=post_data)
        data = r.json()
        if data.get('message') == 'New Block Forged':
            coins_mined += 1
            print("Total coins mined: " + str(coins_mined))
        else:
            print(data.get('message'))
