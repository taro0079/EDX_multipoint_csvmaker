import sys

import numpy as np
import pandas as pd


class fileread:
    def __init__(self, path):
        self.path = path

    def _read(self):
        file = open(self.path)
        return file.readlines()[5::]

    def _split_text(self, lines):
        return [i.replace("\n","").split(sep=",") for i in lines]

    def _find_index(self, lines):
        return lines[0].index("At%")

    def _extract_data_section(self, lines, ind):
        return [i[ind::] for i in lines]

    def _extract_data(self, line):
        return line[1::]

    def _extract_header(self, line):
        return line[0]

    def map_to_float(self, lines):
        return [map(float, i) for i in lines]


    def readdata(self):
        readline = self._read()
        splitedline = self._split_text(readline)
        index = self._find_index(splitedline)
        datasection = self._extract_data_section(splitedline, index)
        stringdata = self._extract_data(datasection)
        data = self.map_to_float(stringdata)
        header = self._extract_header(datasection)
        return Data(data, header)


class Data:
    def __init__(self, data, header):
        self.data = data
        self.header = header

    def create_dataframe(self):
        df = pd.DataFrame(self.data)
        df.columns = self.header
        return dataFrameManipulate(df)


class dataFrameManipulate:
    def __init__(self, data):
        self.__data = data

    def delete_first_column(self):
        first_column = self.__data.columns[0]
        dropeddata = self.__data.drop(first_column, axis=1)
        return dataFrameManipulate(dropeddata)

    def _sum_of_data(self):
        return self.__data.sum()

    def sum_is_nonzero(self):
        return self._sum_of_data() != 0

    def nonzero_column(self):
        return self.sum_is_nonzero()[self.sum_is_nonzero() == True].index

    def extract_nonzero_data(self):
        return self.__data[self.nonzero_column()]

    def show_data(self):
        return self.__data

class relativeDistance:
    def __init__(self, pointnumber):
        self.MAX = 50
        self.MIN = 1
        if pointnumber > self.MAX:
            print("too bigger number of point !")
            sys.exit(0)
        elif pointnumber < self.MIN:
            print("too small number of point !")
            sys.exit(0)
        self.pointnumber = pointnumber

    def make_incremental(self):
        return np.linspace(0, 1, self.pointnumber)

def main():
    newfile = fileread("./AUTO131.CSV")
    data = newfile.readdata()
    df = data.create_dataframe()
    droped = df.delete_first_column()


    print(droped.extract_nonzero_data())


if __name__ == '__main__':
    main()