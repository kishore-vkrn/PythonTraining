#!/bin/bash
println "Executing cloud changes"
def exitValue = "appendtoxml.sh".execute().exitValue()
if(!exitValue) {
	println "REview your config settings"
}

