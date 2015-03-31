# -*- coding: utf-8 -*-

from Tkinter import *

# Zeigt Attribute und den Inhalt eines Dokument-Objekts an
class DocumentView:

	def __init__(self, root, document_attributes):
		self.document_attributes = document_attributes
		
		# Alle Entries, die Dokumentattribute darstellen
		self.entries = {}
		
		# Das aktuell angezeigte Dokument
		self.current_document = None
		
		# Beschriftung der Eingabefelder
		for i in range(0, 10):
			Label(root, text = document_attributes[i] + ":").grid(row = 2*i)
		
		# Erstellen der Eingabefelder
		for i in range(0, 10):
			entry = Entry(root)
			entry.grid(row=1 + 2*i, column=0)
			self.entries[document_attributes[i]] = entry
			
		# Erstellen des Textfeldes
		self.textfield = Text(root, height=35, width=80)
		self.textfield.grid(rowspan=20, row=0, column=1)

		
	# Aktualisiert die eines Dokuments auf die aktuellen Entrytexte
	def _save_to_document(self, document):
		for attribute in self.document_attributes:
			entry = self.entries[attribute]
			text = entry.get()
			document.tags[attribute] = text
	
	# Ändert die Anzeige auf die Daten eines neuen Dokuments
	def update(self, document):
		if self.current_document is not None:
			self._save_to_document(self.current_document)
			
		self.current_document = document
		
		# Anzeigen vom Text des neuen Dokuments
		self.textfield.delete(1.0, END)
		if document is not None:
			self.textfield.insert(END, document.text)

		# Anzeigen von den Attributen des neuen Dokuments
		for attribute in self.document_attributes:
			entry = self.entries[attribute]
			entry.delete(0, END)
			if document is not None:
				attribut_text = document.tags[attribute]
				entry.insert(END, attribut_text)
			
