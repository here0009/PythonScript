# coding: utf-8
# command : python DataFrame_Link.py sample_file info_file_list
# eg.: python DataFrame_Link.py
import pandas as pd
import os
import sys
print("========================")
def read_file(file_name):
    """
    read file to a datafrma
    """
    df_table = pd.read_table(file_name)
    return df_table

def file_list(directory_name):
    '''
    read each file in directory_name into a dataframe, store the file path and name in file_name_list
    '''
    input_file_list = list()
    for file_name in os.listdir(directory_name):
        if file_name.endswith(".txt"):
            input_file_list.append(file_name)
            # print(file_name) #for test

    print("Read the following files into dict:")
    print("===================================")
    file_name_list = []
    for input_file in input_file_list:
        input_file = '\\'.join([directory_name, input_file])
        print(input_file)
        file_name_list.append(input_file)

    return file_name_list

def write_excel(df, file_name):
    '''
    Function to write a dataframe to excel
    '''
    writer = pd.ExcelWriter(file_name)
    df.to_excel(writer)
    writer.save()

# def test():
#     sample_file = "Merged_file_Edited.xlsx"
#     info_file = "Rv_Regular_16-18.txt"
#     outputfile = 'merged_rota_regular.xlsx'
#     info_column = [0,4,5]
#     df_sample = pd.read_excel(sample_file)
#     df_info = pd.read_table(info_file, usecols = info_column)
#     df_merged = pd.merge(df_sample, df_info, how='left', on='patientid')
#     print(df_sample.head())
#     print(df_info.head())
#     print(df_merged.head())
#     write_excel(df_merged, outputfile)

# test()

def main():
    sample_file = sys.argv[1]
    df_merged = pd.read_excel(sample_file)
    directory_name = sys.argv[2].replace('\\','\\')
    # sample_file = "Merged_file_Edited.xlsx"
    outputfile = 'merged_file_virus_test.xlsx'
    info_column = [0,4,5] #patientid, test and sampleno

    info_file_list = file_list(directory_name)
    for info_file in info_file_list:
        df_info = pd.read_table(info_file, usecols = info_column)
        df_merged = pd.merge(df_merged, df_info, how='left', on='patientid')
    
    print(df_merged.head())
    write_excel(df_merged, outputfile)

main()