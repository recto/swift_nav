# Swift Navigation project
## Overview
This is from [mookerji/Application Question](https://gist.github.com/mookerji/ef85e76e8bbfb6539643). This is done for Software, Product, and Embedded Engineering Candidates. The following is the instruction given at the time when I worked on.

In the programming language of your choice, write a program generating the first n Fibonacci numbers F(n), printing ...
- ... "Buzz" when F(n) is divisible by 3.
- ... "Fizz" when F(n) is divisible by 5.
- ... "BuzzFizz" when F(n) is prime.
- ... the value F(n) otherwise.

Bonus points for efficient implementation, testing, documentation, 
and/or upload your code to GitHub.

## Language and Prerequisites
This application is written in Python. Please note this is written based on Python 2.7. This would not work with Python 3. (Note: some functions like xrange are used but those don't exist in Python 3.)

## Installation
You can git clone against https://github.com/recto/swift_nav.git or download it into your local environment.

## Content
You will find the following in your workspace.
* README.md - this file.
* src/application.py - application main
* test/test_application.py - Test cases for application

## Usage
* Start terminal for Linux/Mac OS X, command prompt for Windows.
* Make sure you have Python 2.7 in your environment. (i.e. check it by python --version)
* Change the directory to **your workspace**/src.
* Perform 'python application.py **n**' whereas **n** is the number of Fibonacchi numbers. (e.g. python application.py 10) 
* Check the output.

## Test Cases
Test cases are available at **your workspace**/test directory. You can run it as below: 
* Start terminal for Linux/Mac OS X, command prompt for Windows.
* Make sure you have Python 2.7 in your environment. (i.e. check it by python --version)
* Change the directory to **your workspace**/test.
* Perform 'python test_application.py'
* Make sure all test cases pass.
