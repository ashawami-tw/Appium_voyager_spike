# Appium_voyager_spike

# Installation
A. For Appium Setup
1. Java 8
2. Node.js
3. Appium - Install appium using npm ``npm install -g appium``
4. Android Studio

B. For Appium Project Setup
1. Python
2. Clone Project
3. Install all dependencies from requirements.txt by following command
   `` pip install -r requirements.txt `` or ``pip3 install -r requiremnets.txt``
# Folder Structure

# Run Test
  Before running any test make sure the emulator devices are opened
  can use follwoing command to open them - ``emulator @<device_name>``
  1. Run all tests - ``pytest``
  2. Run particular test - ``pytest ./test/<test_name>``
  3. Run tests parallelly - ``pytest -n <number_of_tests_want_to_run_parallelly>``
  
# Reporting
  1. Run all tests to generate report - ``pytest --html=<file_name.html>``
  
# Reference
  1. Refer for Appium, Android Studio setup - https://rahulshettyacademy.com/blog/index.php/2021/07/25/clone-of-get-started-with-appium/
