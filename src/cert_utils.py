import requests


def fetch_certs(domain):
    url = f"https://crt.sh/?q={domain}&output=json&exclude=expired"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def extract_hostnames(certs):
    hostnames = set()
    for cert in certs:
        name = cert.get("name_value", "")
        if name.startswith("*."):
            continue
        hostnames.add(name.lower())
    return hostnames
