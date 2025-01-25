""" import logging

logging.basicConfig(filename='log.txt',level=logging.WARNING)

print("This is a logging sample code...")

logging.info("this is a info message")
logging.debug("this is a debug message")
logging.critical("this is a debug message")
logging.error("this is a debug message")
logging.warning("this is a debug message")
 """

# Using logging module while handling exception


import logging

logging.basicConfig(filename='logger.txt', level=logging.INFO)

logging.info("=========NEW REQUEST==========")

try:
    x = int(input("Enter the 1st number: "))
    y = int(input("Enter the 2nd number: "))
    print(x/y)
except ZeroDivisionError as msg:
    print("Denominator cannot be 0")
    logging.exception(msg)
except ValueError as msg:
    print("Please enter only integer values..")
    logging.exception(msg)

logging.info("========REQUEST PROCESSED==========")

