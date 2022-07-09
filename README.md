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

## Insert Template in your Project

I recommend the following ways to include it in your project:

- [**Pull branch**](#pull-branch) (to **insert** it into your game and **update** it easily)
- [**Fork**](https://docs.github.com/en/get-started/quickstart/fork-a-repo) (to improve the repo or create a Toolkit based on mine)
- [Manually](https://sites.northwestern.edu/researchcomputing/resources/downloading-from-github/#:~:text=To%20do%20this%2C%20go%20to,likely%20in%20your%20Downloads%20folder.) (not recommended)

### Pull branch

To **insert** or **update** the Toolkit in your repo with Pull branch I recommend the following procedure:

(only if you want to insert the repo) Create a new empty branch, in the example I'll use **vscode-template**

```shell
git checkout -b vscode-template
git checkout vscode-template
git pull https://github.com/DRincs-Productions/renpy-template-debug-vscode.git tool-only --allow-unrelated-histories
```

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
