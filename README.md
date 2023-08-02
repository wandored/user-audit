# User Audit

This script, `user_audit.py`, is designed to import and merge user lists from company systems in order to create a master list of users. It aims to remove duplicates and identify orphaned users.

## Dependencies

The script requires the following dependencies:

- `pandas`: A powerful data manipulation library used for reading and manipulating CSV files.
- `glob`: A module used for finding files based on pattern matching.

Make sure you have these dependencies installed before running the script.

## Usage

To use the script, follow these steps:

1. Place the user list files in the appropriate directories:
   - Microsoft 365 user list: `./downloads/ms.csv`
   - R365 user list: `./downloads/r365.csv`
   - Rackspace user lists: `./downloads/rackspace/*.csv`
   - Reference user list: `./downloads/centra_ref_users.csv`
   <!-- - Dashboard user list: `./downloads/dashboard.csv` -->

2. Run the `user_audit.py` script.

3. The script will import and merge the user lists based on email addresses.

4. It will then generate three reports:
   - "in_master": Users that are present in the master list.
   - "not_in_master": Users that are in the imported file but not in the master list.
   - "not_in_file": Users that are in the master list but not in the imported file.

5. The reports will be saved as an Excel file in the `./output/` directory. The file name will be based on the source of the imported file (`r365.xlsx`, `rackspace.xlsx`, `reference.xlsx`).

6. Review the generated reports to identify duplicates and orphaned users.

Note: The script currently has a commented-out section for reading the dashboard user list. You can uncomment and modify the necessary code to include the dashboard user list if needed.

Please ensure that you have the appropriate file permissions and valid file paths before running the script.

Feel free to modify and adapt the script to suit your specific requirements.
