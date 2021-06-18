# Unit tests

## I. Exploring unit tests, the Makefile, and virtualenvs

![explore](../pics/explore.jpeg)

Unit tests usually live in `tests/unit/`, and test that functions in the source code behave as expected.  For an example, see [here](https://github.com/mikewojnowicz/acc/blob/master/tests/unit/test_arithmetic.py).

1. Type `make test` to run your first test.  What happened?  What assertion failed?
2. Inspect the `Makefile` to determine what `make test` is doing.   
3. Can you replicate `make test` by typing a command directly into the terminal? What is it? What does it do?
4. You can also run a specific test from a specific module.
Try `pytest -sv tests/unit/test_arithmetic.py::test__add_numbers_incorrectly`
5. Type `deactivate` and then rerun that same command.  What happens?  Why?   
6. Launch ipython and type `import acc`.  What happens?  Why?
7. Type `source env/bin/activate`, launch ipython, and type `import acc`.  What happens? Why?
8. Type `mkdir ~/tmp && cd ~/tmp` to create a temporary directory.  Then type `git clone https://github.com/mikewojnowicz/acc.git` to clone a fresh copy of `acc`.  Then launch and activate a virtual environment.   Then type `pip install -e .`  
Then launch ipython and type `import acc`.  What happens?  Why?

## II. Exploring unit tests and the python debugger


![debug](../pics/debug.png)

1. Navigate to `tests/unit/test_arithmetic.py`, and move the `pytest.mark.skip` decorator from ` test__add_numbers_incorrectly__with_random_numbers` to  `test__add_numbers_incorrectly`.
2. Type `make test` to run the tests.  What happened?  
3. Type `make test` again to run the tests again.  Do you get the same result?   Why? Is this desirable?  What could you change if you wanted a different result?
5. We would like to know the values of `x` and `y` for `test_add_numbers_incorrectly_with_random_numbers`.  Run `make test-pdb` and navigate the debugger to determine the values of `x` and `y`.  
4. How could you replicate this procedure in the previous item without using the Makefile?
5. (Optional) Would you like to debug in Ipython rather than the python debugger `pdb`?   If so, then create a file called `~/.pdbrc`.  Add the single line `alias ipy from IPython import embed; user_ns=locals(); user_ns.update(globals()); embed(user_ns=user_ns)`.  Now rerun `make test-pdb` and from the debugger, type `ipy`.  This will launch an ipython instance from the debugger where both local state and global state is maintained.  Confirm the former by typing `x` and `y` into ipython.  Confirm the latter by typing `add_numbers_incorrectly(x,y)`.
6. See if you can diagnose the problem with `add_numbers_incorrectly` WITHOUT looking at the source code.  Run `make test-pdb`,
enter the debugger (perhaps interactively, using an embedded IPython instance), and play around with various values until you come to a hypothesis.
7. Check the source code to see if your hypothesis is correct.
8. Fix the source code, and rerun all tests using `make test`.   Did you fix the problem?

## III.  Writing your own tests 

This section is stolen from [catinabox](https://github.com/keeppythonweird/catinabox)

![catinabox](../pics/catinabox.png)


If you get stuck, [take a peek at the solution](../solutions/test_catmath.py).

1. We will be writing tests for [catmath.py](../src/acc/catmath.py).
   This module contains only one function ```cat_years_to_hooman_years```.

2. Look at [the existing tests](../tests/unit/test_catmath.py). You can see there
   are test stubs:
   
   * ```test__cat_years_to_hooman_years__middle_age__succeeds```
   * ```test__cat_years_to_hooman_years__less_than_one_year__succeeds```
   * ```test__cat_years_to_hooman_years__0__returns_0```
   
3. Fill in the body of these tests. Based on their names, what test case do
   you think each of these is trying to cover?
   
   Each test should be calling ```cat_years_to_hooman_years``` with different
   input and asserting based on the output.

4. When you have filled in the body of these tests, run them with `make test`