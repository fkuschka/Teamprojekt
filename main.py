# -*- coding: utf-8 -*-
__author__ = 'Fab'

from Tkinter import *
# from tkMessageBox import *


root = Tk()
root.title("Texttool")
root.resizable(width=FALSE, height=FALSE)
root.minsize(width=100, height=200)


# Frame fuer Textbereich
textframe = Frame(root, height=100, width=100)
textframe.grid(row=0, column=0)

# Frame für Eingabebereich
inputframe = Frame(root, height=50, width=100)
inputframe.grid(row=1, column=0)


# Textfeld + Scrollbar

scrollbar = Scrollbar(textframe)
textfeld = Text(textframe)
scrollbar.pack(side=RIGHT, fill=Y)
textfeld.pack(side=LEFT, fill=Y)
scrollbar.config(command=textfeld.yview)
textfeld.config(yscrollcommand=scrollbar.set)


beispiel="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."

textfeld.insert(END,beispiel)


# Eingabefelder
Label(inputframe, text="Titel").grid(row=0,column=0, columnspan=1)
e_titel=Entry(inputframe).grid(row=0,column=1, columnspan=1)
Label(inputframe, text="Autor").grid(row=1,column=0, columnspan=1)
e_titel=Entry(inputframe).grid(row=1,column=1, columnspan=1)
Label(inputframe, text="Zeitschrift").grid(row=2,column=0, columnspan=1)
e_titel=Entry(inputframe).grid(row=2,column=1, columnspan=1)
Label(inputframe, text="Band").grid(row=3,column=0, columnspan=1)
e_titel=Entry(inputframe).grid(row=3,column=1, columnspan=1)
Label(inputframe, text="Ausgabe").grid(row=4,column=0, columnspan=1)
e_titel=Entry(inputframe).grid(row=4,column=1, columnspan=1)
Label(inputframe, text="Publikationsjahr").grid(row=0,column=3, columnspan=1)
e_titel=Entry(inputframe).grid(row=0,column=4, columnspan=1)
Label(inputframe, text="Seite(Anfang)").grid(row=1,column=3, columnspan=1)
e_titel=Entry(inputframe).grid(row=1,column=4, columnspan=1)
Label(inputframe, text="Seite (Ende)").grid(row=2,column=3, columnspan=1)
e_titel=Entry(inputframe).grid(row=2,column=4, columnspan=1)
Label(inputframe, text="Anmerkungen").grid(row=3,column=3, columnspan=1)
e_titel=Entry(inputframe).grid(row=3,column=4, columnspan=1)
Label(inputframe, text="Tags").grid(row=4,column=3, columnspan=1)
e_titel=Entry(inputframe).grid(row=4,column=4, columnspan=1)

b_info=Button(inputframe, text="Info").grid(row=6,column=1)
b_save=Button(inputframe, text="Speichern").grid(row=6,column=3)
b_quit=Button(inputframe, text="Ende", command=root.quit()).grid(row=6,column=4)


root.mainloop()