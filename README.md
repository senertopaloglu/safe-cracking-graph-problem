# A Graph Problem: Safe Cracking

This repo contains my submission to a DSA problem that came up during a discussion with my peers. Please find the problem brief below.

### Problem brief
Oh-no! You forgot the number combination that unlocks your safe. Luckily, you knew that you'd be forgetful so you previously wrote down a bunch of hints that can be used to determine the correct combination. Each hint is a pair of numbers 'x, y' that indicates you must enter digit 'x' before 'y' (but not necessarily immediately before y).

The keypad on the safe has digits 0-9. You can assume that the hints will generate exactly one working combination and that a digit can occur zero or one time in the answer.

Write a function, safe_cracking, that takes in a list of hints as an argument and determines the combination that will unlock the safe. The function should return a string representing the combination.

### How to run
#### Prerequisites
Please ensure Python is installed and added to the PATH. Test suite is executed using the `unittest` module - please ensure this module is installed by running `pip install unittest` in the terminal.  

#### Instructions
1. `git clone` this repository
2. `cd` into project folder on local machine
3. execute tests using `python test.py`

### Further steps
* Add more tests to cover edge cases.