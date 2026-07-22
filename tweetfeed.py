#!/usr/bin/env python3
"""
Public IOC Feeds Collector for SOC Lab
Multiple reliable sources
"""

import requests
from datetime import datetime
from pathlib import Path

OUTPUT_DIR = Path("Output")
OUTPUT_DIR.mkdir(exist_ok=True)

def download_file(url, filename):
    try:
        r = requests.get(url, timeout=60)
        if r.status_code == 200 and len(r.content) > 1000:  # Avoid empty files
            path = OUTPUT_DIR / filename
            with open(path, "wb") as f:
                f.write(r.content)
            print(f"[+] Downloaded {filename}: {len(r.content)//1024} KB")
            return True
        else:
            print(f"[-] {filename}: No new data or empty")
    except Exception as e:
        print(f"[!] Error downloading {filename}: {e}")
    return False

def main():
    today = datetime.now().strftime("%Y%m%d")
    print(f"[*] Starting Public IOC Feeds Collector - {datetime.now().strftime('%Y-%m-%d %H:%M')}")

    feeds = [
        ("tweetfeed.csv", "https://tweetfeed.live/api/today.csv"),
        ("urlhaus.csv", "https://urlhaus.abuse.ch/downloads/csv_online/"),
        ("feodo_tracker.csv", "https://feodotracker.abuse.ch/downloads/ipblocklist.txt"),
        ("ssl_blacklist.csv", "https://sslbl.abuse.ch/blacklist/sslipblacklist.csv"),
        ("otx_pulses.json", "https://otx.alienvault.com/api/v1/pulses/subscribed?limit=20"),  # Requires free OTX key (optional)
        ("top_malicious.csv", "https://raw.githubusercontent.com/stamparm/ipsum/master/ipsum.txt"),
    ]

    for filename, url in feeds:
        download_file(url, f"{today}_{filename}")

    print("\n[+] All done! Check the output/ folder for today's IOC files.")
    print("Great for feeding Wazuh, TheHive, or your SIEM.")

if __name__ == "__main__":
    main()
