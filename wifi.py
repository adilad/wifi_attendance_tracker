import subprocess
import pandas as pd
import os
from datetime import datetime
import logging

# Configure logging
log_file = 'attendance.log'
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_connected_wifi_network():
    try:
        # Run a shell command to get the currently connected WiFi network
        result = subprocess.run(["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-I"], capture_output=True, text=True)
        output = result.stdout

        # Search for the SSID in the output
        for line in output.splitlines():
            if line.strip().startswith("SSID:"):
                ssid = line.split(":")[1].strip()
                return ssid

        # If SSID is not found, return None
        return None

    except Exception as e:
        error_message = f"Error: {str(e)}"
        logging.error(error_message)
        print(error_message)
        return None

def is_date_already_present(file_name, date):
    # Check if the given date is already present in the Excel file
    if os.path.exists(file_name):
        df = pd.read_excel(file_name)
        return date in df['Date'].values
    return False

def save_data_to_excel(data):
    # Get the current date (without time)
    date = datetime.now().strftime('%Y-%m-%d')

    # Define the Excel file name (you can change this to your preferred location)
    file_name = 'attendance.xlsx'

    # Check if the date is already present in the Excel file
    if not is_date_already_present(file_name, date):
        # Create a DataFrame to store the data
        df = pd.DataFrame({'Date': [date], 'Connected WiFi Network': [data]})

    # Check if connected to wifi
    if data == "Wefi":
        present_in_office = 1
    else:
        present_in_office = 0

    # Check if the date is already present in the Excel file
    if not is_date_already_present(file_name, date):
        # Create a DataFrame to store the data
        df = pd.DataFrame({'Date': [date], 'Connected WiFi Network': [data], 'Present in Office': [present_in_office]})

        # Check if the file already exists
        if os.path.exists(file_name):
            df.to_excel(file_name, index=False, mode='a', header=False)  # Append without header
        else:
            df.to_excel(file_name, index=False)  # Create a new file with header

if __name__ == "__main__":
    connected_wifi = get_connected_wifi_network()
    if connected_wifi:
        info_message = f"Connected WiFi Network: {connected_wifi}"
        logging.info(info_message)
        print(info_message)
        save_data_to_excel(connected_wifi)
    else:
        error_message = "Not connected to a WiFi network."
        logging.error(error_message)
        print(error_message)
