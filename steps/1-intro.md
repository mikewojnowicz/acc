# Introductory Material


## I. Clone the repo 

![clone](../pics/clone.jpeg)

1. Navigate to a directory in the terminal which will contain your copy of the `acc` repo locally.  (On Windows, you can use the Command Prompt or Git Bash).  To navigate use `cd` and `ls` if you are on Mac or Linux, `cd` and `dir` if you're on Windows.
2. Type `git clone https://github.com/mikewojnowicz/acc.git` in the terminal; this will clone the repository. You can see all the files in your folder (even the hidden ones), by using `ls -a`.
3. Type `cd acc` to navigate into the directory you just cloned. 

<div style="page-break-after: always;"></div>
<br>

## II. Virtual environment practice  

![virtualenv](../pics/virtualenv.jpeg)

`virtualenv` is a tool for constructing virtual environments for your Python project.
Virtual environments allow for isolated and reproducible dependencies.


1. Type `pip freeze` to see what python packages are installed globally. 
2. Type `virtualenv env` in the terminal to create a virtual environment. 
3. Type `ls .`.  Do you see a new folder called `env`?
4. Then type `source env/bin/activate` to activate the virtual environment.  (Windows users: see troubleshooting.)
5. Type `pip freeze` to see what packages are installed in the virtual environment.  What do you see?
6. Install a simple python package to your virtualenvironment by typing `pip install pip install typing-extensions==3.10.0.0`.   
7.  Type `pip freeze`.  What do you see?
8. Type `deactivate` to deactivate the virtual environment
9. Type `rm -rf env` to remove the virtual environment 
10.  Type `make env` to construct a new virtual environemnt, into which we install all dependencies from all requirements files into the virtual environment.  (Note: we could have also done `pip install -e .` and then `pip install -r requirements.txt dev-requirements.txt`.)
11. Type `source env/bin/activate`.  (Windows users: see troubleshooting.)
12. Type `pip freeze`.  What do you see?
13. What version of `pytest` do you have installed?  Type `pip freeze | grep pytest`.  
14. For a better understanding of virtual environments, there is a short chapter on this in the excellent book by Brett Slatkin, [Effective Python](https://www.oreilly.com/library/view/effective-python-59/9780134034416/).

<div style="page-break-after: always;"></div>
<br>
