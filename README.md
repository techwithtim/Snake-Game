## Insert Lib in your Project

I recommend the following ways to include it in your project:

- [**Pull branch**](#pull-branch) (to **insert** it into your game and **update** it easily)
- [**Fork**](https://docs.github.com/en/get-started/quickstart/fork-a-repo) (to improve the repo or create a Toolkit based on mine)
- [Manually](https://github.com/DRincs-Productions/renpy-template-debug-vscode/releases) (not recommended)

### Pull branch

To **insert** or **update** the Toolkit in your repo with Pull branch I recommend the following procedure:

(only if you want to insert the repo) Create a new empty branch, in the example I'll use **vscode-template**

```shell
git checkout -b renpy-utility-lib
git checkout renpy-utility-lib
git config pull.rebase false
git pull https://github.com/DRincs-Productions/renpy-utility-lib.git tool-only --allow-unrelated-histories
git submodule update --remote

```
