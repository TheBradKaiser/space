import requests

#import coverage


class SpacePeople:

    def getData(self,url):
        #grab data from api using requests module, if url is not valid return error
        try:
            response = requests.get(url)
            return response.json()["people"]
        except:
            return "Please enter valid url"
        
    def sortData(self,data):
        #used in part of challenge 2, sort data by craft so people can be grouped by craft
        return data.sort(key=lambda x: x["craft"])

    def parseData(self,data):
        #initialize variables. name is 4 letters long so its the minimum length of name column, 5 for craft column
        li=[]
        mname=4
        mcraft=5
        for a in range(len(data)):
            #add values to list
            li.append(data[a]["name"])

            #check if craft has already been accounted for. (challenge 2)
            #potential issue if a person has the same name as a spaceship? jeff bezos is really the only worry
            if data[a]["craft"] in li:
                li.append("")
            else:
                li.append(data[a]["craft"])
            #check max length of names and crafts
            if len(data[a]["name"]) >= mname:
                mname = len(data[a]["name"])
            if len(data[a]["craft"]) >= mcraft:
                mcraft = len(data[a]["craft"])
        return mname,mcraft,li
        
    def createTableHeader(self,mname,mcraft):
        #craft header by using the maximum lengths of name and craft field.
        table="Name".ljust(mname)+"|"+"Craft".ljust(mcraft)+"\n"+"-"*(mname)+"+"+"-"*(mcraft)+"\n"
        return table


    def createTable(self,table,li):
        #iterate through table placing items in their place, along with seperators and new line characters
        for a in range(len(li[2])):
            if a%2==0:
                table=table+li[2][a].ljust(li[0])+"|"
            else:
                table=table+li[2][a].ljust(li[1])+"\n"
        return table

#5 lines
x=SpacePeople()
data = x.getData("http://api.open-notify.org/astros.json")
x.sortData(data)
li=x.parseData(data)
table = x.createTableHeader(li[0],li[1])
print(x.createTable(table,li))
