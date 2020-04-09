# submarino-testing

## Preparing the execution
Before the test run, you have to change the directory of chromeDriver in SearchTest.py (lines 10 and 11) and CartTest.py (lines 11 and 12) to the directory of chromeDriver in your computer. 

*Example: "C:\Users\Vagno\PycharmProjects\submarino-testing\web-automation-submarino\chromedriver.exe"*

## Create virtual env
1. python -m virtualenv env
2. env\Scripts\activate

## How to execute?
1. pip install -r requirements.txt (linux) or "path\pip.exe" install -r requirements.txt (windows)
2. cd TestSuite 
3. pytest --html=TestingSubmarinoReport.html TestSuite.py

## Python3 Version
Python 3.7.0

## Testing Plan
In [this](https://github.com/wagnerlucas/submarino-testing/blob/master/Testing%20Plan%20-%20Submarino%20website.pdf) file is explained a little bit more about the test and the test scenarios

