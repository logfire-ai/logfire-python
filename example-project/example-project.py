# This is an example project of Logfire python integration
# This project showcases how to use Logfire in your python projects
# For more infromation please visit https://github.com/logfire-sh/logfire-python

# SETUP

# Import Logfire client library and deault logging library
from logfire import LogfireHandler
import logging
import sys

# Check for program arguments
if len(sys.argv) != 2:
    print("Program requires source token as an argument, run the program as followed\npython example-project.py <source-token>")
    sys.exit()

# Create handler
handler = LogfireHandler(source_token=sys.argv[1])

# Create logger
logger = logging.getLogger(__name__)
logger.handlers = []
logger.setLevel(logging.DEBUG) # Set minimal log level
logger.addHandler(handler) # asign handler to logger

# LOGGING EXAMPLE
# Following code shocases logger usage

# Send debug log using the debug() method
logger.debug('I am using Logfire!')

# Send info level log about interesting events using the info() method
logger.info('I love Logfire!')

# Send warning level log about warrying events using the warning() method
# You can also add a custom structured information to the log by passing it as a second argument
logger.warning('Log structured data', extra={
    'item': {
        'url': "https://my-store.com/order-1",
        'item': "my-item"
    }
})

# Send error level log about errors in runtime using the error() method
logger.error('Oops! An error occured!')

# Send critical level log about critical events in runtume using the critical() method
logger.critical('Its not working, needs to be fixes ASP!')

# Send exception level log about errors in runtime using the exception() method
# Error level log will be sent. Exception info is added to the logging message. 
# This method should only be called from an exception handler.
try:
    nonexisting_function() # Calling nonexisting function
except Exception as Argument:
    logger.exception("Error occurred while calling non-existing function") # Additional info will be added
    # OUTPUT:
    # Error occurred while calling non-existing function
    #Traceback (most recent call last):
    #   File "logfire.py", line 48, in
    #       nonexisting_function()
    #NameError: name 'nonexisting_function' is not defined

print('All done! You can check your logs now.')