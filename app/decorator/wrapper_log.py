import logging

# Configure logging
logging.basicConfig(filename='data/log/LOGS_WRAPPER.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def wrapper_log(process):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                logging.info(f"{func.__name__}() executed successfully. -> " + process + " - SUCESSO")
                return result
            except Exception as e:
                error_message = f"An error occurred in {func.__name__}: {e} -> " + process
                logging.error(error_message)
                raise Exception(error_message)
        return wrapper
    return decorator


