# -*- coding: utf-8 -*-
__author__ = 'Fab'

from Tkinter import *
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString
import codecs


class Teamprojekt(object):
    def __init__(self):
        root = Tk()
        root.title("Texttool")
        root.resizable(width=FALSE, height=FALSE)
        root.minsize(width=100, height=150)

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

        # Beispieltext
        self.beispiel = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
        textfeld.insert(END, self.beispiel)
        self.filename = "test.xml"


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

        Label(inputframe, text="Dateien").grid(row=0, column=0)
        self.listbox = Listbox(inputframe)
        self.listbox.grid(row=1, column=0, rowspan=5, columnspan=1)

        # Buttons für Info, Speichern, Beenden
        self.b_info = Button(inputframe, text="Info")
        self.b_info.grid(row=6, column=2)
        self.b_save = Button(inputframe, text="Speichern", command=lambda: self.savexml())
        self.b_save.grid(row=6, column=3)
        self.b_quit = Button(inputframe, text="Beenden", command=root.quit)
        self.b_quit.grid(row=6, column=4)

        root.mainloop()

    # XML Elemente erstellen
    def savexml(self):

        entry = Element('entry')
        text = SubElement(entry, "text")
        text.text = self.beispiel
        annotations = SubElement(entry, "annotations")
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

        xml = tostring(entry)
        dom = parseString(xml)
        tosave = dom.toprettyxml('    ')
        print tosave

        with codecs.open(self.filename, 'w', 'utf-8') as output_file:
            output_file.write(tosave.decode('utf-8'))


if __name__ == "__main__":
    projekt = Teamprojekt()

