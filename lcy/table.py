import csv
import pandas

def write(data, file="output.csv", header=False, columns=None, index=False, index_in_list=False, mode="wb", sep=","):
    if type(data) != pandas.core.frame.DataFrame:
        if index_in_list:
            index_in_list = [i[0] for i in data] 
            data = [i[1:] for i in data]
        else:
            index_in_list=None
        data = pandas.DataFrame(data, columns=columns, index=index_in_list)
    data.to_csv(file, mode=mode, sep=sep, index=index, header=header)

        
def read(file="input.csv", sep=",", header=None, names=None, index_col=None, usecols=None,comment=None):
    # names = colnames
    # usecols = index or colnames in names
    df = pandas.read_table(file, sep=sep, header=header, names=names, index_col=index_col, usecols=usecols, comment=comment)
    return df
