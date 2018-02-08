from urlparse import urlsplit,parse_qs
class Profile(object):
	"""Stores totp details of a profile"""
	def __init__(self,url,name,secret,period=30,algorithm='SHA1',issuer=):
		super(Profile, self).__init__()
		if url is not None:
			self.url = url
			self.parse_url()
			return
		self.name=name
		self.secret=secret
		self.period = duration
		self.algorithm=algo

	def parse_url(self):
		""" parse the self.url and assign values"""
		if self.url is None:
			raise ValueError("URI is not set")
		url_split = urlsplit(self.url)
		if url_split is not "otpauth" or url_split.netloc is not "totp"
		return None

	def totp(self):
		""" find the TOTP token at any given time"""
		return None



# 	algorithm': ['SHA1']
 # 'digits': ['6'],
 # 'issuer': ['ACME Co'],
 # 'period': ['30'],
 # 'secret': ['HXDMVJECJJWSRB3HWIZR4IFUGFTMXBOZ']}