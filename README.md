# Voxy WebStage Automated Tests

This project is part of a selection process for a sopt of Automation Tester in the Voxy team. This project contains a set of test cases for the Returning Login flow for Voxy’s platform located at: https://web-stage.voxy.com/v2/#/login. This test is set to run on both Windows OS and Linux distributions which have a Firefox Web browser installed.

## Requirements to run the Automate Test Script

* [Python 3](https://www.python.org/downloads/)
* [pip](https://pypi.org/project/pip/)
* [Firefox Web Browser](https://www.mozilla.org/pt-BR/firefox/new/)
* [Firefox GeckoDriver for Windows](https://sourceforge.net/projects/geckodriver.mirror/files/v0.30.0/geckodriver-v0.30.0-win64.zip/download) or [Firefox GeckoDriver for Linux](https://sourceforge.net/projects/geckodriver.mirror/files/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz.asc/download)

## Getting started

Go to the directory where requirements.txt is located and run the command below in your terminal.

```
pip install -r requirements.txt
```

After install all the packages, make sure you have Firefox installed in your computer, if not, install it.

The next step is to download the Firefox GeckoDriver in your computer (remember in which folder you place the GeckoDriver).

Go to the fixtures.py file and locate the method browser_firefox, then follow the instructions and type the path of the GeckoDriver you have just downloaded.

Then you should go to the terminal again and execute the following command.

```
behave --tags=script
```

And that is it, nothing more to be done.
Your Firefox browser should open and automatically execute the test cases for "email login.feature".

## How it is going to work

* After you write the behave command in your terminal, wait until the firefox browser opens automatically and execute the script.
* Afterwards, when all Scenarios defined in the gherkin file are done executing, the browser should automatically close.
* Finally, it should appear a list of all steps that were executed and their respective status, 
if they passed they will be green, if an error occured they will be red.

## Author

[Caio Pedreira](https://github.com/caiovvp)
