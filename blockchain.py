from block import Block


class Blockchain:
    """
    blueprint of a local blockchain
    """

    def __init__(self):
        self.chain = []
        self.unconfirmed_transactions = []
        self.genesis_block()

    def genesis_block(self):
        """
        the first hard-coded block to kicksstart the chain
        :return: the updated chain with the genesis block
        """
        transactions = []
        genesis_block = Block(transactions, "0")
        genesis_block.generate_hash()
        self.chain.append(genesis_block)

    def add_block(self, transactions):
        """
        adds new blocks to the chain (without general consensus of the PoW but the PoW is implemented
        :param transactions: the transactions of the block
        :return: the updated chain
        """
        previous_hash = (self.chain[len(self.chain) - 1]).hash
        new_block = Block(transactions, previous_hash)
        new_block.generate_hash()
        # proof = proof_of_work(block)
        self.chain.append(new_block)

    def print_blocks(self):
        """
        prints the blocks in the blockchain
        :return: print statements
        """
        for i in range(len(self.chain)):
            current_block = self.chain[i]
            print("Block {} {}".format(i, current_block))
            current_block.print_contents()

    def validate_chain(self):
        """
        checks if the blockchain makes sense based on the hashes
        :return: validated statements whether the chain is okay
        """
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.generate_hash():
                print("Current hash does not equal generated hash")
                return False
            if current.previous_hash != previous.generate_hash():
                print("Previous block's hash got changed")
                return False
        return True

    def proof_of_work(self, block, difficulty=2):
        """
        PoW of the blockchain by finding the nonce (hash with two 0s)
        :param block: the new block
        :param difficulty: the amount of 0s to find a hash for
        :return: the hash that satisfies the condition
        """
        proof = block.generate_hash()
        while proof[:2] != "0" * difficulty:
            block.nonce += 1
            proof = block.generate_hash()
        block.nonce = 0
        return proof
