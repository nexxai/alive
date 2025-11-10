#!/usr/bin/env python3

import argparse
import os
import sys
import datetime
from src.cert_utils import fetch_certs, extract_hostnames
from src.dns_utils import check_alive
from src.save_utils import save_results


def main():
    parser = argparse.ArgumentParser(description="Find alive subdomains from crt.sh")
    parser.add_argument("domain", help="Root domain")
    args = parser.parse_args()

    domain = args.domain
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(
        "results", f"alive_{domain.replace('.', '_')}_{timestamp}.txt"
    )

    print(f"[-] Fetching certificates for {domain} from crt.sh...")
    try:
        certs = fetch_certs(domain)
    except Exception as e:
        print(f"[!] Error fetching from crt.sh: {e}")
        sys.exit(1)
    print(f"[+] Fetched {len(certs)} certificates")

    print("[-] Extracting unique hostnames from certificates...")
    hostnames = extract_hostnames(certs)
    print(f"[+] Extracted {len(hostnames)} unique hostnames")

    print("[-] Checking DNS resolution...")
    alive = check_alive(hostnames)
    print(f"[+] Found {len(alive)} alive domains")

    print(f"[-] Saving results to {filename}...")
    save_results(alive, filename)
    print(f"[+] Saved results to {filename}")


if __name__ == "__main__":
    main()
