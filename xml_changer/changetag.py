import sys

import xml.etree.ElementTree as ET

tree = ET.parse('cloud.xml')
root = tree.getroot()

print root.tag
# Cloud Settings
# nativeLibraryPath
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for i in f.iterfind('nativeLibraryPath'):
		i.text = 'changes'
		print 'found master changing to ',i.text

# master
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for i in f.iterfind('master'):
		i.text = 'changes'
		print 'found master changing to ',i.text

# jenkinsURL
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for i in f.iterfind('jenkinsURL'):
		i.text = 'jenkinsURL'
		print 'found master changing to ',i.text

# checkpoint
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for i in f.iterfind('checkpoint'):
		i.text = 'checkpoint'
		print 'found master changing to ',i.text

# onDemandRegistration
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for i in f.iterfind('onDemandRegistration'):
		i.text = 'onDemandRegistration'
		print 'found master changing to ',i.text

# declineOfferDuration
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for i in f.iterfind('declineOfferDuration'):
		i.text = 'declineOfferDuration'
		print 'found master changing to ',i.text

# Slave INFO
# labelString
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('labelString'):
				i.text = 'labelString'
				print 'found master changing to ',i.text

# slaveCpus
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('slaveCpus'):
				i.text = 'slaveCpus'
				print 'found master changing to ',i.text

#-------------
# slaveMem
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('slaveMem'):
				i.text = 'slaveMem'
				print 'found master changing to ',i.text

# executorCpus
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('executorCpus'):
				i.text = 'executorCpus'
				print 'found master changing to ',i.text

# maxExecutors
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('maxExecutors'):
				i.text = 'maxExecutors'
				print 'found master changing to ',i.text

# executorMem
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('executorMem'):
				i.text = 'executorMem'
				print 'found master changing to ',i.text

# remoteFSRoot
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('remoteFSRoot'):
				i.text = 'remoteFSRoot'
				print 'found master changing to ',i.text

# idleTerminationMinutes
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('idleTerminationMinutes'):
				i.text = 'idleTerminationMinutes'
				print 'found master changing to ',i.text

# jvmArgs
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('jvmArgs'):
				i.text = 'jvmArgs'
				print 'found master changing to ',i.text

# jnlpArgs
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('jnlpArgs'):
				i.text = 'jnlpArgs'
				print 'found master changing to ',i.text

# defaultSlave
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('defaultSlave'):
				i.text = 'defaultSlave'
				print 'found master changing to ',i.text

# type
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('type'):
				i.text = 'type'
				print 'found master changing to ',i.text

# dockerImage
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('dockerImage'):
				i.text = 'dockerImage'
				print 'found master changing to ',i.text

# containerPath
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('containerPath'):
				i.text = 'containerPath'
				print 'found master changing to ',i.text

# hostPath
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('hostPath'):
				i.text = 'hostPath'
				print 'found master changing to ',i.text

# readOnly
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('readOnly'):
				i.text = 'readOnly'
				print 'found master changing to ',i.text

# networking
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('networking'):
				i.text = 'networking'
				print 'found master changing to ',i.text

# useCustomDockerCommandShell
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('useCustomDockerCommandShell'):
				i.text = 'useCustomDockerCommandShell'
				print 'found master changing to ',i.text

# dockerPrivilegedMode
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('dockerPrivilegedMode'):
				i.text = 'dockerPrivilegedMode'
				print 'found master changing to ',i.text

# dockerForcePullImage
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('dockerForcePullImage'):
				i.text = 'dockerForcePullImage'
				print 'found master changing to ',i.text
		
tree.write('cloud.xml')