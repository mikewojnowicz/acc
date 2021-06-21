
## Description

Software engineering tools are not pervasively used by academic researchers, but they can make life doing research much easier. This workshop describes how to incorporate automatic code checking into your workflow.  Automatic code checking can help identify serious code issues before they bite you, and can help automate otherwise tedious tasks. In particular, we will introduce students to unit testing, syntax checking, and code formatting. We will motivate why you would want to integrate these things into your workflow, and we will demonstrate by applying various Python packages (pytest, pylint, black, and sort) to specific examples. We will also discuss how to automate the application of these tools via Makefiles and pre-commit hooks. 

## Before the workshop

Please follow these steps, in order of priority:

1. Make sure you have Python (ideally 3.x).  (0-15 min)
2. If you haven't already, install the following (0-5 min)

    * [pip](https://pip.pypa.io/en/stable/installing/): This probably came with your Python installation, unless you’re on Linux and installed using your OS package manager.
    * _virtualenv_:  Just do `pip install virtualenv`.  
    * _tox_: Just do `pip install tox`. 
3. If you have never used the terminal / command prompt before, go through this [introductory tutorial](https://tutorial.djangogirls.org/en/intro_to_command_line/). The tutorial covers commands such as `ls` (for Mac and Linux users), `dir` (for Windows users), and `cd` (for everyone). (0-15 min)
4. Install Git, following these [instructions](https://karink520.github.io/git-and-github-intro/install_git.html). (0-10 min)


# Tutorial Steps

1. [Introductory Material](./steps/1-intro.md)
2. [Unit tests](./steps/2-unit-tests.md)
3. [Syntax and formatting](./steps/3-syntax-and-formatting.md)

# Troubleshooting

The tutorial has only been tested on a Mac.   However, see [known troubleshooting tips for windows users](./troubleshooting.md). We will likely need to figure out further adjustments for Windows (and perhaps even Linux) live.  


