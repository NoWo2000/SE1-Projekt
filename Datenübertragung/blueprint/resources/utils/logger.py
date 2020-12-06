from .config import config

class Logger:
    __lvl_dic = { "DEBUG" : 1, "LOG" : 2, "ERROR" : 3 }
    
    def __init__(self, level = 2):
        self.setLevel(level)
        
    def setLevel(self, level):
        if level in {1, 2, 3}:
            self.lvl = level
        elif level in self.__lvl_dic:
            self.lvl = self.__lvl_dic[level]
        else:
            raise TypeError("Level not a valid integer or string: %r" % level)
    
    def debug(self, msg):
        if self.lvl == 1:
            self.__logConsole('\033[94m' + "DEBUG", msg + '\033[00m')
            self.__logFile("DEBUG", msg)
    
    def log(self, msg):
        if self.lvl <= 2:
            self.__logConsole("LOG", msg)
            self.__logFile("LOG", msg)
    
    def error(self, msg):
        if self.lvl <= 3:
            self.__logConsole("\033[91m" + "ERROR", msg + '\033[00m')
            self.__logFile("ERROR", msg)
    
    def __logConsole(self, level, msg):
        print(level + ": " + msg)
        
    def __logFile(self, level, msg):
        log_file = open(config['LOGGER']['file'],"a+")
        log_file.write(level + ": " + msg + "\n")
        log_file.close()

loggerFile = Logger(int(config['LOGGER']['level']))

# debug Logger-class
if __name__ == '__main__':
    print('*'*10 + ' Debug: Logger ' + '*'*10 )
    loggerFile.log('Dies ist ein Testlog')
    loggerFile.error('Dies ist ein Testerror')
    loggerFile.debug('Dies ist ein Testdebug')
    