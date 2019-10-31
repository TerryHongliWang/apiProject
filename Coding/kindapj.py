import requests
from tkinter import *
import webbrowser
from os import path
from PIL import ImageTk,Image


#Main
def writeHTML(datajson,pokemonEnter):
    

    ofile = open("htmlDisplay.html","w")

    #Heading, style of program
    ofile.write("<head>"+"\n" )
    ofile.write("   <title>Pokemon Data</title>"+"\n")
    ofile.write("   <link rel=" + "'stylesheet'" + "href=" "'styleAPI.css'" + ">"+"\n")
    ofile.write("</head>" + "\n")

    #Header
    ofile.write("<h1>" + datajson["name"].capitalize() + "</h1>")

    #Check Number of Types
    pokeType = datajson["types"]
    typeLength = len(pokeType)

    #sType = showType.get()
    #print(sType)

    #Print that number of types in a list
    #if sType == 1:
    ofile.write("<div>" + "<p1>Types:</p1>")
    for i in range(typeLength):
        ofile.write("<p>" + datajson["types"][i]["type"]["name"].capitalize() +"   "+ "</p>")
    ofile.write("</div>")

    pokeAbility = datajson["abilities"]
    abilityLength = len(pokeAbility)

    ofile.write("<div>" + "<p1>Abilities:</p1>")
    for i in range(abilityLength):
        ofile.write("<p>" + datajson["abilities"][i]["ability"]["name"].capitalize()+"   "+ "</p>")
    ofile.write("</div>")

    pokeMove = datajson["moves"]
    moveLength = len(pokeMove)

    ofile.write("<div>" + "<p1>Moves:</p1>")
    for i in range(moveLength):
        ofile.write("<p>" + datajson["moves"][i]["move"]["name"].capitalize()+"   "+ "</p>")
    ofile.write("</div>")
        
    ofile.close()

def doit():
    if len(pokemonEnter.get()) == 0:
        print("There is no pokemon indicated!")
    else:
        doRequest  = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokemonEnter.get())
        datajson = doRequest.json()
        writeHTML(datajson,pokemonEnter.get())
        #b2 = Button(root,text="complete - view your file",command=webbrowser.open('file://' + path.realpath('htmlDisplay.html')))

#Master    
root = Tk()
root.geometry("400x300")
root.title("")


#GUI for main program
topframe = Frame(root,bg="#FF4C4C",height="37")
topframe.pack(fill=X)
textFrame = Frame(root, height=70)
textFrame.pack()
space = Canvas(textFrame, height=70)
space.grid(row=0,column=0)
head = Label(textFrame,text="Pokemon Info Database", font=("Osaka", 28), fg="#373737")
mid = Label(textFrame, text="Enter the name or id of any pokemon:", font=("Osaka", 14), fg="#777777")
head.grid(row=0,column=0)
mid.grid(row=1,column=0)

#Entry Section
pokemonEnter = Entry(root)
pokemonEnter.pack()
b1 = Button(root,text="Submit",command=doit)
b1.pack()

#showType = IntVar()

#showTypes = Checkbutton(root,text= "Show Types", variable = "showType", onvalue = "1", offvalue = "0")
#showTypes.pack()

#showMoves = Checkbutton(root,text= "Show Moves", variable = "showMove")
#showMoves.pack()

root.mainloop()