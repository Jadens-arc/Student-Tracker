import json, sys

class Tracker:
    def __init__(self, filename):
        try:
            with open(filename) as rawdata:
                try:
                    self.dataFile = json.loads(rawdata.read())
                except:
                    print('file contains invalid data')
                    
        except:
            print('file does not exist')
            sys.exit()
            
    def addStudent(self):
        pass
    
    def deleteStudent(self, student):
        pass

if __name__ == '__main__':
    myTrack = Tracker('data.json')
    while True:
        userin = input('what would you like to do\n').strip().lower()
        print(userin)
