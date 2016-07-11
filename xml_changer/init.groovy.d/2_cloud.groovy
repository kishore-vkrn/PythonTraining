#!/bin/bash
println "Executing cloud changes"
def action = "sh /root/.jenkins/init.groovy.d/appendtoxml.sh"
println action.execute().text
