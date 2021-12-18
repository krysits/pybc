# Hack the chain, changing values in the first block.
import datetime
from src.Block import Block
from src.BlockChain import BlockChain


def is_secure():
    test_coin = BlockChain()

    print("Mining block 1...")
    test_coin.push(Block(index=1, timestamp=datetime.datetime.now(), data="amount: 4"))

    print("Mining block 2...")
    test_coin.push(Block(index=2, timestamp=datetime.datetime.now(), data="amount: 10"))

    print("Chain valid: ", test_coin.is_valid())

    print("Changing second block...")
    test_coin.chain[1].data = "amount: 1000"
    test_coin.chain[1].hash = test_coin.chain[1].calculate_hash()

    print("Chain valid: ", test_coin.is_valid())
