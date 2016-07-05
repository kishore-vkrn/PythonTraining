import sys

import xml.etree.ElementTree as ET

tree = ET.parse('cloud.xml')
root = tree.getroot()

print root.tag


for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for i in f.iterfind('master'):
		i.text = 'changes'
		print 'found master changing to ',i.text

tree.write('cloud.xml')
	
