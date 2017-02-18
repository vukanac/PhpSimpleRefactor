WukanacPhpSimpleRefactor for Sublime Text
=========================================

A simple way to integrate [PHP Refactoring Browser]'s method extraction in Sublime Text 3 

Requirements
------------

### refactor.phar

You need to have PHP installed and [PHP Refactoring Browser]'s `refactor.phar` file.

Download `refactor.phar`, eg. in:

* `d:\bin\` for Win,
* `~/bin/`  for OsX or Linux.

Add `bin/` to `PATH`.

Must be executable.

### patch

To use refactor you also need `patch` on your system.

Check it with:

    $ which patch

If you are Windows user you will have to specify `patch` command path.

When you are using Git Bash it's located at:

    c:/Users/<Your User Name>/AppData/Local/Programs/Git/usr/bin/patch.exe


Or download `patch.exe` binary to your desired location.


Installation
------------

--The package (PhpSimpleRefactor) is available on [Package Control](https://sublime.wbond.net/).--

* In Sublime Text Editor,
* Open > Preferences
* Open > Browse Packages

Folder should be `/Sublime Text 3/Packages/`.

In that folder open terminal and clone repo:

    git clone https://github.com/vukanac/PhpSimpleRefactor.git WukanacPhpSimpleRefactor
    cd WukanacPhpSimpleRefactor
    git checkout feature/config-patch-tool

Patch tool should be configurable for Windows user, as it is suggested to use `--binay` flag.


Configuration
------------

Edit the file WukanacPhpSimpleRefactor.sublime-settings,  
[Preferences > Package Settings > WukanacPhpSimpleRefactor > Settings – User]  
with the correct:

Example:

    /** FILE: WukanacPhpSimpleRefactor.sublime-settings **/
    {
        "php_path" : "",
        "refactor_path" : "/home/dev/bin/refactor.phar",
        "patch_path" : "patch",
        "patch_opts" : "--binary",
    }

If php is globaly accessible `php_path` can be left empty.

Parameter `refactor_path` can contains only `patch` if you have `patch` in PATH.

Parameter `patch_path` can contains only `patch` if you have `patch` in PATH.


For key short-cut, in `Preferences > Key Bindings - User` add this line:

    [
        { "keys": ["ctrl+shift+e"], "command": "wukanac_php_simple_refactor_extract_method" },
        { "keys": ["ctrl+shift+r"], "command": "wukanac_php_simple_refactor_rename_local_variable" }
    ]




Usage
=====
There are two functionalities:

**Extract method:** Select the lines that you'd like to extract to a new method,
and use the shortcut **`ctrl+shift+e`**
(or right click on the text and select "**WukanacPhpSimpleRefactor -> Extract method**").
The plugin will ask you for the method name to use. 

**Rename local variable:** Right click inside the scope that contains the local variable that you want to rename and select "**WukanacPhpSimpleRefactor -> Rename local variable**".
The plugin will ask you for the variable old name and the new name.


License
----

MIT

[PHP Refactoring Browser]:https://github.com/QafooLabs/php-refactoring-browser
