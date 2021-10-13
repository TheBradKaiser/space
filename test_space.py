import unittest
import requests
import space

class testmain(unittest.TestCase):

    
    def test_getData(self):
        x=space.SpacePeople()
        response = x.getData("http://api.open-notify.org/astros.json")
        self.assertEqual(response,[{'craft': 'ISS', 'name': 'Mark Vande Hei'}, {'craft': 'ISS', 'name': 'Oleg Novitskiy'}, {'craft': 'ISS', 'name': 'Pyotr Dubrov'}, {'craft': 'ISS', 'name': 'Thomas Pesquet'}, {'craft': 'ISS', 'name': 'Megan McArthur'}, {'craft': 'ISS', 'name': 'Shane Kimbrough'}, {'craft': 'ISS', 'name': 'Akihiko Hoshide'}, {'craft': 'ISS', 'name': 'Anton Shkaplerov'}, {'craft': 'ISS', 'name': 'Klim Shipenko'}, {'craft': 'ISS', 'name': 'Yulia Pereslid'}])

        response = x.getData("http://asdfjkl")
        self.assertEqual(response,"Please enter valid url")


    def test_sortData(self):
        x=space.SpacePeople()
        weirdset=[{'craft': 'abc', 'name': 'Markie Vande Hei'},{'craft': 'e', 'name': 'Mar'},{'craft': 's', 'name': 'M'},{'craft': 'abcd', 'name': 'i'}]
        numset=[{'craft': '1', 'name': 'Markie Vande Hei'},{'craft': '3', 'name': 'Mar'},{'craft': '2', 'name': 'M'},{'craft': 'A', 'name': 'i'}]
        dupeset=[{'craft': '1', 'name': 'Markie Vande Hei'},{'craft': '1', 'name': 'Markie Vande Hei'},{'craft': '0', 'name': 'Markie Vande Hei'}]
        emptyset=[]
        x.sortData(weirdset)
        x.sortData(numset)
        x.sortData(dupeset)
        x.sortData(emptyset)
        self.assertEqual(weirdset,[{'craft': 'abc', 'name': 'Markie Vande Hei'},{'craft': 'abcd', 'name': 'i'},{'craft': 'e', 'name': 'Mar'},{'craft': 's', 'name': 'M'}])
        self.assertEqual(numset,[{'craft': '1', 'name': 'Markie Vande Hei'},{'craft': '2', 'name': 'M'},{'craft': '3', 'name': 'Mar'},{'craft': 'A', 'name': 'i'}])
        self.assertEqual(dupeset,[{'craft': '0', 'name': 'Markie Vande Hei'},{'craft': '1', 'name': 'Markie Vande Hei'},{'craft': '1', 'name': 'Markie Vande Hei'}])
        self.assertEqual(emptyset,[])

    def test_parseData(self):
        x=space.SpacePeople()
        #need to ensure values of lengths are ok
        weirdset=[{'craft': 'abc', 'name': 'Markie Vande Hei'},{'craft': 'e', 'name': 'Mar'},{'craft': 's', 'name': 'M'},{'craft': 'abcd', 'name': 'i'}]
        emptyset=[]
        oneset=[{'craft': '1', 'name': 'Markie markie mark mark'}]
        longset=[{'craft': '11111111111111111111111111111111111111111111', 'name': 'Markie Vande Hei'},{'craft': '1', 'name': 'aaaaaaaaaaasssssssssssdddddddddfffffffff'}]
        l1=x.parseData(weirdset)
        self.assertEqual(l1,(16,5,['Markie Vande Hei','abc','Mar','e','M','s','i','abcd']))
        l1=x.parseData(emptyset)
        self.assertEqual(l1,(4,5,[]))
        l1=x.parseData(oneset)
        self.assertEqual(l1,(23,5,['Markie markie mark mark','1']))
        l1=x.parseData(longset)
        self.assertEqual(l1,(40,44,['Markie Vande Hei','11111111111111111111111111111111111111111111','aaaaaaaaaaasssssssssssdddddddddfffffffff','1']))
        
    def test_createTableHeader(self):
        x=space.SpacePeople()
        #MINIMUM lengths for name and craft are 4 and 5 respectively, due to the length of the headers
        name1=4
        name2=10
        name3=50
        craft1=5
        craft2=10
        craft3=50
        table=x.createTableHeader(name1,craft1)
        self.assertEqual(table,"Name|Craft\n----+-----\n")
        table=x.createTableHeader(name2,craft2)
        self.assertEqual(table,"Name"+" "*6+"|Craft"+" "*5+"\n----------+----------\n")
        table=x.createTableHeader(name3,craft3)
        self.assertEqual(table,"Name"+" "*46+"|Craft"+" "*45+"\n--------------------------------------------------+--------------------------------------------------\n")

    def test_createTable(self):
        x=space.SpacePeople()
        weirdtupe=(16,5,['Markie Vande Hei','abc','Mar','e','M','s','i','abcd'])
        emptytupe=(4,5,[])
        oneset=(23,5,['Markie markie mark mark','1'])
        longset=(40,44,['Markie Vande Hei','11111111111111111111111111111111111111111111','aaaaaaaaaaasssssssssssdddddddddfffffffff','1'])
       
        table = x.createTableHeader(weirdtupe[0],weirdtupe[1])
        self.assertEqual(x.createTable(table,weirdtupe),"Name            |Craft\n----------------+-----\nMarkie Vande Hei|abc  \nMar             |e    \nM               |s    \ni               |abcd \n")
        
        table = x.createTableHeader(emptytupe[0],emptytupe[1])
        self.assertEqual(x.createTable(table,emptytupe),"Name|Craft\n----+-----\n")

        table = x.createTableHeader(oneset[0],oneset[1])
        self.assertEqual(x.createTable(table,oneset),"Name                   |Craft\n-----------------------+-----\nMarkie markie mark mark|1    \n")

        table = x.createTableHeader(longset[0],longset[1])
        self.assertEqual(x.createTable(table,longset),"Name                                    |Craft"+" "*39+"\n----------------------------------------+--------------------------------------------\nMarkie Vande Hei                        |11111111111111111111111111111111111111111111\naaaaaaaaaaasssssssssssdddddddddfffffffff|1"+" "*43+"\n")


if __name__ == '__main__':
    unittest.main()