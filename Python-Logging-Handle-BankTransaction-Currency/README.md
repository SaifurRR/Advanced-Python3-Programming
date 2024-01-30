# Logging in Python

### 1. Currency-Converter-Logging
[2023-12-08 04:44:41,987] DEBUG [Current rates: {'USD': 1.0, 'EUR': 0.861775, 'GBP': 0.726763, 'INR': 75.054725, 'AUD': 1.333679, 'CAD': 1.237816, 'SGD': 1.346851}]
DEBUG:__main__:Current rates: {'USD': 1.0, 'EUR': 0.861775, 'GBP': 0.726763, 'INR': 75.054725, 'AUD': 1.333679, 'CAD': 1.237816, 'SGD': 1.346851}
   
[2023-12-08 04:44:41,997] INFO [Converting from EUR to USD: 52.217806271938734]
INFO:__main__:Converting from EUR to USD: 52.217806271938734  

[2023-12-08 04:44:42,000] INFO [Converting from USD to USD: 52.217806271938734]
INFO:__main__:Converting from USD to USD: 52.217806271938734
52.217806271938734

### 2. Logging-Errors-and-Messages
<Logger __main__ (WARNING)>

Dividend: 6
Divisor: 0

Attempting to divide by 0!
The result value is None!


### Project: ATM-Logging

The goal of this project is to modify the existing BankAccount methods to utilize the logging module instead of print statements. Using the logging module over print statements will help make the project code more readable and maintainable after these modifications are made.
