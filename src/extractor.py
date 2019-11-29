import binascii
import hashlib

from src.bitcoin_service import BitcoinService
from src.utils import Utils


# noinspection SpellCheckingInspection
class Extractor:
    @staticmethod
    def calculate_fee(tx_id):
        decoded_tx = BitcoinService.get_transaction(tx_id)
        vin = decoded_tx['vin']
        vout = decoded_tx['vout']

        sum_vin = 0
        try:
            for in_tx in vin:
                decoded_in_tx = BitcoinService.get_transaction(in_tx['txid'])
                sum_vin += decoded_in_tx['vout'][in_tx['vout']]['value']
        except KeyError:
            print('Could not extract key from vin transaction. Are you trying to compute coinbase transaction?')

        sum_vout = 0
        for out_tx in vout:
            sum_vout += out_tx['value']

        return sum_vin - sum_vout

    @staticmethod
    def validate_block(block_id):
        block = BitcoinService.get_block(block_id)
        version_hex = block['versionHex']
        prev_block_hex = block['previousblockhash']
        merkle_root_hash = block['merkleroot']
        time_hex = hex(int(block['time']))[2:]
        bits_hex = block['bits']
        nonce_hex = hex(int(block['nonce']))[2:]

        # concatinated header
        header_hex = (Utils.reverse_hex(version_hex) + Utils.reverse_hex(prev_block_hex)
                      + Utils.reverse_hex(merkle_root_hash) + Utils.reverse_hex(time_hex) + Utils.reverse_hex(bits_hex)
                      + Utils.reverse_hex(nonce_hex))
        # header in binary form
        header_bin = binascii.unhexlify(header_hex)

        # big endian hash
        block_hash_be = hashlib.sha256(hashlib.sha256(header_bin).digest()).hexdigest()
        # little endian hash
        block_hash = Utils.reverse_hex(block_hash_be)

        return block_hash == block['hash']