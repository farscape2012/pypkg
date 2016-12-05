import pandas

def write(data, file="output.csv", header=False, columns=None, index=False, index_in_list=False, mode="wb", sep=","):
    """Write a table (list of lists) / data frame (pandas object) to a file.

    Args:
        data: A list of lists or pandas dataFrame object.
        file: a file string.
        header: A logic value indicating whether header are written or not. Default is False.
        columns: A column names can be given when data is a list of lists. Default is None. When data is panda DataFrame object and has "columns" attribute, "columns" attribute is used as header/ column names. 
        index: A logic value indicating whether index will be written or not. Default is False. When data is panda DataFrame object and has "index" attribute, "index" is used as index. 
        index_in_list: A logic value indicating whether data (list of lists) contan index in the list. Default is False. When it is True, the first element is used as index.
        mode="wb": A string of mode
        sep=",": A string of delimeter. Default is ","
    Returns:
        Nothing.
    Raises:
        TypeError: if n is not a number.
        ValueError: if n is negative.

    """
    if type(data) != pandas.core.frame.DataFrame:
        if index_in_list:
            index_in_list = [i[0] for i in data] 
            data = [i[1:] for i in data]
        else:
            index_in_list=None
        data = pandas.DataFrame(data, columns=columns, index=index_in_list)
    data.to_csv(file, mode=mode, sep=sep, index=index, header=header)

        
def read(file="input.csv", sep=",", header=None, names=None, index_col=None, usecols=None,comment=None):
    """Read a table from a file.

    Args:
        file: a file string.
        sep=",": A string of delimeter. Default is ","
        header: A none negative value indicating which row is used as header. Default is None.
        names: List of column names to use. Default is None. 
        index_col: An int or sequence or False, default None. Column to use as the row labels of the DataFrame. If a sequence is given, a MultiIndex is used.  
        usecols: Array-like, default None. Return a subset of the columns. All elements in this array must either be positional (i.e. integer indices into the document columns) or strings that correspond to column names provided 
        comment: 
        
    Returns:
        Nothing.
    Raises:
        TypeError: if n is not a number.
        ValueError: if n is negative.
    # names = colnames
    # usecols = index or colnames in names
    """
    df = pandas.read_table(file, sep=sep, header=header, names=names, index_col=index_col, usecols=usecols, comment=comment)
    return df
