#!/bin/bash

################################################################################
#
# Title:        Ansible_init.sh
# Author:       Adrian Bronder (adapted: Ron Feist)
# Date:         2020-09-03 (adapted 2020-06-08)
# Description:  Prepare the Linux host "rhel1" in the Lab for ONTAP REST API Training
#               --> Course ID: "TBD"
#
# URLs:         https://labondemand.netapp.com/lab/sl10599
#               http://docs.netapp.com/ontap-9/index.jsp
#               https://pypi.org/project/netapp-ontap/
#               https://galaxy.ansible.com/netapp/ontap
#
################################################################################

echo "--> Updating Red Hat system"
yum -y update

echo "--> Installing additional packages"
yum -y install jq

echo "--> Installing NetApp Python lib (for ZAPI use)"
pip install netapp_lib

echo "--> Installing ONTAP collection for Ansible"
ansible-galaxy collection install netapp.ontap

echo "--> Creating links for Python3"
ln -s /usr/local/bin/python3.7 /usr/bin/python3
ln -s /usr/local/bin/pip3.7 /usr/bin/pip3

echo "--> Creating aggrgates on primary cluster (cluster 1)"
$(dirname $0)/ansible_init_cluster.sh



### REMOVED FROM 1.1 to 1.2 (already installed in LoD or not relevant anymore):
: '
echo "--> Installing additional packages"
yum -y install epel-release zlib-devel openssl-devel jq

echo "--> Installing Python 3.8.2 (as alternative version)"
wget -P /opt/ https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tgz
tar xf /opt/Python-3.8.2.tgz -C /opt/
cd /opt/Python-3.8.2
./configure --enable-optimizations
make altinstall
ln -s /usr/local/bin/python3.8 /usr/bin/python3
ln -s /usr/local/bin/pip3.8 /usr/bin/pip3
cd ~

echo "--> Upgrading Python pip (for both versions)"
pip install --upgrade pip
pip3 install --upgrade pip

echo "--> Installing ONTAP Python client libraries and dependencies"
pip install requests marshmallow
pip install netapp-lib
pip3 install requests marshmallow
pip3 install netapp-lib
pip3 install netapp-ontap

echo "--> Installing Ansible"
yum -y install ansible
'
