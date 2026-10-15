#!/usr/bin/env bash
set -euo pipefail

# Check commit message
if [ $# -eq 0 ]; then
    echo "Usage: ./update.sh \"Commit message\""
    exit 1
fi

MESSAGE="$*"

# Go to the project directory
cd "$(dirname "$0")"

# Check branches
if [[ "$(git branch --show-current)" != "master" ]] ||
   [[ "$(git -C public branch --show-current)" != "master" ]]; then
    echo "Error: both repositories must be on master."
    exit 1
fi

# 1. Generate website
echo "Generating website..."
"$HOME/.local/bin/hugo70"

# 2. Commit and push generated website
echo "Updating GitHub Pages..."
git -C public add -A

if ! git -C public diff --cached --quiet; then
    git -C public commit -m "$MESSAGE"
fi

git -C public push origin master

# 3. Commit and push source repository
echo "Updating academic-kickstart..."
git add -A

if ! git diff --cached --quiet; then
    git commit -m "$MESSAGE"
fi

git push origin master

echo "Website successfully updated!"