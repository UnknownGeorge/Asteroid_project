import json
class top_file:
    def __init__(self, file_location="scores.json"):
        self.file_location = file_location

    def writer(self, name, value):
        with open(self.file_location,"r+") as files:
            file_read = json.load(files)
        with open(self.file_location,"w") as files:
            file_read.update({len(file_read):{"name":name, "score":value}})
            #files.truncate(0)
            json.dump(file_read, files)

    def reader(self):
        with open(self.file_location,"r+") as files:
            file_read = json.load(files)
            #sorted_list = sorted(file_read.items(), key=lambda x: x[1]["score"], reverse=True)
            sorted_list = sorted(sorted(file_read.items(), key=lambda x:x[1]['name'].upper()), key=lambda x: x[1]['score'],reverse=True)
            #print(sorted_list)
            return sorted_list
    def top10(self):
        for i in range(10):

            print(self.reader()[i])
