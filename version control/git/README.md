[Git Cheat Sheet](https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet)

Keywords:

- `HEAD` - a pointer to the current commit ID. Can be thought of as the current branch. When you switch branches, the HEAD changes to point to the tip of the new branch.
- `Remote` - the remote destination/URL of your repository

## Basics

- `git init [<directory>]` - initialize the current folder as a git repository
- `git clone <repository.git> [<directory name>]` - clone the repository. Optionaly give the directory a different name
- `git config user.name <name> [--global]` - define author name to be used for all commits in current repo, or all commits for all repos
- `git add <directory/file>` - stage changes in directory for the next commit. Individual files can be staged too
- `git commit -m "<message>"` - commit the staged changes, message required
- `git status` - list all files which are staged, unstaged, or untracked
- `git log` - display entire commit history
- `git diff` - display unstaged changes between your index and working directory

## Undo

- `git revert <commit>` - create a new commit which undoes all changes made in specified commit
- `git reset <file>` - remove file from staging area. Does not overwrite any changes
- `git clean -n` - show files which would be remove from working directory.

## Rewrite Git History

- `git commit --amend` - merge last commit with staged changes. Use with nothing staged to edit the commit message
- `git rebase <base>` - rebase the current branch onto base. Base can be a commit ID, branch name, tag, or relative reference to HEAD
- `git reflog` - show a log of changes to local repo's HEAD

## Branches

- `git branch` - list all branches in your repo
- `git checkout -b <branch name>` - create and switch to a new branch. Drop -b to switch to an existing branch
- `git merge <branch>` - merge branch into current branch

## Remote

- `git remote add <name> <repo URL>` - create a connection to a remote repo. This is not required for repos you have cloned, as the remote will already be named origin.
- `git fetch [<remote>] [<branch>]` - fetch a specific branch from remote. Downloads the contents from the remote
- `git pull [<remote>]` - fetch the remote copy of the current branch, immediately merging into the local copy
- `git push <remote> <branch>` - push the branch to remote, creating the branch if it doesn't exist
