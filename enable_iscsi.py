#!/usr/bin/env python3

################################################################################
#
# Title:	enable_iscsi_pri_svm.py
# Author:	Ronald Feist
# Date:		2020-06-10
# Description:	Enable iSCSI on the Primary SVM
#		with ONTAP Python client library
#
# Resources:    netapp_ontap.resources.nfs_service
#
# URLs:		http://docs.netapp.com/ontap-9/index.jsp
#		https://pypi.org/project/netapp-ontap/
#		https://library.netapp.com/ecmdocs/ECMLP2858435/html/index.html
#
################################################################################

import json, os, sys
from netapp_ontap import config, HostConnection, NetAppRestError
from netapp_ontap.resources import IscsiService


### Step 1 - Read in global variables
with open(os.path.dirname(sys.argv[0])+'/global.vars') as json_file:
	global_vars = json.load(json_file)


### Step 2 - Configure connection
config.CONNECTION = HostConnection(
	global_vars["PRI_CLU"],
	username=global_vars["PRI_CLU_USER"],
	password=global_vars["PRI_CLU_PASS"],
	verify=False
)


### Step 3 - Create operation
iscsi = IscsiService.from_dict(
{
  "svm": {
    "name": global_vars["PRI_SVM"]
  },
  "enabled": "true",
  }
)

print("--> Starting Service operation")
try:
	iscsi.post()
	print("--> iSCSI enabled successfully on SVM \"{}\"".format(iscsi.svm.name))
except NetAppRestError as err:
	print("--> Error: iSCSI was not enabled:\n{}".format(err))
print("")