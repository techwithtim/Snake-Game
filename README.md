# Ren'Py VSCode Project Template

This template includes VSCode tasks and extensions for developing Ren'Py projects.
- `bin/renpy`: macOS/linux script for calling Ren'Py SDK `renpy.sh`
- `bin/renpy.ps1`: Windows script for calling Ren'Py SDK `renpy.exe`
- `.vscode/tasks.json`: Tasks for launching Ren'Py SDK commands without opening the Ren'Py launcher.
  - Set .renpy-sdk file (custom file for remembering your project's SDK path for commands to work)
  - Run
  - Lint
  - Force Recompile
  - Delete Persistent data
  - Distribute
- `.vscode/extensions.json`: Optional extensions that VSCode will offer to install for you
  - [Ren'Py Language](https://marketplace.visualstudio.com/items?itemName=LuqueDaniel.languague-renpy) for syntax highlighting
  - [Task Explorer](https://marketplace.visualstudio.com/items?itemName=spmeesseman.vscode-taskexplorer) for an easy clickable list of tasks from `.vscode/tasks.json`
- `.gitignore`: Git configuration file for ignoring certain file paths and types.
  - \*.rpyc/rpymc
  - log.txt, error.txt, traceback.txt

## Using files directly (no repository of your own)
1. [Download the template files to your computer](https://github.com/tiliv/renpy-vscode-template/archive/refs/heads/main.zip).
2. Extract the zip file into an existing Ren'Py **Project**.

NOTE: The zip archive will contain a hidden files like the `.vscode` folder.  If you are struggling to move `.vscode` into your project, open the unzipped folder in VSCode and use the VSCode UI to cut/paste the `.vscode` folder into your Ren'Py **Project** folder.

## Making your own GitHub repository

Alternatively, if you want to copy this template and also track your Ren'Py project files on GitHub, you may use the following steps instead.  Your Ren'Py project must already exist before you begin.

1. Install `git` for the command line (make sure you can type `git` in a command prompt or powershell, etc)
1. Create a new repository with by visiting https://github.com/tiliv/renpy-vscode-template/generate.  Note that github repositories tend to prefer lowercase names without spaces.  This name will only be used on GitHub and will not affect your Ren'Py project name.
3. Open a command prompt in your existing Ren'Py **Project** folder.
4. Confirm you are in the right location by typing `pwd` into your command prompt.  **Don't continue to step 5 unless you're sure you're using the right folder!**
5. Connect your **Repository** to your **Project** folder by running or pasting these commands in a command line.  You may run them one at a time if you prefer.
```shell
# This works the same for macOS, linux, and Windows
# Run this from a command prompt in your `/Your/RenPy/Project` folder.
git init
git remote add origin https://github.com/YOUR-ACCOUNT/YOUR-NEW-REPOSITORY.git  # replace this with your repo path
git fetch origin
git checkout -b main --track origin/main
git add -A
git push
```

# Instructions for use

Locate the Task Explorer panel to run your project-specific tasks.

<img width="536" alt="Screen Shot 2021-04-07 at 4 52 54 PM" src="https://user-images.githubusercontent.com/618184/113932541-bb318880-97c1-11eb-9e94-d678eb4c665f.png">

To see the tasks without the Task Explorer extension, open VSCode's [Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) and search for `Tasks: Run Task`:

<img width="878" alt="tasks" src="https://user-images.githubusercontent.com/618184/113929032-8b808180-97bd-11eb-8e77-5cd00534776a.png">

Before you can use the included Ren'Py tasks, run the task `Ren'Py Setup: Set .renpy-sdk path` and paste the path to your Ren'Py SDK.  The right path depends on where you unzipped the Ren'Py SDK.  The folder name is something like `renpy-7.4.4-sdk`, and should NOT include any trailing slashes at the end.
- If I keep my SDK in `~/Applications/`, then the path would be `/Users/autumn/Applications/renpy-7.4.4-sdk`
- If I keep my SDK in `C:\Program Files\`, then the path would be `C:\Program Files\renpy-7.4.4-sdk`

A file will be created in the root of your workspace called `.renpy-sdk` with the path you entered inside it.  You can re-run the setup task whenever you want to update this file, or modify the file directly.

You may mark relevant tasks as favorites.  The Windows-specific tasks will call on the `bin/renpy.ps1` helper script, while the non-Windows version will call on `bin/renpy`.
