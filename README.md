We use Python and Selenium Webdriver

Note: This was only tested with chrome webdriver on Windows although it should also work in Linux (chrome only)

The Project contains the following files:
----------------------------------------
locators.py (selenium locators)
page.py (all page objects)
Tests.py (unittest - for running the test)
TestsData.py (Test Data: Facebook user/pass, Name & Birthday) - Don't forget to fill it before launching the suit

How to Run the Test Suite:

Prerequisite:
-------------
* Python 3.8.0 Installed https://www.python.org/downloads/
* Selenium Webdriver for Python: https://selenium-python.readthedocs.io/installation.html
* Chrome Webdriver for the installed chrome version placed it the repository's root folder: https://chromedriver.chromium.org/downloads
  **The chromedriver.exe in this repository is for chrome 78 (windows)


Run:
---
Change Directory to the project's root folder
If you have not install Selenium Webdriver for Python, please do so now (pip install selenium)
run: python Tests.py

**I recommend using PyCharm


