#!/usr/bin/env bash

# Branching and feature-development workflow.
# This script is intentionally not executed during project preparation.

set -e

REPOSITORY_NAME="branching-feature-portal"
PROJECT_DIR=$(pwd)
FEATURE_SEED="$PROJECT_DIR/.feature_seed"

echo "Step 1: Perform safety and tool checks"
if [ -d .git ]; then
    echo "This folder already has its own Git repository. Stopping safely."
    exit 1
fi
command -v git >/dev/null
command -v gh >/dev/null
gh auth status

echo "Step 2: Initialize the main branch"
git init -b main
git config user.name >/dev/null
git config user.email >/dev/null
git add .gitignore README.md VIDEO_SCRIPT.md git_workflow.sh logging_config.py
git commit -m "Set up User Portal project"
git add main.py
git commit -m "Add initial User Portal application"

echo "Step 3: Create the public repository and push main"
gh repo create "$REPOSITORY_NAME" \
    --public \
    --source=. \
    --remote=origin
git push -u origin main
git remote -v

echo "Step 4: Develop feature-login using git checkout"
git checkout -b feature-login
cp "$FEATURE_SEED/feature-login/login.py" login.py
cp "$FEATURE_SEED/feature-login/main.py" main.py
python main.py
git status
git diff
git add login.py main.py
git commit -m "Add user login feature"
git push -u origin feature-login

echo "Step 5: Merge feature-login and delete its local branch"
git checkout main
git merge --no-ff feature-login -m "Merge login feature into main"
git push origin main
git branch -d feature-login

echo "Step 6: Develop feature-profile using git switch"
git switch -c feature-profile
cp "$FEATURE_SEED/feature-profile/profile.py" profile.py
cp "$FEATURE_SEED/feature-profile/main.py" main.py
python main.py
git status
git diff
git add profile.py main.py
git commit -m "Add user profile feature"
git push -u origin feature-profile

echo "Step 7: Merge feature-profile and delete its local branch"
git switch main
git merge --no-ff feature-profile -m "Merge profile feature into main"
git push origin main
git branch -d feature-profile

echo "Step 8: Develop feature-dashboard"
git switch -c feature-dashboard
cp "$FEATURE_SEED/feature-dashboard/dashboard.py" dashboard.py
cp "$FEATURE_SEED/feature-dashboard/main.py" main.py
cp "$FEATURE_SEED/feature-dashboard/test_portal.py" test_portal.py
python test_portal.py
python main.py
git status
git diff
git add dashboard.py main.py test_portal.py
git commit -m "Add user dashboard feature and tests"
git push -u origin feature-dashboard

echo "Step 9: Merge feature-dashboard and delete its local branch"
git switch main
git merge --no-ff feature-dashboard -m "Merge dashboard feature into main"
git push origin main
git branch -d feature-dashboard

echo "Step 10: Verify all local and remote branches"
git fetch origin
git branch --all

echo "Step 11: Run the final merged project"
python test_portal.py
python main.py

echo "Step 12: Save the public repository URL"
REPOSITORY_URL=$(gh repo view --json url --jq .url)
printf '# Submission Link\n\n- Repository: %s\n' \
    "$REPOSITORY_URL" > SUBMISSION_LINKS.md
git add SUBMISSION_LINKS.md
git commit -m "Add public repository link"
git push origin main

echo "Step 13: Display the final branch and merge history"
git status
git branch --all
git log --oneline --graph --all --decorate
echo "Repository: $REPOSITORY_URL"
