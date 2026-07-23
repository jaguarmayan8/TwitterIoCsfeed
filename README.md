# TwitterIoCsfeed

Automated daily collection of IOCs from public feeds for cybersecurity labs and SOCs.

## Features

- Daily IOC collection from reliable public sources (URLhaus, TweetFeed, Abuse.ch, etc.)
- Docker support for easy deployment
- Automatic GitHub push to `Output/` folder
- Runs every day at 8:00 AM Central Time

## Quick Start

```bash
docker compose build
docker compose up
Output
New files are saved daily in the Output/ folder and automatically pushed to this repository.
Automation

Cron job runs every day at 8 AM Central
Uses Docker for consistency

Author
Jorge Tejada (@Chap_Corner)
License
GPL-3.0
