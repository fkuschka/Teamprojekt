# -*- coding: utf-8 -*-

import os
import tkFileDialog
from Tkinter import *
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString
import codecs


root = Tk()

# Pfad zu den Dokumenten
path = tkFileDialog.askdirectory(parent = root)


class Document:
    text = ""
    def __init__(self, filename, attributes):
        file_handle = open(filename)
        self.text = file_handle.read()

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

# Dateinamen aller Dokumente
document_filenames = os.listdir(path)

# Die geladenen Dokumente indiziert durch ihren Dateinamen
loaded_documents = {}
for name in document_filenames:
    loaded_documents[name] = Document(path+ "/" + name, document_attributes)

        
# Frame für Eingabebereich
inputframe = Frame(root, height=50, width=100)
inputframe.grid(row=1, column=0)


# Initialisiert die Benutzeroberfläche
def initgui():
    
    document_view = DocumentView(root, document_attributes)
    
    # Buttons für Info, Speichern, Beenden
    b_info = Button(inputframe, text="Info")
    b_info.grid(row=6, column=1)
    b_save = Button(inputframe, text="Speichern", command=lambda: document_view.savexml())
    b_save.grid(row=6, column=3)
    b_quit = Button(inputframe, text="Beenden", command=root.quit)
    b_quit.grid(row=6, column=4)
    
    Label(inputframe, text="Dateien").grid(row=0, column=0)
    listbox = Listbox(inputframe)
    listbox.grid(row=1, column=0, rowspan=5, columnspan=1)
    for item in document_filenames:
        listbox.insert(END, item)
    
    # Anklicken in der Listbox zeigt das ausgewählte Dokument an.
    def choose_document():
        
        # Angeklickten Namen herausfinden
        current_document_name = listbox.get(listbox.curselection())
        
        # Dokument mit dem Namen im DocumentView anzeigen
        document_view.update(loaded_documents[current_document_name])

        # Filename setzen
        document_view.filename = listbox.get(listbox.curselection())

    listbox.bind("<<ListboxSelect>>", lambda event: choose_document())
        
    root.mainloop()


class DocumentView:
    entries = {}
    current_document = None
    filename = ""

    def __init__(self, root, document_attributes):
        self.document_attributes = document_attributes
            
        # Eingabefelder mit Titel erstellen
        Label(inputframe, text="Titel").grid(row=0, column=2, columnspan=1)
        self.e_title = Entry(inputframe)
        self.e_title.grid(row=0, column=3, columnspan=1)
        Label(inputframe, text="Autor").grid(row=1, column=2, columnspan=1)
        self.e_author = Entry(inputframe)
        self.e_author.grid(row=1, column=3, columnspan=1)
        Label(inputframe, text="Zeitschrift").grid(row=2, column=2, columnspan=1)
        self.e_journal = Entry(inputframe)
        self.e_journal.grid(row=2, column=3, columnspan=1)
        Label(inputframe, text="Band").grid(row=3, column=2, columnspan=1)
        self.e_volume = Entry(inputframe)
        self.e_volume.grid(row=3, column=3, columnspan=1)
        Label(inputframe, text="Ausgabe").grid(row=4, column=2, columnspan=1)
        self.e_edition = Entry(inputframe)
        self.e_edition.grid(row=4, column=3, columnspan=1)
        Label(inputframe, text="Publikationsjahr").grid(row=0, column=4, columnspan=1)
        self.e_year = Entry(inputframe)
        self.e_year.grid(row=0, column=5, columnspan=1)
        Label(inputframe, text="Seite(Anfang)").grid(row=1, column=4, columnspan=1)
        self.e_pagestart = Entry(inputframe)
        self.e_pagestart.grid(row=1, column=5, columnspan=1)
        Label(inputframe, text="Seite (Ende)").grid(row=2, column=4, columnspan=1)
        self.e_pageend = Entry(inputframe)
        self.e_pageend.grid(row=2, column=5, columnspan=1)
        Label(inputframe, text="Anmerkungen").grid(row=3, column=4, columnspan=1)
        self.e_comment = Entry(inputframe)
        self.e_comment.grid(row=3, column=5, columnspan=1)
        Label(inputframe, text="Tags").grid(row=4, column=4, columnspan=1)
        self.e_tags = Entry(inputframe)
        self.e_tags.grid(row=4, column=5, columnspan=1)
            
        # Frame fuer Textbereich
        textframe = Frame(root, height=100, width=100)
        textframe.grid(row=0, column=0)

        # Textfeld + Scrollbar
        scrollbar = Scrollbar(textframe)
        self.textfield = Text(textframe)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.textfield.pack(side=LEFT, fill=Y)
        scrollbar.config(command=self.textfield.yview)
        self.textfield.config(yscrollcommand=scrollbar.set)

        # Beispieltext
        self.beispiel = "Datei auswaehlen"
        self.textfield.insert(END, self.beispiel)

    def update(self, document):
        self.current_document = document
        
        # Anzeigen vom Text des neuen Dokuments
        self.textfield.delete(1.0, END)
        self.textfield.insert(END, document.text)

    # XML Elemente und Baum erstellen
    def savexml(self):
        # self.filename = self.listbox.get(self.listbox.curselection())+".xml"
        # XML root
        entry = Element('entry')

        # XML Eintrag fuer text
        text = SubElement(entry, "text")
        text.text = self.beispiel
        # XML Verzeichnis fuer Anmerkungen

        annotations = SubElement(entry, "annotations")

        # XML Eintraege fuer Anmerkungen
        title = SubElement(annotations, "title")
        title.text = self.e_title.get()
        author = SubElement(annotations, "author")
        author.text = self.e_author.get()
        journal = SubElement(annotations, "journal")
        journal.text = self.e_journal.get()
        volume = SubElement(annotations, "volume")
        volume.text = self.e_volume.get()
        edition = SubElement(annotations, "edition")
        edition.text = self.e_edition.get()
        year = SubElement(annotations, "year")
        year.text = self.e_year.get()
        pagestart = SubElement(annotations, "pagestart")
        pagestart.text = self.e_pagestart.get()
        pageend = SubElement(annotations, "pageend")
        pageend.text = self.e_pageend.get()
        comment = SubElement(annotations, "comment")
        comment.text = self.e_comment.get()
        tags = SubElement(annotations, "tags")
        tags.text = self.e_tags.get()

        # XML in String parsen und schoen machen :)
        xml = tostring(entry)
        dom = parseString(xml)
        tosave = dom.toprettyxml('    ')
        # print tosave
        # print self.filename

        # Dateiname schoen machen
        new_filename = self.filename[:-4]

        # XML in datei Speichern
        with codecs.open(path + "/" + new_filename + ".xml", 'w', 'utf-8') as output_file:
            output_file.write(tosave.decode('utf-8'))

initgui()
