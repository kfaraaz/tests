#!/bin/sh

set -x

AUTO_HOME=~/drillAutomation
Drill_GitURL=$1
Drill_GitCommitID=$2
Drill_Version=$3
Timeout=600

### Check Usage
if [ "$#" != "3" ]
then
        printf "Usage:\nbuildDrill.sh\n\t-Drill Git URL\n\t-Drill Commit ID\n\t-Drill Version\n\n"
        exit
fi

# Create the builds directory if not exists
if [ ! -d "$AUTO_HOME/builds" ]; then
        mkdir -p $AUTO_HOME/builds
fi

# Stop any existing Drillbits
sshpass -p "mapr" pssh -t ${Timeout} -A -h $AUTO_HOME/scripts/hosts -O LogLevel=quiet -O UserKnownHostsFile=/dev/null -O StrictHostKeyChecking=no "/opt/mapr/drill/drill-${Drill_Version}/bin/drillbit.sh stop"

# Clone Drill into Docker Host
cd $AUTO_HOME/builds
rm -Rf *drill*
git clone $Drill_GitURL > /dev/null 2>&1
cd *drill*
git checkout $Drill_GitCommitID

# Build Drill with MapR profile
mvn clean install -U -DskipTests -Pmapr
