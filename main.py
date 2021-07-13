#f = open("./AUTO131.csv")
#lines = f.readlines()[5::]
#splitline = [i.split(sep=",") for i in lines]
#ind = splitline[0].index("At%")
#deletedline = [i[ind::] for i in splitline]
#print(deletedline)




class fileread:
    def __init__(self, path):
        self.path = path

    def _read(self):
        file = open(self.path)
        return file.readlines()

    def _split_text(self, lines):
        return [i.split(sep=",") for i in lines]

    def _find_index(self, lines):
        return lines[0].find("At%")

    def _extract_data_section(self, lines, ind):
        return [i[ind::] for i in lines]

    def _extract_data(self, line):
        return line[1::]

    def _extract_header(self, line):
        return line[0]


    def readdata(self):
        readline = self._read()
        splitedline = self._split_text(readline)
        index = self._find_index(splitedline)
        datasection = self._extract_data_section(splitedline, index)
        data = self._extract_data(datasection)
        header = self._extract_header(datasection)
        return









def main():
    newfile = fileread("./AUTO131.CSV")
    lines = newfile.read()
    print(lines)


if __name__ == '__main__':
    main()