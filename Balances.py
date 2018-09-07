#!/usr/bin/python

from re import sub

class Inventory:
    def __init__(self,isDynamic):
        self.inv=[]        
        self.dynamic=isDynamic

    def move(self,item,dest):
        for myItem in self.inv:
            if myItem.name == item.name:
                dest.push(myItem)
                self.inv.delete(myItem)

class OldFurniture:
    def __init__(self):
        self.DynamicInventory=[]
        self.StaticInventory=[]
        self.name="Old Furniture"
        self.description="Old torn up furniture"

    def ProcessCommand(self,comm):
        for myComm in self.commlist:
            if comm.word==myComm.word:
                pass

class RamShackleHut:
    def __init__(self):
        self.DynamicInventory=[]
        self.StaticInventory=[]
        self.name="Ramshackle Hut"
        self.Description="You find yourself in a room"
        self.commlist=[]

    def ProcessCommand(self,comm):
        for myComm in self.commlist:
            if comm.word==myComm.word:
                pass
    


class Command:
    def __init__(self,x):
        self.word=x
        self.isMotion=1


    def match(self,txt):
        self.word == txt


    def action(self):
        pass



Take=Command('take')
Look=Command('look')




commlist=[Take, Look]

print (commlist)

def processInput(inData):
    inData = inData.strip()
    inData = sub(r'\s+', ' ', inData)
    print(inData)
    commLine=inData.split(' ')
    print (commLine)

strInput=""
strConfirmQuit=""


while strConfirmQuit not in ("y", "Y", "yes", "Yes"):
    strInput=""
    while strInput <> "quit":
        strInput=raw_input('>')
        #print(strInput)
        processInput(strInput)

    strConfirmQuit=raw_input("Really quit?: ")
