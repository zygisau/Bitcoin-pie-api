import binascii


class Utils:
    @staticmethod
    def reverse_hex(target):
        byte_arr = bytearray.fromhex(target)
        byte_arr.reverse()
        hex_string = ''.join(format(x, '02x') for x in byte_arr)
        return hex_string
