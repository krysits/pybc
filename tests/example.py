# Example of the chain, adding block values
import datetime
from src.Block import Block
from src.BlockChain import BlockChain


def run_example():
    test_coin = BlockChain()

    print("Mining block 1...")
    test_coin.push(Block(index=1, timestamp=datetime.datetime.now(), data="amount: 4"))

    print("Mining block 2...")
    test_coin.push(Block(index=2, timestamp=datetime.datetime.now(), data="amount: 10"))

    print("Chain valid: ", test_coin.is_valid())

    print(test_coin)
