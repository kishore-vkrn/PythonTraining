import sys

import xml.etree.ElementTree as ET
import config

tree = ET.parse('cloud.xml')
root = tree.getroot()

print root.tag
print config.nativeLibraryPath

# Cloud Settings
# nativeLibraryPath
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for i in f.iterfind('nativeLibraryPath'):
		i.text = config.nativeLibraryPath
		print 'found nativeLibraryPath changing to ',i.text

# master
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for i in f.iterfind('master'):
		i.text = config.master
		print 'found master changing to ',i.text

# jenkinsURL
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for i in f.iterfind('jenkinsURL'):
		i.text = config.jenkinsURL
		print 'found jenkinsURL changing to ',i.text

# checkpoint
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for i in f.iterfind('checkpoint'):
		i.text = config.checkpoint
		print 'found checkpoint changing to ',i.text

# onDemandRegistration
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for i in f.iterfind('onDemandRegistration'):
		i.text = config.onDemandRegistration
		print 'found onDemandRegistration changing to ',i.text

# declineOfferDuration
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for i in f.iterfind('declineOfferDuration'):
		i.text = config.declineOfferDuration
		print 'found declineOfferDuration changing to ',i.text

# Slave INFO
# labelString
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('labelString'):
				i.text = config.labelString
				print 'found labelString changing to ',i.text

# slaveCpus
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('slaveCpus'):
				i.text = config.slaveCpus
				print 'found slaveCpus changing to ',i.text

# slaveMem
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('slaveMem'):
				i.text = config.slaveMem
				print 'found slaveMem changing to ',i.text

# executorCpus
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('executorCpus'):
				i.text = config.executorCpus
				print 'found executorCpus changing to ',i.text

# maxExecutors
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('maxExecutors'):
				i.text = config.maxExecutors
				print 'found maxExecutors changing to ',i.text

# executorMem
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('executorMem'):
				i.text = 'executorMem'
				print 'found executorMem changing to ',i.text

# remoteFSRoot
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('remoteFSRoot'):
				i.text = config.remoteFSRoot
				print 'found remoteFSRoot changing to ',i.text

# idleTerminationMinutes
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('idleTerminationMinutes'):
				i.text = config.idleTerminationMinutes
				print 'found idleTerminationMinutes changing to ',i.text

# jvmArgs
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('jvmArgs'):
				i.text = config.jvmArgs
				print 'found jvmArgs changing to ',i.text

# jnlpArgs
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('jnlpArgs'):
				i.text = config.jvmArgs
				print 'found jvmArgs changing to ',i.text

# defaultSlave
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('defaultSlave'):
				i.text = config.defaultSlave
				print 'found defaultSlave changing to ',i.text
# type
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('containerInfo'):
				for l in i.iterfind('type'):	
					l.text = config.type1
					print 'found type changing to ',l.text

# dockerImage
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('containerInfo'):
					for l in i.iterfind('dockerImage'):
						l.text = config.dockerImage
						print 'found dockerImage changing to ',l.text

# containerPath
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('containerInfo'):
				for l in i.iterfind('volumes'):
					for m in l.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo_-Volume'):
						for n in m.iterfind('containerPath'):
							n.text = config.containerPath
							print 'found containerPath changing to ',n.text

# hostPath
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('containerInfo'):
				for l in i.iterfind('volumes'):
					for m in l.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo_-Volume'):
						for n in m.iterfind('hostPath'):
							n.text = config.hostPath
							print 'found hostPath changing to ',n.text

# readOnly
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('containerInfo'):
				for l in i.iterfind('volumes'):
					for m in l.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo_-Volume'):
						for n in m.iterfind('readOnly'):
							n.text = config.readOnly
							print 'found readOnly changing to ',n.text

# networking
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('containerInfo'):
				for l in i.iterfind('type'):
					i.text = config.networking
					print 'found networking changing to ',i.text

# useCustomDockerCommandShell
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('containerInfo'):
				for l in i.iterfind('type'):
					i.text = config.useCustomDockerCommandShell
					print 'found useCustomDockerCommandShell changing to ',i.text

# dockerPrivilegedMode
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('containerInfo'):
				for l in i.iterfind('type'):
					i.text = config.dockerPrivilegedMode
					print 'found dockerPrivilegedMode changing to ',i.text

# dockerForcePullImage
for f in root.findall('org.jenkinsci.plugins.mesos.MesosCloud'):
	for k in f.iterfind('slaveInfos'):
		for j in k.iterfind('org.jenkinsci.plugins.mesos.MesosSlaveInfo'):
			for i in j.iterfind('containerInfo'):
				for l in i.iterfind('type'):
					i.text = config.dockerForcePullImage
					print 'found dockerForcePullImage changing to ',i.text
		
tree.write('cloud.xml')