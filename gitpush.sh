#!/bin/bash
cd /home/manu/TwitterIoCsfeed

git add Output/*.csv 2>/dev/null

if git diff --cached --quiet; then
    echo "$(date) - No changes to commit"
else
    git commit -m "Daily IOC update - $(date +'%Y-%m-%d %H:%M')"
    git push origin main
    echo "$(date) - Pushed to GitHub"
fi
