from hashlib import sha256


class Block:
    nonce = 0

    def __init__(self, index, timestamp, data, previous_hash=None):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        input_ = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return sha256(input_.encode('utf-8')).hexdigest()

    def __str__(self):
        return str(self.index) + ', ' + str(self.data) + ', ' + str(self.hash)
