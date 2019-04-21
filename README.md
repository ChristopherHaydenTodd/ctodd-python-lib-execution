# Christopher H. Todd's Python Library For Wrapping Callable Execution

The ctodd-python-lib-execution project is responsible for warpping callables in Python to wrap in function logging, execution time, and other quality of life improvements. Useful for wrapping functions with start and stop timers.

## Table of Contents

- [Dependencies](#dependencies)
- [Libraries](#libraries)
- [Example Scripts](#example-scripts)
- [Notes](#notes)
- [TODO](#todo)

## Dependencies

### Python Packages

- wrapt>=1.11.1

## Libraries

### [function_executors.py](https://github.com/ChristopherHaydenTodd/ctodd-python-lib-execution/blob/master/execution_helpers/function_executors.py)

Library for Logging the Execution Details of any callable or the main() function of a script.

Functions:

```
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
```

## Example Scripts

Example executable Python scripts/modules for testing and interacting with the library. These show example use-cases for the libraries and can be used as templates for developing with the libraries or to use as one-off development efforts.

### N/A

## Notes

 - Relies on f-string notation, which is limited to Python3.6.  A refactor to remove these could allow for development with Python3.0.x through 3.5.x

## TODO

 - Unittest framework in place, but lacking tests
