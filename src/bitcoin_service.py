from bitcoin.rpc import RawProxy


class BitcoinService:
    @staticmethod
    def get_transaction(tx_id):
        proxy = RawProxy()
        raw_tx = proxy.getrawtransaction(tx_id)
        return proxy.decoderawtransaction(raw_tx)

    @staticmethod
    def get_block(block_id):
        proxy = RawProxy()
        return proxy.getblock(block_id)
