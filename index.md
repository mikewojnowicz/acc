## Description

Software engineering tools are not pervasively used by academic researchers, but they can make life doing research much easier. This workshop describes how to incorporate automatic code checking into your workflow.  Automatic code checking can help identify serious code issues before they bite you, and can help automate otherwise tedious tasks. In particular, we will introduce students to unit testing, syntax checking, and code formatting. We will motivate why you would want to integrate these things into your workflow, and we will demonstrate by applying various Python packages (pytest, pylint, black, and sort) to specific examples. We will also discuss how to automate the application of these tools via Makefiles and pre-commit hooks. 

## Goals

* Gain experience with writing and using unit tests (via pytest)
* In tandem, gain experience with virtualenvs, Makefiles, and python debugging  
* ...and more.  Stay tuned! 


## Before the workshop

1. If you have never used the terminal / command prompt before, go through this [introductory tutorial](https://tutorial.djangogirls.org/en/intro_to_command_line/). The tutorial covers commands such as `ls` (for Mac and Linux users), `dir` (for Windows users), and `cd` (for everyone). (0-15 min)
2. Install Git, following these [instructions](https://karink520.github.io/git-and-github-intro/install_git.html). (0-10 min)
3. Make sure you have Python (ideally 3.x).  (0-15 min)
4. If you haven't already, install (0-5 min)

    * [pip](https://pip.pypa.io/en/stable/installing/): This probably came with your Python installation, unless you’re on Linux and installed using your OS package manager.
    * _virtualenv_:  Just do `pip install virtualenv`.  

## Workshop materials
[Workshop instructions](workshop_instructions.md)
