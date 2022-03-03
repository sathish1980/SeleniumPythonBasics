import logging

class logdata:
        logger = logging.getLogger(__name__)
        def logfile(self):

                Formatter=logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
                FL=logging.FileHandler('C:\\Users\\sathishkumar\\PycharmProjects\\SeleniumProject\\Seleniumbasics\\logfile3.txt')
                FL.setFormatter(Formatter)
                self.logger.addHandler(FL) # Handle the filehandler - this is specifically used to print the log in to the file
                #set the filteration in the log file
                self.logger.setLevel(logging.CRITICAL)
                self.logger.debug("This is debugger log")
                self.logger.info("This is info log")
                self.logger.warning("This is warning log")
                self.logger.error("This is error log")
                self.logger.critical("critical log")


