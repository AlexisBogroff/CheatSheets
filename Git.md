## Create a repository

### Create a local folder and initialize git
```
cd path/to/enclosing/folder
mkdir <repo_folder_name>
cd <repo_folder_name>
git init
echo "Write your introduction here" >> README.md
git add README.md
git commit -m "Repo initialization"
git branch -M master
```

### Link the local folder with a remote one
- Go to your Github account
- Click "New repository" ("+" sign on top right at time of writting nov-2020)
- Write a name and click Create repository
- Copy the link of the form "https://github.com/<MyAccount>/<repository_name>.git"
```
git remote add origin "https://github.com/<MyAccount>/<repository_name>.git"
git push -u origin master
```

## Branches
### Rename a branch
```
git checkout <current_branch_name>
git branch -m <new_branch_name>
git push origin -u <new_branch_name>
```

# TODO: reorganize
git pull  # retrieve repo
git status  # get amended files
git diff <fname>  # get amended rows in the file specified

git add  # ps: todo 1 file at a time, add to the temp transfer folder
git commit -m "<comment>"  # add comment to the change
git push  # update git repo

git log  # verify the change and commit


2019-12:
git push origin --delete <name>  # delete a remote branch
git branch -d <name>  # delete a local branch
git revert HEAD~1  # revert the last commit


2020-01:
git checkout <branch>  # change active branch with an existing one
git checkout -b <new_branch>  # change active branch with an existing one
git push -u origin <new_branch>  # build the remote branch
git branch -D <branch_name>  # delete a local branch

## Push changes to the remote branch
git add -A  # stage all changes
git commit -am "commit message"
git push

## Remove local untracked files
git clean -n  # see what would be deleted
git clean -f  # actually delete the files

## Stop tracking a file
git rm --cached <file_name> -r  # -r for recursive folder


## 2020-04
git branch -a  # see all branches (including remotes)

## Replace a branch content by another's (master by dev)
git checkout dev  # it creates the branch dev if it didn't exist
git merge --strategy=ours master    # keep the content of this branch, but record a merge
git checkout master
git merge dev             # fast-forward master up to the merge
git push
git reset --soft HEAD~  # undo a commit that was not pushed


## 2020-09
.gitignore subtleties:

If you want to ignore files in just one repository but want to avoid committing the ignore list (for example for personal files) you can add them to .git/info/exclude in that repository.

If you want to ignore certain files on every repository on your machine you can create the file ~/.gitignore_global and then run
ex: git config --global core.excludesfile ~/.gitignore_global

## 2020-11
git remote -v   # to know the address that is set for the repository
git remote set-url origin [new_address]
git branch --list  # list all local branches
git symbolic-ref HEAD  # get the name of the current branch
