# Ren'Py VSCode Project Template

This template includes VSCode tasks and extensions for developing Ren'Py projects.
- `bin/renpy`: macOS/linux script for calling Ren'Py SDK `renpy.sh`
- `bin/renpy.ps1`: Windows script for calling Ren'Py SDK `renpy.exe`
- `bin/set-origin.sh`: Git setup helper to configure your local folder to sync to a remote host
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

## Making your own GitHub repository

If you can run `git` on your command prompt (or powershell, etc), you can use it to synchronize your project to GitHub or other git provider.

If you don't have `git` or don't want to synchronize your project to a repository, skip to the next section.

1. Create a new repository from our simple template https://github.com/tiliv/renpy-vscode-template/generate.
   - The repository name you choose will not affect your Ren'Py project name.
2. Create a Ren'Py project on your computer or locate an existing project.
3. Open a command prompt in the directory your Ren'Py folder (the folder that contains `game/`).
4. Run the setup helper with the URL for your repository.  You may see a `.git` suffix on some urls, but you shouldn't include that suffix here.
```shell
bin/set-origin.sh 'https://github.com/USERNAME/REPOSITORY_NAME'
git push
```

## Using files directly (no repository)
1. [Download the template files to your computer](https://github.com/tiliv/renpy-vscode-template/archive/refs/heads/main.zip).
2. Extract the zip file into an existing Ren'Py **Project**.

NOTE: The zip archive will contain a hidden files like the `.vscode` folder.  If you are struggling to move `.vscode` into your project, open the unzipped folder in VSCode and use the VSCode UI to cut/paste the `.vscode` folder into your Ren'Py **Project** folder.

## Instructions to insert Toolkit in your repo 
I recommend the following ways to include it in your project:
- [**Pull branch**](https://github.com/DRincs-Productions/renpy-vscode-template#pull-branch) (to **insert** it into your game and **update** it easily)
- **Fork** (to improve the repo or create a Toolkit based on mine)

### Pull branch
To **insert** or **update** the Toolkit in your repo with Pull branch I recommend the following procedure:

(only if you want to insert the repo) Create a new empty branch, in the example I'll use **vscode-template**

`git checkout vscode-template`

`git pull https://github.com/DRincs-Productions/renpy-vscode-template.git main --allow-unrelated-histories`

At the end make a merge inside the arm of the project.

# Instructions for use

By default, opening a VSCode project will notify you of "recommended" extensions.  VSCode is notifying you that our `.vscode/extensions.json` is present, and allows you install them for you.  We include a task explorer panel and a Ren'Py language highlighter.  Neither is required, but both are useful.

Locate the Task Explorer panel to run your project-specific tasks:

<img width="536" alt="task-explorer" src="https://user-images.githubusercontent.com/618184/113932541-bb318880-97c1-11eb-9e94-d678eb4c665f.png">

To see the tasks without the Task Explorer extension, open VSCode's [Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) and search for `Tasks: Run Task`:

<img width="878" alt="tasks" src="https://user-images.githubusercontent.com/618184/113929032-8b808180-97bd-11eb-8e77-5cd00534776a.png">

To use the provided tasks, please first run the task `Ren'Py Setup: Set .renpy-sdk path`.  It will ask for the path to your Ren'Py SDK (where you unzipped it).  The folder name is something like `renpy-7.4.4-sdk`, and should NOT include any trailing slashes at the end.
- If I keep my SDK in `~/Applications/`, then the path would be `/Users/autumn/Applications/renpy-7.4.4-sdk`
- If I keep my SDK in `C:\Program Files\`, then the path would be `C:\Program Files\renpy-7.4.4-sdk`

A file will be created in the root of your workspace called `.renpy-sdk` with the path you entered inside it.  You can re-run the task to update it, or just modify the `.renpy-sdk` file directly.

The Windows-specific tasks will call on a `bin/renpy.ps1` helper script, while the non-Windows version will call on `bin/renpy`:

<img width="535" alt="all-tasks" src="https://user-images.githubusercontent.com/618184/113933305-6b06f600-97c2-11eb-84f7-f0c344dc23a3.png">

