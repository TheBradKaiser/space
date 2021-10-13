import requests

#import coverage


class SpacePeople:

    def getData(self,url):
        response = requests.get(url)
        return response.json()["people"]
        
    def sortData(self,data):
        #used in part of challenge 2
        return data.sort(key=lambda x: x["craft"])

    def parseData(self,data):
        li=[]
        mname=4
        mcraft=5
        for a in range(len(data)):
            #add values to list
            li.append(data[a]["name"])

            #check if craft has already been accounted for. (challenge 2)
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
        table="Name".ljust(mname)+"|"+"Craft".ljust(mcraft)+"\n"+"-"*(mname)+"+"+"-"*(mcraft)+"\n"
        return table


    def createTable(self,table,li):
        for a in range(len(li[2])):
            if a%2==0:
                table=table+li[2][a].ljust(li[0])+"|"
            else:
                table=table+li[2][a].ljust(li[1])+"\n"
        print(table)

#5 lines
x=SpacePeople()
data = x.getData("http://api.open-notify.org/astros.json")
x.sortData(data)
li=x.parseData(data)
table = x.createTableHeader(li[0],li[1])
x.createTable(table,li)
