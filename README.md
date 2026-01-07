# bikepoint_api_project

## Extract

**Set Up**
Created a new repository, cloned it with github desktop and opened it in vscode. Created a virtual environment (**python -m venv .venv**) and activated it (**.venv/Scripts/activate**). Installed requests (**pip install requests**) - this is the only non-native package we used so it is the only one I had to install. Created a new branch (**git switch -c extract branch**). Created a requirements file (**pip freeze > requirements.txt**).

**Import Packages**

Imported packages to use in the script. Including:
 - **requests**: for calling the api
 - **os**: for finding the directory to save the file in
 - **datetime**: for timestamps
 - **json**: to use json.dump to write the file in a json format
 - **time**: to define the time it takes for it to error before it times out
 - **logging**: to create the log files and define the log messages

**API Call, Read in as JSON, Save as JSON**

Using response.get(), the API is called and the status code is saved as a variable. If the call is sucessful it converts the response to a JSON format, creates file directory (if it doesn't already exist) and creates a filepath. Using a try/except statement, if there are no errors a file is created in the directory, while if there are errors it prints and error message.

**Error Handling**

Error handling is done using an if statement and a while loop. If the API call is successfull it breaks the loop. If there are errors in the call that are to do with the source system (the error code is less with 200 or more than 499) then it tries calling it again. It only attempts to call it 3 times maximum. If there is an error code other than this then it prints out the error code and breaks the loop.

---
