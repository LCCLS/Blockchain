import datetime
from hashlib import sha256


class Block:
    """
    basic blueprint of an individual block
    """
    def __init__(self, transactions, previous_hash):
        self.time_stamp = datetime.datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.generate_hash()

    def generate_hash(self):
        """
        generates a sha256 hash based on the timestamp, the transactoins, the previous hash and the PoW
        :return: the block hash
        """
        block_header = str(self.time_stamp) + str(self.transactions) + str(self.previous_hash) + str(self.nonce)
        block_hash = sha256(block_header.encode())
        return block_hash.hexdigest()

    def print_contents(self):
        """
        basic print function of the block
        :return: print statements
        """
        print("timestamp:", self.time_stamp)
        print("transactions:", self.transactions)
        print("current hash:", self.generate_hash())
        print("previous hash:", self.previous_hash)
