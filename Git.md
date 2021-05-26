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

Retrieve repo
```
git pull  
```

Get amended files
```
git status
```

Get amended rows in the file specified
```
git diff <fname>
```

Add files to the tracking list
```
git add <file_name>  # a specific file
git add .            # all the files
```

Add comment to the change and commit
```
git commit -m "<comment>"
```

Update git repo: this is the crucial step that impacts the remote repository, careful
```
git push
```

Verify the change and commit
```
git log
```


## 2019-12
Delete a remote branch
```
git push origin --delete <name>
```

Delete a local branch
```
git branch -d <name>
```

Revert the last commit
```
git revert HEAD~1
```

## 2020-01
Change active branch with an existing one
```
git checkout <branch>
```

Change active branch with an existing one
```
git checkout -b <new_branch>
```

Build the remote branch
```
git push -u origin <new_branch>
```

Delete a local branch
```
git branch -D <branch_name>
```

### Push changes to the remote branch
```
git add -A  # stage all changes
git commit -am "commit message"
git push
```

### Remove local untracked files
See what would be deleted
```
git clean -n
```

Actually delete the files
```
git clean -f
```

Stop tracking a file
```
git rm --cached <file_name> -r  # -r for recursive folder
```


## 2020-04
See all branches (including remotes)
```
git branch -a
```

### Replace a branch content by another's (master by dev)
Create the branch dev if it didn't exist
```
git checkout dev  
```

Keep the content of this branch, but record a merge
```
git merge --strategy=ours master
git checkout master
```

Fast-forward master up to the merge
```
git merge dev
git push
```

Undo a commit that was not pushed (tracked and committed but not pushed)
```
git reset --soft HEAD~
```

## 2020-09
### About .gitignore

If you want to ignore files in just one repository but want to avoid committing the ignore list (for example for personal files) you can add them to .git/info/exclude in that repository.

If you want to ignore certain files on every repository on your machine you can create the file ~/.gitignore_global and then run
ex: git config --global core.excludesfile ~/.gitignore_global

## 2020-11
Get the address that is set for the repository
```
git remote -v
```
Set address of the shortcut "origin" to correspond with the repository's
```
git remote set-url origin [new_address]
```
List all local branches
```
git branch --list
```

Get the name of the current branch
```
git symbolic-ref HEAD
```

Delete untracked files
```
git clean -df  
git checkout -- .
```

Get the list of remotes URLs that are registered locally
```
git remote -v
```

## 2021-05
See commits not pushed
```
git cherry -v origin/master
```
