# -*- coding: utf-8 -*-

try:  # pragma: no cover
    # py3
    from urllib.parse import urlsplit,parse_qs,unquote
except ImportError:  # pragma: no cover
    # py2
    from urlparse import urlsplit,parse_qs
	from urllib import unquote

