import os

def verify_file_path(file_path):
    try:
        
        absolute_path = os.path.abspath(file_path)
        print(f"Absolute Path: {absolute_path}")

        
        file_exists = os.path.exists(absolute_path)
        print(f"File Exists: {file_exists}")

        
        can_read = os.access(absolute_path, os.R_OK)
        print(f"Can Read: {can_read}")

        
        if file_exists and can_read:
            with open(absolute_path, 'r') as file:
                print(file.read())
        else:
            print("File does not exist or cannot be read.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
verify_file_path('data\\vandalism\\data.yaml')