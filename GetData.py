import logging
import os


def notSupport():
    """
    Handle incompatible format
    """
    logging.error("Cannot support such file type, please use another one.")


class GetData:
    # TODO some other format of files
    # TODO get the data from other sources
    """
    Every operations related to get data, including get data from the local data file, internet, some other source, etc
    Use dictionary to deal with the different datafile type
    """

    def __init__(self, filename):
        """
        :param filename: the data file name
        """
        self.filename = filename

    def getContentFromTxtDataFile(self):
        """
        Read the data file, and eliminate the \n in every line
        :return:the content of the file
        """
        # read the file
        f = open(self.filename, encoding="utf-8")
        data = f.readlines()
        # eliminate the \n in every line
        for i in range(len(data)):
            data[i] = data[i].strip('\n')
        f.close()
        # return the content of file
        logging.info("Read the file successfully.")
        return data

    def fileTypeDict(self, suffix):
        # TODO excel csv xlsx xls
        """
        Use directory to execute the function according to the file suffix instead of switch case
        :param suffix: suffix name of the file
        :return: content of the data file
        """
        suffixes = {
            "txt": self.getContentFromTxtDataFile
        }

        return suffixes.get(suffix, notSupport)()

    def getContent(self):
        """
        1. Check if the file exists
        2. Analysis file type and the read the data
        3. Read the file
        :return:the content of the file
        """
        if os.path.exists(self.filename):
            suffix = os.path.splitext(self.filename)[-1][1:]  # analysis the file type
            logging.info("Analysis file type successfully.")
            return self.fileTypeDict(suffix)
        else:
            logging.error("The data file doesn't exists, please check the file name and path.")
