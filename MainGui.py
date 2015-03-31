# -*- coding: utf-8 -*-

import os

from Tkinter import *
from tkMessageBox import *
from DocumentView import DocumentView

class MainGui:
    
    def __init__(self, document_attributes, loaded_documents): 
    
        self.root = Tk()
        
        self.document_view = DocumentView(self.root, document_attributes)
        
        # Erstellen des Save-Buttons
        def save_documents_as_xml():
            # Erzwinge speichern aller Änderungen in document_view
            self.document_view.update(self.document_view.current_document)
            
            # Speichere alle offenen Dateien
            for filename, document in loaded_documents.iteritems():
                (root, ext) = os.path.splitext(filename)
                document.save_to_file(root+".xml")
        
        def show_info():
            showinfo("Info","Projektseminar Wissensrepräsentation WS14/15 Teamprojekt von Fabian Kuschka-Kleibrink, Hilal Catak, Pascal Hiller")
                
        self.info_button = Button(self.root, text="Info", command = show_info)
        self.info_button.grid(row=21, column=0)
        
        self.save_button = Button(self.root, text="Speichern", command = save_documents_as_xml)
        self.save_button.grid(row=21, column=1)
        
        # Erstellen des Verlassen-Buttons
        self.quit_button = Button(self.root, text="Verlassen", command = self.root.quit)
        self.quit_button.grid(row=21, column=2)
    
        # Erstellen der Dokumentliste
        self.listbox = Listbox(self.root)
        self.listbox.grid(rowspan=20, row=0, column=2)
        for filename in loaded_documents:
            self.listbox.insert(END, filename)
                
        # Anklicken in der Listbox zeigt das ausgewählte Dokument an.
        def choose_document():
            
            # Angeklickten Namen herausfinden
            current_document_name = self.listbox.get(self.listbox.curselection())
            
            # Dokument mit dem Namen im DocumentView anzeigen
            self.document_view.update(loaded_documents[current_document_name])
        
        self.listbox.bind("<<ListboxSelect>>", lambda event :choose_document() )
            

        self.root.mainloop()
