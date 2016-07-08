#!/bin/bashi
JENKINS_HOME=/root/.jenkins/
A=$( (sed -n '$=' $JENKINS_HOME/config.xml) | awk '{print $1}' )
lin=`expr $A - 1`
echo 'adding cloud.xml at line to config.xml' $lin
sed -e "${line}r ./cloud.xml" $JENKINS_HOME/config.xml > $JENKINS_HOME/temp_config.xml
mv $JENKINS_HOME/config.xml $JENKINS_HOME/bkp_config.xml
mv $JENKINS_HOME/temp_config.xml $JENKINS_HOME/config.xml
