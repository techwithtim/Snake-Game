git init
git remote add origin $1.git
git fetch origin
git checkout -b main --track origin/main
git add -A
git commit -m "Add new project files"
