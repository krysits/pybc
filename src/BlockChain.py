from .Block import Block


def str_repeat(string="", times=0):
    return string * times


class BlockChain:
    difficulty = 4
    chain = []

    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "2022-01-01", "Genesis Block")

    def get_last_block(self):
        return self.chain[len(self.chain) - 1]

    def push(self, block):
        block.previous_hash = self.get_last_block().hash
        self.mine(block)
        self.chain.append(block)

    def mine(self, block):
        while str_repeat('0', self.difficulty) not in block.hash:
            block.nonce += 1
            block.hash = block.calculate_hash()

        print('Block mined: ', block.hash)

    def is_valid(self):
        for key in range(1, len(self.chain)):
            block = self.chain[key]
            previous_block = self.chain[key - 1]

            if block.hash != block.calculate_hash():
                return False

            if block.previous_hash != previous_block.hash:
                return False

        return True

    def __str__(self):
        output = ''
        for block in self.chain:
            output += str(block) + "\n"
        return output
