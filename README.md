# DATA1202-01
Repository for Data Analysis Tools [1202-01] projects

# Introduction
This project analysis the youtube dataset provided which contains about 4k records regarding views per channel type, as well as each channel.

# Structure of this folder:

config/
    db_config.yaml
helper_functions.py
main.py

# db_config.yaml
Important to add creadentials to your database server where the CSV file will be uploaded to
This file can be used as an example of the required structure for the database server credentials

# main.py
This is the main script that will be executed in this project.

It will :
• read the CSV file
• Retrieve the distribution of a specified column in the CSV file
• Plot the retrieve distribution
• Open a connection to the database (specified in the file db_config.yaml)
• Load the retrieved data from the CSV file into a new table
• Close the connection 

# helper_functions.py
Contains a list of functions to assist in the main script, this can be re-used in other projects
Functions available are:

## • def connect_to_db(username, pwd, server, database)
Return a connection to the specified database

## • def diff_of_na(df)
Remove NaN rows and return the difference of rows before/after 

## • def sales_by_region(df, grouped_column, agg_col)
Misleading name, it will return the SUM of the column (agg_col) by grouping by the column(s) in the argument: grouped_column
The dataset is informed in the argument df.

# TODO

• rename function sales_by_region to get_column_sum, this will reflect what the functoin does.
• Add arguments for CSV filename, maybe via yaml file as well, or required argument in the main.py file 
• move function def load_dataframe_to_db(table_name, conn, dataframe) from main.py to helper_functions.py
• move function def distribution_top_records(topRecords, dataset, column) from main.py to helper_functions.py
