# Branching and Feature Development

This project demonstrates independent feature development through three Git
branches and merges the completed features into `main`.

## Required branches

| Branch | Change implemented |
|---|---|
| `feature-login` | Adds demonstration user authentication |
| `feature-profile` | Adds user profile creation and display |
| `feature-dashboard` | Adds a course-progress dashboard and final tests |

## Workflow

Each feature follows the same process:

1. Create a feature branch from the latest `main`.
2. Implement and test one focused feature.
3. Stage and commit the change.
4. Push the feature branch to GitHub.
5. Switch back to `main`.
6. Merge with `--no-ff` to preserve a visible merge commit.
7. Push the updated `main` branch.
8. Delete the merged local feature branch.

The remote feature branches are intentionally retained because the assignment
requires all branches to be published.

## Final project structure

After the workflow finishes, the merged `main` branch contains:

```text
branching-feature-portal/
├── .gitignore
├── README.md
├── VIDEO_SCRIPT.md
├── dashboard.py
├── login.py
├── logging_config.py
├── main.py
├── profile.py
├── test_portal.py
└── git_workflow.sh
```

## Prepared feature files

The ignored `.feature_seed/` directory contains the changes for each feature.
The workflow script copies the appropriate files only after switching to that
feature branch. Therefore, each commit and merge accurately demonstrates how the
feature entered the project.

## Run the initial version

```bash
python main.py
```

## Run the complete Git workflow

Review the script first, then run it while recording the video:

```bash
bash git_workflow.sh
```

The script requires GitHub CLI to be installed and authenticated. It creates a
public repository named `branching-feature-portal`.

## Final application commands

After all merges:

```bash
python main.py
python test_portal.py
git branch --all
git log --oneline --graph --all --decorate
```

## Submission links

- Public GitHub repository: `GENERATED-AFTER-RUNNING-THE-SCRIPT`
- YouTube video: `ADD-YOUTUBE-VIDEO-URL`
