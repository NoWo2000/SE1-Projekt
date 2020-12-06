import configparser

config = configparser.ConfigParser()
config.read('config.ini')

# debug configuration
if __name__ == '__main__':
    print('*'*10 + ' Debug: config ' + '*'*10 )
    
    for key in config.keys():
        print('Group: ' + key)
        for item in config[key]:
            print(f'* {item} => {config[key][item]}')
