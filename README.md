# Wi-Fi based Attendance

This Python script logs the currently connected Wi-Fi network and generates an Excel record based on the Wi-Fi network name. It's designed to be run as a cron job on macOS.

## Usage

1. **Clone or Download Repository**: Clone or download this repository to your local machine.

2. **Install Python and Dependencies**:
   - Ensure you have Python 3.x installed. You can use Homebrew to install Python on macOS:
     ```bash
     brew install python@3.x
     ```
   - Install the required Pandas library using pip:
     ```bash
     pip install pandas
     ```

3. **Edit Crontab**:
   - Open your terminal and run the following command to edit your crontab file:
     ```bash
     crontab -e
     ```
   - Add the following line to schedule the script to run every hour (adjust paths as needed):
     ```cron
     0 * * * * /opt/homebrew/bin/python3 /Users/user1/PycharmProjects/wifi.py
     ```
   - Save and exit the text editor.

4. **Script Location**:
   - Ensure that the script (`wifi.py`) is located in the specified directory (`/Users/user1/PycharmProjects/`) and is executable. You may need to adjust the path and filename according to your setup.

5. **Automated Execution**:
   - The script will run automatically every hour, log the connected Wi-Fi network, and generate an Excel record.
   - The Excel log file is named `attendance.xlsx` and will be saved in the same directory as the script.

## Requirements

- Python 3.x
- Pandas library (install using `pip install pandas`)

## Logging

- The script logs its activities to a log file named `script.log`, located in the same directory as the script.
- You can review the log file for any errors or information about the script's execution.

## Notes
- The docker is currently not supported, since it cannot make a call to the host wifi network
- This script is designed to run on macOS due to the use of macOS-specific commands and paths.
- Please ensure that you have the necessary permissions to edit crontab and execute the script.
- Customize the paths and filenames according to your specific setup.
