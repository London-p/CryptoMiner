from hashlib import sha256
MAX_NONCE = 1000000000000

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def  mine(block_number, transactions, previous_hash, prefix_zeros):
    preifx_str = '0'*prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(preifx_str):
            print(f"Successfully mined bitcoins with value:{nonce}")
            return new_hash
    
    raise BaseException(f"Couldn't find hash after trying {MAX_NONCE} times")

if __name__=='__main__':
    transactions='''
    Phillip->Joe->20,
    Alex->Jake->45
    '''

    difficulty=6
    import time
    start = time.time()
    print("Started mining")
    new_hash = mine(5,transactions,'000000098fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', difficulty)
    total_time = ((time.time() - start)) + 2.5
    ear = (total_time)**16 / 31536000 / 6.25
    year = 1 / (ear)
    print(f"Finished mining. You can mine {year} bitcoins in one year")
    print (new_hash)
