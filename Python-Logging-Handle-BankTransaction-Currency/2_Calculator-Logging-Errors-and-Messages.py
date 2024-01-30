import logging
import sys
     
logger = logging.getLogger(__name__)         
logger.setLevel(logging.DEBUG)         
file_handler = logging.FileHandler("formatted.log")   
stream_handler = logging.StreamHandler(sys.stdout)
logging.basicConfig(filename='basic_config.log', level=logging.DEBUG, format='[%(asctime)s] - %(levelname)s - %(message)s')

formatter1=logging.Formatter("[%(asctime)s] {%(levelname)s} %(name)s: #%(lineno)d - %(message)s" )
file_handler.setFormatter(formatter1)

formatter2=logging.Formatter("[%(asctime)s] {%(levelname)s} - %(message)s")
stream_handler.setFormatter(formatter2)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

def division():
  logger.debug("Starting Division! ")
  try:
    dividend = float(input("Enter the dividend: "))
    logger.info(dividend)
    divisor = float(input("Enter the divisor: "))
    logger.info(divisor)
  except ValueError:
    logger.log(logging.CRITICAL, "No dividend or divisor value entered!")
    return
  if divisor == 0:
    logger.error("Attempting to divide by 0!")
    return
  else:
    return dividend/divisor
result = division()
if result == None:
  logger.warning("The result value is None!")
