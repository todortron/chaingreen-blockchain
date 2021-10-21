from typing import Tuple

import aiosqlite

from chaingreen.consensus.blockchain import Blockchain
from chaingreen.consensus.constants import ConsensusConstants
from chaingreen.full_node.block_store import BlockStore
from chaingreen.full_node.coin_store import CoinStore
from chaingreen.full_node.hint_store import HintStore
from chaingreen.util.db_wrapper import DBWrapper


async def create_ram_blockchain(consensus_constants: ConsensusConstants) -> Tuple[aiosqlite.Connection, Blockchain]:
    connection = await aiosqlite.connect(":memory:")
    db_wrapper = DBWrapper(connection)
    block_store = await BlockStore.create(db_wrapper)
    coin_store = await CoinStore.create(db_wrapper)
    hint_store = await HintStore.create(db_wrapper)
    blockchain = await Blockchain.create(coin_store, block_store, consensus_constants, hint_store)
    return connection, blockchain
