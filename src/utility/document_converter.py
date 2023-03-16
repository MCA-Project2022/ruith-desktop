import pypandoc


class DocumentConverter:

    def __init__(self):
        pass

    @property
    def input(self):
        return self.__input

    @input.setter
    def input(self, value):
        self.__input = value

    @property
    def input_format(self):
        return self.__input_format

    @input_format.setter
    def input_format(self, value):
        self.__input_format = value

    @property
    def output(self):
        return self.__output

    @output.setter
    def output(self, value):
        self.__output = value

    @property
    def output_format(self):
        return self.__output_format

    @output_format.setter
    def output_format(self, value):
        self.__output_format = value

    def start(self):
        pypandoc.convert_file(self.__input, format=self.__input_format,
                              outputfile=self.__output, to=self.__output_format)
