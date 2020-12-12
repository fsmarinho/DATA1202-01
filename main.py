import matplotlib.pyplot as plt 
from helper_functions import diff_of_na, connect_to_db, sales_by_region
import pandas as pd 
import yaml

## load dataset
youtube_df = pd.read_csv("youtube_dataset.csv", encoding='cp1252')

db_conn = None 
## load credentials:
with open('./config/db_config.yaml', 'r') as stream:
    try:
        db_conn = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

## see the first rows of this dataframe
print(youtube_df.head())

## check the columns 
print(youtube_df.columns) 

## check the columns 
print(youtube_df['channeltype'].unique()) 

## Q1 Create a function to calculate the distribution of channeltype from the top 1000 records.
def distribution_top_records(topRecords, dataset, column):
    """
        This function will return the top x records dataframe 
        as well as the distribution of a column
        Input:
            topRecords: number of records 
            dataset: dataframe to filter top records 
            column: name of the column to retrieve distribution
        Output:
            dataframe of top records, distribution of column 
         
    """
    new_df = dataset.loc[:topRecords]
    return new_df, new_df.groupby(column)[column].count()

## call function and retrieve its output 
top1000, distributionChannelType = distribution_top_records(1000, youtube_df, "channeltype")

## check the columns 
print(top1000) 
print(distributionChannelType)

## plot distribution as a horizontal bar graph
fig, ax = plt.subplots(figsize = (12, 8)) 
distributionChannelType.plot.barh(color ='maroon',  width = 0.4) 

plt.xlabel("No. of channels") 
plt.ylabel("Channel Type") 
plt.title("Distribution of channel type in the dataset") 
plt.show() 


# Q2 Load only the top 1000 records of the original 4000 into a separate CSV file, or database table
def load_dataframe_to_db(table_name, conn, dataframe):
    try:
        dataframe.to_sql(table_name, conn, if_exists='fail');
    except ValueError as valuesException:
        print(valuesException)
    except Exception as exceptionMsg:   
        print(exceptionMsg)
    else:
        print(f'Table {table_name} created successfully.');   
    finally:
        conn.close()

## create database connection 
conn = connect_to_db(db_conn['user'], db_conn['pwd'], db_conn['server'], db_conn['database'])

## call function to create table in DB from dataframe
load_dataframe_to_db('youtube_dataset', conn, top1000)