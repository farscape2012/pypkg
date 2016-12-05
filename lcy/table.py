import csv
import pandas

def write(data, file="output.csv", columns=None, index_in_list=False, mode="wb", sep=","):
    #columns = ["abcd","bcde","cdef"] #a csv with 3 columns
    if index_in_list:
        index = [i[0] for i in data] 
        data = [i[1:] for i in data]
    else:
        index = None
    df = pandas.DataFrame(data, columns=columns, index=index)
    #Now you have a csv with columns and index:
    df.to_csv(file, mode=mode, sep=sep)

        
def read(file="input.csv", sep=",", header=None, names=None, index_col=None, usecols=None,comment=None):
    # names = colnames
    # usecols = index or colnames in names
    df = pandas.read_table(file, sep=sep, header=header, names=names, index_col=index_col, usecols=usecols, comment=comment)
    return df
