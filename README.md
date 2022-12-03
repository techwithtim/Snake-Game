# Debug and Template (VSCode) Ren'py

This template includes VSCode launchs and extensions for developing Ren'Py projects.

## File

- `bin/renpy`: macOS/linux script for calling Ren'Py SDK `renpy.sh`
- `bin/renpy.ps1`: Windows script for calling Ren'Py SDK `renpy.exe`
- `bin/set-origin.sh`: Git setup helper to configure your local folder to sync to a remote host
- `.vscode/launch.json`: Launch for launching Ren'Py SDK commands without opening the Ren'Py launcher.
  - Setup (custom file for remembering your project's SDK path for commands to work)
  - Run
  - Force Recompile & Run
  - Delete Persistent
  - Lint
  - Distribute
- `.vscode/extensions.json`: Optional extensions that VSCode will offer to install for you
- `.vscode/settings.json`: For Test Formatting, and other settings
  - [Ren'Py Language](https://marketplace.visualstudio.com/items?itemName=LuqueDaniel.languague-renpy) for syntax highlighting
  - [Power Shell](https://marketplace.visualstudio.com/items?itemName=ms-vscode.PowerShell) for an easy clickable list of launchs from `.vscode/launch.json`
  - [Python](https://marketplace.visualstudio.com/items?itemName=spmeesseman.vscode-taskexplorer) for python syntax highlighting
- `.gitignore`: Git configuration file for ignoring certain file paths and types.
- `/game/tool/utility.rpy`: Useful functions such as: isNullOrEmpty 
- `/game/tool/flags.rpy`: Flags System
- `/game/tool/notify.rpy`: Notify System
- `/game/tool/log_system.rpy`: Log System

## How Run Debug (F5)

![image](https://user-images.githubusercontent.com/67595890/179401467-c8abbc9b-8970-4bad-af86-2b5b31c173a4.png)


### Setup

( **Necessary only in the beginning** )

Paste the path to your Ren'Py SDK folder

### Run

Select:

- Run or
- Force Recompile & Run

And Play!

#### For Linux first:

```bash
chmod +x renpy.sh
chmod +x renpy.py
chmod +x renpy.exe
chmod +x lib/py3-linux-x86_64/renpy
chmod +x lib/py3-linux-x86_64/pythonw
sudo apt-get install -y xdg-utils

```

when opening the text with error info via terminal, write:

```bash
:q

```


if this:

![image](https://user-images.githubusercontent.com/67595890/181924847-19e28398-259a-4ca0-831a-da72410e4612.png)


them:

```bash
sudo apt-get install -y yad

```

#### For microsoft wsl
https://docs.microsoft.com/it-it/windows/wsl/tutorials/gui-apps


## Insert Template in your Project

I recommend the following ways to include it in your project:

- [**Pull branch**](#pull-branch) (to **insert** it into your game and **update** it easily)
- [**Fork**](https://docs.github.com/en/get-started/quickstart/fork-a-repo) (to improve the repo or create a Toolkit based on mine)
- [Manually](https://github.com/DRincs-Productions/renpy-template-debug-vscode/releases) (not recommended)

### Pull branch

To **insert** or **update** the Toolkit in your repo with Pull branch I recommend the following procedure:

(only if you want to insert the repo) Create a new empty branch, in the example I'll use **vscode-template**

```shell
git checkout -b vscode-template
git checkout vscode-template
git config pull.rebase false
git pull https://github.com/DRincs-Productions/debug-and-template-VSCode-renpy.git tool-only --allow-unrelated-histories

```

At the end make a merge inside the arm of the project.

### Fix Common
```regex
    # renpy/common/(.*)
    old "###########"
    new "(.*)"
```

```regex
    # # renpy/common/(.*)
    # old "###########"
    # new "(.*)"
```
