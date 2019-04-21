#!/usr/bin/env python3
"""
    Purpose:
        Library for Logging the Execution Details of any callable
        or the main() function of a script.
"""

# Python Library Imports
import logging
from datetime import datetime
from wrapt import decorator


@decorator
def main_executor(wrapped, instance, args, kwargs):
    """
    Purpose:
        Decorator for running the main() function. Decorator will
        log the start and completion of the script, time the
        execution and performance of the script, and handle
        and exceptions (log the exception to the log file and raise)
    Args:
        wrapped (main function):
        instance: pass in self when wrapping class method.
            default is None when wrapping function.
        args (Tuple): List of arguments
        kwargs (Dict): Dictionary of named arguments
    """
    logging.info(
        "Starting Script: {function}. Args={args}, Kwargs={kwargs}".format(
            function="{0}->{1}".format(wrapped.__code__.co_filename, wrapped.__name__),
            args=args,
            kwargs=kwargs,
        )
    )

    start_time = datetime.now()
    try:
        wrapped(*args, **kwargs)
        execution_time = datetime.now() - start_time
        logging.info(
            "{function} Script Complete (Execution Time: {time})".format(
                function="{0}->{1}".format(
                    wrapped.__code__.co_filename, wrapped.__name__
                ),
                time=str(execution_time),
            )
        )
    except Exception as err:
        logging.error(
            "Error Running {function}: {err}".format(
                function="{0}->{1}".format(
                    wrapped.__code__.co_filename, wrapped.__name__
                ),
                err=err,
            ),
            exc_info=True,
        )
        raise err


@decorator
def function_executor(wrapped, instance, args, kwargs):
    """
    Purpose:
        Decorator for running any function. Decorator will
        log the start and completion of the function, time the
        execution and performance of the function, and handle
        and exceptions (log the exception to the log file and raise)
    Args:
        wrapped (any function):
        instance: pass in self when wrapping class method.
            default is None when wrapping function.
        args (Tuple): List of arguments
        kwargs (Dict): Dictionary of named arguments
    """
    logging.info(
        "Starting Fucntion Call: {function}. Args={args}, Kwargs={kwargs}".format(
            function=wrapped.__name__, args=args, kwargs=kwargs
        )
    )

    start_time = datetime.now()
    try:
        wrapped(*args, **kwargs)
        execution_time = datetime.now() - start_time
        logging.info(
            "{function} Script Complete (Execution Time: {time})".format(
                function=wrapped.__name__, time=str(execution_time)
            )
        )
    except Exception as err:
        logging.error(
            "Error Running {function}: {err}".format(
                function=wrapped.__name__, err=err
            ),
            exc_info=True,
        )
        raise err
