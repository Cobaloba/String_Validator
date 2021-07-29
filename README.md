
# Valid Sentence Coding Test

A command line interface program to test the validity of strings based on a set of rules.


## Requirements

This project requires Python3 to be installed. To install: https://www.python.org/downloads/

  
## Run Locally

To run this project, run the following command from within the String_Validator directory:

```bash
  python3 String_Validity_V1.py
```
You  will be greeted with a list of tests that can be ran against an input phrase. 
Enter a test phrase and press enter. You will then be prompted to enter tests to run. 
Multiple tests can be ran simultaneously by seperating by commas, e.g:
```bash
  Enter tests to perform, numbers above seperated by commas (blank for all tests): 
  1,3,4,5
```
All tests can be performed by submitting blank.

The result will be returned in JSON format, stating true or false for each test, 
and an overall result of validity for the chosen tests.

Tests are as follows:

Tests:
 * 1 - String starts with a capital letter
 * 2 - String has an even number of quotation marks
 * 3 - String ends with a period character “."
 * 4 - String has no period characters other than the last character 
 * 5 - Numbers below 13 are spelled out (”one”, “two”, "three”, etc…)


## Running unit Tests

To run unit tests, run the following command from within the String_Validator directory:

```bash
  python3 test_String_Validity.py
```

