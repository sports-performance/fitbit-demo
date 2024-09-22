# Fitbit demo applications

## File Descriptions:

**get-access-token.py:<br>** 

This retrieves an access token required to access Fitbit data programmatically.  To run it, you must have already registered a Fitbit application and obtained a Client ID and Secret.  Modify the appropriate section in the file to input these values.  The access token is valid for 8 hours.  Once expired, you may run the script again to get a new code.  You may also obtain an access code through the web interface:  
https://dev.fitbit.com/build/reference/web-api/troubleshooting-guide/oauth2-tutorial/ 

**steps.py:**
A minimal demo app that illustrates how to retrieve step data for a week.  You must first update the ACCESS_TOKEN variable.

**fitbit_data.py:**

Set of utility functions (and tests) to retrieve step, HRV, and heart rate data.  Data is saved in csv files and returned as DataFrames.  Requires installation of python-dotenv module (see below).  

**fitbit_dashboard.py:** 

Streamlit dashboard application that plots step count for a 30-day period and heartrate for a given day.  Requires installation of streamlit module (see below).  

## How to run the code:

Note: The Fitbit API requires Python 3.9.13 or earlier and cherrpy.  Install fitbit and cherrypy as part of a Python virtual environment.  
