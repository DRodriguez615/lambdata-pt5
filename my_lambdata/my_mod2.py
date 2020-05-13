
# my_lambdata/my_mod2.py
import pandas as pd


def check_nulls(df):
    """
    Checks null values within dataframe

    Param: dataframe

    Return number of null values
    """
    return df.isnull().sum()


#
#
if __name__ == "__main__":

    print("JUNK")
    print("TEST")