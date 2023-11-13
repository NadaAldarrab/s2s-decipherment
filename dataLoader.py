import requests
import zipfile
import io
import os


def dataLader():
    
    # URL of the raw zip file
    url = "https://github.com/isi-nlp/s2s-decipherment-datafirst/raw/master/gutenberg-data.zip"

    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        response.raise_for_status()

        # Create a file-like object from the response content
        zip_file = zipfile.ZipFile(io.BytesIO(response.content))

        # Get the current working directory
        current_directory = os.getcwd()

        # Extract all the contents of the zip file in the current directory
        zip_file.extractall(current_directory)

        print("Zip file extracted successfully in the current directory.")
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
if __name__ == "__main__":
    dataLader()