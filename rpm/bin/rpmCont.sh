#!/bin/bash

SCRIPT_NAME=$0
BASE_DIR="$(dirname $SCRIPT_NAME)"
#GIT data
GIT_DIR=$(readlink -f $BASE_DIR/../..)

#RPM Controller Path
M2M_APP_DIR=$GIT_DIR

#SPECS
SPECS_DIR=$M2M_APP_DIR/rpm/spec

#Data parameters
VERSION=$1
REVISION=$2

RPM_DIR=$(rpm --eval '%{_rpmdir}')

m2m_create_rpm () {
        if [ -n $1 ];then
                 eval "rpmbuild -ba $1 -D \"_gs_version $VERSION\" -D \"_gs_revision $REVISION\" -D \"_gitdir $GIT_DIR\" $2";
        fi
        if [ $? -ne 0 ]
        then
                echo "Error creating RPM from $1. Error $?"
                echo "Extra data: $2"
                return 1;
        fi;
}

create_rpm_controller () {
        echo "Creating RPM of RPM Controller..."
        m2m_create_rpm $SPECS_DIR/rpmCont.spec
        if [ $? -eq 0 ];then
                echo "RPM Conrtoller packed!"
        fi;
}

create_rpm_controller
if [ $? -ne 0 ];then
        exit 1
fi
