# -*- coding: utf-8 -*-

from xml.etree.ElementTree import ElementTree, Element, SubElement, tostring
from xml.dom.minidom import parseString
import codecs

# Repräsentiert den Inhalt einer Textdatei und die dazugehörigen Attribute
class Document:

    def __init__(self, filename, attributes):
        file_handle = open(filename)
        self.text = file_handle.read()
        
        self.tags = {}
        
        for attribute in attributes:
            self.tags[attribute] = ""
        
    # Speichert das Dokument mit Attributen in eine Datei
    def save_to_file(self, filename):
        entry = Element('entry')
        
        text = SubElement(entry, "text")
        text.text = self.text
        
        annotations = SubElement(entry, "annotations")
        for tag in self.tags:
            element = SubElement(annotations, tag)
            element.text = self.tags[tag]
        
        # XML in String parsen und schoen machen :)
        xml = tostring(entry)
        dom = parseString(xml)
        tosave = dom.toprettyxml('    ')

        #ElementTree(entry).write(filename)
        with codecs.open(filename, 'w', 'utf-8') as output_file:
            output_file.write(tosave.decode('utf-8'))
