import logging  # used to write the progress into a file
from GetData import GetData
from RunRedis import RunRedis


def runonce():
    """
    Testing
    run the program
    not the final one
    TODO use user interface to run the program
    """
    # runRedis = RunRedis()  # call the RunRedis class
    # runRedis.deleteAll()  # test deleteAll function
    # runRedis.insert("bob", "11")  # test insert function
    # runRedis.insert("bob", ["male", "China"])  # test insert function
    # print(runRedis.searchAllByKey("bob"))  # test searchAll function
    # getData1 = GetData("data.txt.txt")  # call the GetData class with unresisting file
    # getData1.getContent()  # check if GetData can handle the wrong info otherwise the previous line will be ignored
    # getData1 = GetData("system.log")  # call the GetData class with wrong file
    # getData1.getContent()  # check if GetData can handle the wrong info otherwise the previous line will be ignored
    getData = GetData("data.txt")  # call the GetData class with a correct file
    print(getData.getContent())  # check if it can get the suffix of file and get the data


def runLogging():
    """
    It is used to display the log information in the console and write it into a system.log file
    Need to run this method before running the others, otherwise the system log will not be written in the file
    """
    logger = logging.getLogger()
    # the min level of information which is wrote in the file
    logger.setLevel(logging.DEBUG)
    # set the format of level,time, message
    formatter = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s', datefmt='%Y-%d-%m %H:%M:%S')

    # used to setup the console output
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)

    # used to setup the system.txt log file output
    Log_filename = "system.log"
    file = logging.FileHandler(Log_filename)
    file.setLevel(logging.DEBUG)
    file.setFormatter(formatter)

    # used to start the two handler so that it can display and write the system progress
    logger.addHandler(console)
    logger.addHandler(file)


if __name__ == "__main__":
    runLogging()
    runonce()
