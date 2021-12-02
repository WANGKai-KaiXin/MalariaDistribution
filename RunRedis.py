import logging  # used to write the progress information
import sys  # used to terminate the progress
import redis  # database


class RunRedis:
    # TODO use Redisearch to search the data quickly
    # TODO use the cloud server redis database instead of local redis server
    # TODO search all data in the database
    # TODO add error exception
    """
    Every operation related to the redis database
    """

    def __init__(self):
        """
        get connection to the redis database
        """
        try:
            self.pool = redis.ConnectionPool(host='localhost', port=6379, db=0, decode_responses=True)
            self.r = redis.Redis(connection_pool=self.pool)
            self.r.client_list()
        except redis.ConnectionError:
            logging.error("Disconnect to redis. Please check if the redis starts.")
            sys.exit(1)  # exit the progress with error status

    def insert(self, key, values):
        """
        :param key: name of the key you want to insert the value
        :param values: elements you want to insert
        """
        # if values is list, add one by one
        # otherwise add it directly
        if type(values).__name__ == 'list':
            for value in values:
                self.r.rpush(key, value)
            logging.info("Insert data list successfully.")
        else:
            self.r.rpush(key, values)
            logging.info("Insert one data successfully.")

    def deleteAll(self):
        """
        delete all data in the redis database
        """
        for elem in self.r.keys():
            self.r.delete(elem)
        logging.info("Delete all the data successfully.")

    def deleteByKey(self, key):
        """
        :param key: the name of key you want to delete
        """
        self.r.delete(key)
        logging.info("Delete the key [" + str(key) + "] and data successfully.")

    def searchAllByKey(self, key):
        """
        :param key: name of the key you want to search
        :return: all elements of key
        """
        logging.info("Search the key [" + str(key) + "] and data successfully.")
        return self.r.lrange(key, 0, self.r.llen(key))

    def searchTagByTKey(self, key, directory, tag):
        """
        :param key: name of the key you want to search
        :param directory: the list of element information, such as country, name, sex etc.
        :param tag: the tag of element you want
        :return: the information of the tag you want
        """
        index = -1
        for word in directory:
            index += 1
            if tag == word:
                return self.r.lindex(key, index)
