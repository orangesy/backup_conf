#!/usr/bin/env python
# $./cert_web_check.py "www.google.com"
# output days
#
import sys
import ssl
import OpenSSL
import datetime

d = sys.argv
#cert = ssl.get_server_certificate(('www.google.com', 443))
cert = ssl.get_server_certificate((d[1], 443))
x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
#x509.get_subject().get_components()
#x509.get_issuer()
#x509.get_notAfter()


cur_date = datetime.datetime.utcnow()
cert_nbefore = datetime.datetime.strptime(x509.get_notBefore(),'%Y%m%d%H%M%SZ')
cert_nafter = datetime.datetime.strptime(x509.get_notAfter(),'%Y%m%d%H%M%SZ')
expire_days = int((cert_nafter - cur_date).days)
print expire_days

