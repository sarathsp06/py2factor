from urlparse import urlsplit,parse_qs
from urllib import unquote
from totp import validate_secret,get_totp_token
from totp import ALGORITHM,PERIOD,DIGITS

class Profile(object):
	"""Stores totp details of a profile"""
	def __init__(self,url=None,name=None,secret=None,period=PERIOD,algorithm=ALGORITHM,digits=DIGITS):
		super(Profile, self).__init__()
		if url is not None:
			self.parse_url()
			return
		if name is None or secret is None:
			raise ValueError("Name and Secret are mandatory if Url is not passed")
		self.url=None
		self.name=name
		self.secret=secret
		self.period = period
		self.issuer = None
		self.algorithm=algorithm
		self.digits=digits
		self.url = url

	def totp(self):
		return get_totp_token(self.secret,self.period,self.algorithm,self.digits)

	def parse_url(self):
		""" parse the self.url and assign values
		sample url  : otpauth://totp/ACME%20Co:john.doe@email.com?secret=HXDMVJECJJWSRB3HWIZR4IFUGFTMXBOZ&issuer=ACME%20Co&algorithm=SHA1&digits=6&period=30
		"""
		if self.url is None:
			raise ValueError("URI is not set")
		url_split = urlsplit(self.url)
		if url_split.scheme !="otpauth" or url_split.netloc != "totp":
			raise ValueError("Invalid url : url format has to be otpauth://totp/name?secret=Base32SECRET&issuer=&algorithm=SHA1&digits=6&period=30")
		query = parse_qs(url_split.query)
		try:
			self.secret = query["secret"][0]
			validate_secret(self.secret)
		except KeyError:
			raise ValueError("Invalid url : No secret")
		except TypeError as e:
			raise ValueError("Invalid secret : Not in base32 format ," + str(e))
		
		self.name = unquote(url_split.path[1:])			
		self.algorithm = query.get("algorithm",[ALGORITHM])[0]
		self.issuer = query.get("issuer",[None])[0]
		self.digits = int(query.get("digits",[DIGITS])[0])
		self.period = int(query.get("period",[PERIOD])[0])