# Video Explanation Guide

1. Show the initial `main` branch and explain that it contains the starting project.
2. Create `feature-login` with `git checkout -b`, implement login, commit, and push.
3. Switch to `main`, merge `feature-login`, push `main`, and delete the local branch.
4. Create `feature-profile` with `git switch -c` and repeat the workflow.
5. Create `feature-dashboard`, add the dashboard and final tests, then repeat the
   commit, push, merge, and local deletion workflow.
6. Run `git branch --all`. Explain that local feature branches were deleted while
   remote feature branches were retained for assignment evidence.
7. Run `git log --oneline --graph --all --decorate` and identify the three feature
   commits and three merge commits.
8. Run `python main.py` and explain the login, profile, and dashboard output.
9. Run `python test_portal.py` and show the passing tests.
10. Open the public GitHub repository and show `main` and all three remote branches.

Key explanation: a feature branch isolates one change so development does not
directly disturb the stable `main` branch. Merging integrates the completed work.
