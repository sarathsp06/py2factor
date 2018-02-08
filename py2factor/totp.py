import hmac, base64, hashlib, time

def big_endian_encode(number):
	hex_codes = [chr(0x00)] * 8
	for i in xrange(8):
		hex_codes[7-i] = chr(number & 0xff)
		number = number >> 8
	return "".join(hex_codes)


def big_endian_decode(data):
	val = 0
	for j in  map(ord,data):
		val = (val << 8) + j
	return val

def hashing_algorithm(algo):
	algos = {"sha1" : hashlib.sha1}
	return algos[algo]


def get_hotp_token(secret, intervals_no,hash_algo="sha1"):
    key = base64.b32decode(secret, True)
    msg =  big_endian_encode(intervals_no)
    h = hmac.new(key, msg, hashing_algorithm(hash_algo)).digest()
    o = ord(h[19]) & 0x0f
    h = (big_endian_decode(h[o:o+4]) & 0x7fffffff) % 1000000
    return h

def get_totp_token(secret,duration=30):
    return get_hotp_token(secret, intervals_no=int(time.time())//duration)