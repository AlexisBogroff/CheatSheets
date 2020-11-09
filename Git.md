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
