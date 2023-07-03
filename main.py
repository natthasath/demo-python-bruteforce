import zipfile

def extract_zipfile(zip_path, password_file, extract_path):
    with open(password_file, 'r') as file:
        passwords = file.readlines()
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for password in passwords:
            password = password.strip()
            
            try:
                # Set the password for the ZIP file
                zip_ref.setpassword(password.encode('utf-8'))
                
                # Extract all files from the ZIP archive
                zip_ref.extractall(extract_path)
                
                print(f"Password found: {password}")
                break  # Exit the loop if password is found
            
            except Exception as e:
                # Handle incorrect password
                print(f"Password incorrect: {password}")
                continue

# Usage example
zip_file = 'download.zip'
password_file = 'password.txt'
extract_directory = 'extract/'

extract_zipfile(zip_file, password_file, extract_directory)
