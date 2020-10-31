import json
class top_file:
    def __init__(self, file_location="scores.json"):
        '''
        sets the file inside the project to the file location for use

        PARAMETERS:
        -----------
        file_location: str
            contains the json file to be used for reading and writing
        '''
        self.file_location = file_location

    def writer(self, name, value):
        '''
        writes to the file

        PARAMETERS:
        -----------
        file_location: str
            contains the json file to be used for reading and writing
        file_read: dictionary
            contains all the information containing the scores and names
        '''
        with open(self.file_location,"r+") as files:
            file_read = json.load(files)
        with open(self.file_location,"w") as files:
            file_read.update({len(file_read):{"name":name, "score":value}})
            json.dump(file_read, files)

    def reader(self):
        '''
        read from the file

        PARAMETERS:
        -----------
        file_location: str
            contains the json file to be used for reading and writing
        file_read: dictionary
            contains all the information containing the scores and names
        sorted_list: list
            contains the sorted list of the scores
        '''
        with open(self.file_location,"r+") as files:
            file_read = json.load(files)
            sorted_list = sorted(sorted(file_read.items(), key=lambda x:x[1]['name'].upper()), key=lambda x: x[1]['score'],reverse=True)
            return sorted_list
    def top10(self):
        '''
        writes to the file

        PARAMETERS:
        -----------
        values: list
            contains the list of the top ten scores with names
        reader: function
            reads from the file
        '''
        values = []
        if len(self.reader()) >= 10:
            for i in range(10):
                values.append( self.reader()[i])
        else:
            for i in range(len(self.reader())):
                values.append(self.reader()[i])
        return values
