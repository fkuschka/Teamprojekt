# -*- coding: utf-8 -*-

from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString

def savexml(filename, contentdict):
    #XML Elemente erstellen

    entry = Element('entry')
    text = SubElement(entry,"text").text = contentdict["text"]
    annotations = SubElement(entry,"annotations")
    # vvv Das geht noch schöner! vvv
    title = SubElement(annotations,"title")
    author = SubElement(annotations,"author")
    journal = SubElement(annotations,"journal")
    volume = SubElement(annotations,"volume")
    edition = SubElement(annotations,"edition")
    year = SubElement(annotations,"year")
    pagestart = SubElement(annotations,"pagestart")
    pageend = SubElement(annotations,"pageend")
    comment = SubElement(annotations,"comment")
    tags = SubElement(annotations,"tags")


