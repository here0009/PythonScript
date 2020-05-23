# coding: utf-8
# Merge Excel Files. If the excel files have the same header, then merge them.
# command: python ExcelMerge.py .\sample(path of sample)
import os
import sys
import copy
import pandas as pd
def read_excel_file(file_name) :
    '''
    Function to read excel file, store it in a dataframe
    '''
    df_excel = pd.read_excel(file_name)
    # print(df_excel.head())
    return df_excel

def load_files(directory_name):
    '''
    read the files in directory_name, store the dataframe in df_total
    '''
    input_file_list = list()
    for file_name in os.listdir(directory_name):
        if file_name.endswith(".xls"):
            input_file_list.append(file_name)
            # print(file_name) #for test

    print("Read the following files into dict:")
    print("===================================")
    df_list = []
    for input_file in input_file_list:
        input_file = '\\'.join([directory_name, input_file])
        print(input_file)
        df_list.append(read_excel_file(input_file))

    df_total = pd.concat(df_list, join = 'inner',ignore_index=True)

    print(df_total.head())
    print(df_total.tail())
    print("The size of the dataframe is ",df_total.shape)
    return df_total

def write_excel(df, file_name):
    '''
    Function to write a dataframe to excel
    '''
    writer = pd.ExcelWriter(file_name)
    df.to_excel(writer)
    writer.save()


def main():
    directory_name = sys.argv[1].replace('\\','\\')
    df_total = load_files(directory_name)
    outputfile = "Merged_file.xlsx"
    write_excel(df_total, outputfile)
    print("The mergeed file have been writen to ", outputfile)
    
main()