import sys
import xml.etree.ElementTree as ET

class Users(object):
    def __init__(self, users=None):
        self.doc = ET.parse("users.xml")
        self.root = self.doc.getroot()