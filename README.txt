Steps to run the notebook:
    1. Open "Opt-Out Assignment.ipynb" with Jupyter NoteBook
    2. click the Run All ( >> ) button to execute all cells
    3. in order to create the connection object, it requires the user to enter his/her client id manually
    4. after entering the client id, click enter button then the user will be redirected to the ArcGis website
    5. log in to get a temp code then copy and paste that code back to the notebook to complete the login process
       (there will be a small window in the 3rd cell for the user to paste the code)
    6. all the rest cells will then be executed automatically after the connection object is created

NOTE: if the user would like to execute each cell manually, please run in this order - from cell 1 to the last cell 
(do not skip any cells in the middle)

Summary:
    1. There is a function - get_connect to create the GIS connection object
    2. There are 2 maps for the selected Country - Australia (the first map reflects the confrimed cases in each province,
the 2nd reflects the number of deaths per province)
    3. There is a Australia DataFrame contains 5 columns - Province_State, Last_Update, Confirmed, Recovered and Deaths.
    4. There are 3 charts and 4 statements (the result of each statement is obtained by one of 2 helper functions in the notebook) 
which help the user to understand Australia's confirmed and dead cases in the latest update