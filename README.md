# moneyfy_app_automation
moneyfy_app_automation contains front end simulation using python

# Framework Used
`Unittest framework`
Python unit testing framework supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and independence of the tests from the reporting framework
`Page Object Model` and `Page Factory` using Appium.
Page Object Model, also known as POM, is a design pattern in Selenium that creates an object repository for storing all web elements.In Page Object Model, consider each web page of an application as a class file. Each class file will contain only corresponding web page elements. Using these elements, we can perform operations on the application under test.
It is useful in reducing code duplication and improves test case maintenance.
Helps with reusing code
It eases readability and reliability of scripts:


# tools required
`android studio for uiautomator`
`appium server GUI`
`node js`
`java`

#test report in debug log will have the overall testreport like how many passed and failed with details

# used ui automator for getting resources like id,xpath.

## Packages to be installed
pip3 install selenium,
pip install appium-python-client

`how to run`
navigate to testsuites and run test_monefy_ui.py from terminal

## Project structure

```
branch master
|
|_ src
|	|
|	|
|	|_ comm_utility (Utility classes)(Contains Action classes)
|   | 
|	|
    |-moneyfy_actions(contains driver instance and action methods)
    |
|	|_ testsuites ( test case scripts)
|
|_ debug_logs (Python debug logs and testreport)
```
