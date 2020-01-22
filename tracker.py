import json, sys

class Tracker:
    def __init__(self, filename):
        self.filename = filename
        try:
            with open(filename, 'r') as rawdata:
                try:
                    self.dataFile = json.loads(rawdata.read())
                except:
                    print('file contains invalid data')
                    
        except:
            print('file does not exist')
            sys.exit()

    def save(self):
        with open(self.filename, 'w') as writeFile:
            writeFile.write(json.dumps(self.dataFile))
        
            
    def addStudent(self, studentInfo):
        self.dataFile.update(studentInfo)
        self.save()
    
    def deleteStudent(self, student):
        pass

if __name__ == '__main__':
    myTrack = Tracker('data.json')

    while True:
        userin = input('what would you like to do\n').strip().lower()
        if userin == 'add':
            studentInfo = {
                'name': input('What is the students name\n'),
                'id': input('What is their student id\n'),
                'dob': input('What is their date of birth')
                
            }
            myTrack.addStudent(studentInfo)
            
