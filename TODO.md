## Convert Local to Instance Variable

Converts a local variable into an instance variable, creates the property and renames all the occurrences in the selected method to use the instance variable:

    php refactor.phar convert-local-to-instance-variable <file> <line> <variable>


## Rename Class and Namespaces

Batch Operation to rename classes and namespaces by syncing class-names (IS-state) to filesystem names (SHOULD-state) based on the assumption of PSR-0.

Fix class and namespace names to correspond to the current filesystem layout, given that the project uses PSR-0. This means you can use this tool to rename classes and namespaces by renaming folders and files and then applying the command to fix class and namespaces.

    php refactor.phar fix-class-names <dir>


## Optimize use statements

Optimizes the use of Fully qualified names in a file so that FQN is imported with "use" at the top of the file and the FQN is replaced with its classname.

All other use statements will be untouched, only new ones will be added.

    php refactor.phar optimize-use <file>
