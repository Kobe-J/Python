import json

def read_config():
    file = open("config.json",'r', encoding='UTF-8')
    content = file.read()
    file.close()
    return content

def analyze_config():
    config = read_config()
    config = json.loads(config)

    url = config["http"]["url"]
    title = config["http"]["title"]

    ip_address = config["icmp"]["ip_address"]
    times = config["icmp"]["times"]

    domain = config["dns"]["domain"]
    dnsserver = config["dns"]["dnsserver"]
    return url,title,ip_address,times,domain,dnsserver