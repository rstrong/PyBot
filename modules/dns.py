import socket
import re
import pprint
def __init__(self):
    print "DNS Initialized"

def say(user, channel, msg):
    regexp = re.compile('^\s*(?:nslookup|dns)(?: for)?\s+(\S+)$', re.IGNORECASE);
    
    result = None
    if regexp.match(msg):
        m = re.findall(regexp,msg)
        if re.match('\d+\.\d+\.\d+\.\d+', m[0]):
            result = get_dns_by_num(m[0])
        else:
            result = get_dns_by_name(m[0])        
    if result:
        return result

def get_dns_by_num(ip):
    result = None
    try:
        r = socket.gethostbyaddr(ip)
        if r[0]:
            result = "%s resolves to %s" % (ip, r[0])
        else:
            raise FoobarException
    except:
        result = "I had trouble resolving %s" % ip
    return result

def get_dns_by_name(host):
    result = None
    try:
        r = socket.gethostbyname(host)
        if r:
            result = "%s resolves to %s" % (host, r)
        else:
            raise FoobarException
    except:
        result = "I had trouble find %s in dns" % host
    return result
