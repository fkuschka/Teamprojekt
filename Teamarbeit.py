# -*- coding: utf-8 -*-

import os, sys
sys.dont_write_bytecode = True

from Tkinter import *
from Document import Document
from MainGui import MainGui
import tkFileDialog

# Alle Attribute eines Dokuments
document_attributes = [
    "Titel",
    "Autor",
    "Zeitschrift",
    "Band",
    "Ausgabe",
    "Publikationsjahr",
    "Startseite",
    "Endseite",
    "Anmerkungen",
    "Tags"]

filetk = Tk()
filetk.withdraw()
# Pfad zu den Dokumenten
path = tkFileDialog.askdirectory(parent = filetk)

# Dateinamen aller Dokumente
document_filenames = os.listdir(path)

# Die geladenen Dokumente indiziert durch ihren Dateinamen
loaded_documents = {}
for name in document_filenames:
    loaded_documents[name] = Document(path + "/" + name, document_attributes)

# Initialisiert die Benutzeroberfläche
MainGui(document_attributes, loaded_documents)
