# Ren'Py VSCode Project Template

This repository is a template for VSCode tasks and extensions for developing Ren'Py projects.

# Using files directly (no repository of your own)
1. [Download the template files to your computer](https://github.com/tiliv/renpy-vscode-template/archive/refs/heads/main.zip).
2. Extract the zip file into an existing Ren'Py **Project**.

NOTE: The zip archive will contain a hidden `.vscode` folder.  If you are struggling to move `.vscode` into your project, open the unzipped folder in VSCode and use the VSCode UI to cut/paste the `.vscode` folder into your Ren'Py **Project** folder


# Making your own GitHub repository

Alternatively, if you want to copy this template and also track your Ren'Py project files on GitHub, you may use the following steps instead.  Your Ren'Py project must already exist before you begin.

1. Install `git` for the command line (make sure you can type `git` in a command prompt or powershell, etc)
1. Create a new repository with by visiting https://github.com/tiliv/renpy-vscode-template/generate.  Note that github repositories tend to prefer lowercase names without spaces.  This name will only be used on GitHub and will not affect your Ren'Py project name.
3. Open a command prompt in your existing Ren'Py **Project** folder.
4. Confirm you are in the right location by typing `pwd` into your command prompt.  **Don't continue to step 5 unless you're sure you're using the right folder!**
5. Connect your **Repository** to your **Project** folder by running or pasting these commands in a command line.  You may run them one at a time if you prefer.
```shell
# This works the same for macOS, linux, and Windows
# Run this from a command prompt in /Your/RenPy/Project folder.
git init
git remote add origin https://github.com/YOUR-ACCOUNT/YOUR-NEW-REPOSITORY.git  # replace this with your repo path
git fetch origin
git checkout -b main --track origin/main
git add -A
git push
```
