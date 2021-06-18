# Automatic Syntax and Formatting Checks and Corrections

Here we use pre-commit hooks to identify issues with syntax and formatting before committing to a git repo.  
The formatting issues can be corrected automatically.

## I. Formatting Checks
1. Look at the [format violations module](../src/acc/format_violations.py).  What format violations do you see? 
2. Remove the `# fmt: off` and `#fmt: on` tags.
3. Type `git status` then `git add .` then `git commit`.   What happens?   
4. Type `git add .` then `git commit` again.  What happens this time? 
5. Look again at the [format violations module](../src/acc/format_violations.py).  What changed?  For reference, see the [pre-fix version](../pre-fixes/format_violations_pre_fix.py).

## II. Syntax Checks
1. Look at the [syntax violations module](../src/acc/syntax_violations.py).  What syntax violations do you see? 
2. Navigate to the [flake8 settings file](../.flake8) and remove `*syntax_violations*` from the `exclude` argument.
3. Type `git status` then `git add .` then `git commit`.   What happens?   
4. Type `git add .` then `git commit` again.  What happens this time?  
5. Fix up the module yourself.
6. Type `git add.` and then `git commit`. What happens?