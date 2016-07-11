#!/bin/bash
JENKINS_HOME=/root/.jenkins/

python $JENKINS_HOME/init.groovy.d/changetag.py

A=$( (sed -n '$=' $JENKINS_HOME/config.xml) | awk '{print $1}' )
lin=`expr $A - 1`
cp $JENKINS_HOME/config.xml $JENKINS_HOME/bkp_config.xml
echo 'adding cloud.xml at line to config.xml' $lin
sed -e "${lin}r ./cloud.xml" $JENKINS_HOME/config.xml > $JENKINS_HOME/temp_config.xml
cp $JENKINS_HOME/temp_config.xml $JENKINS_HOME/config.xml
