import logging


# Set up basic logging configuration
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(message)s')

def process_data(data):
    try:
        # Simulate some data processing that may raise different exceptions
        if data == "file_error":
            raise FileNotFoundError("File not found!")
        elif data == "value_error":
            raise ValueError("Invalid value provided!")
        else:
            return f"Processed {data}"
    
    except FileNotFoundError as e:
        logging.error(f"File error: {e}")
        print("File not found. Please check the file path.")
    
    except ValueError as e:
        logging.error(f"Value error: {e}")
        print("Invalid value provided.")

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print("An unexpected error occurred.")
    
    # Will only be executed if the try block doesn't raise any exceptions.
    else:
        print("Processing completed successfully.")
    
    # Will always execute no matter what

    finally:
        print("End of processing.")



if __name__ == "__main__":
    # Example usage
    process_data("file_error")
    print("\n")
    process_data("value_error")
    print("\n")
    process_data("valid_data")