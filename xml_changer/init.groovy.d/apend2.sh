#!/bin/bash
JENKINS_HOME=/root/.jenkins/
python $JENKINS_HOME/init.groovy.d/changetag.py

B=$( (sed -n '$=' $JENKINS_HOME/init.groovy.d/cloud.xml) | awk '{print $1}' )
echo 'Total numbe of lines at cloud.xml ' $B
sed -e '$ a  <!-- Modified Cloud -->' $JENKINS_HOME/init.groovy.d/cloud.xml > $JENKINS_HOME/init.groovy.d/temp_cloud.xml
rm -rf  $JENKINS_HOME/init.groovy.d/cloud.xml
mv $JENKINS_HOME/init.groovy.d/temp_cloud.xml $JENKINS_HOME/init.groovy.d/cloud.xml
echo "Modified cloud"

A=$( (sed -n '$=' $JENKINS_HOME/config.xml) | awk '{print $1}' )
lin=`expr $A - 1`
echo 'adding cloud.xml at line to config.xml' $lin
sed -e "${line} a $JENKINS_HOME/init.groovy.d/cloud.xml" $JENKINS_HOME/config.xml > $JENKINS_HOME/temp_config.xml
mv $JENKINS_HOME/config.xml $JENKINS_HOME/bkp_config.xml
mv $JENKINS_HOME/temp_config.xml $JENKINS_HOME/config.xml
