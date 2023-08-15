#!/usr/bin/env python3

################################################################################
#
# Title:	create_pri_svm.py
# Author:	Ronald Feist
# Date:		2020-06-10
# Description:	Create a primary SVM for iSCSI
#		with ONTAP Python client library
#
# Resources:    netapp_ontap.resources.svm
#
# URLs:		http://docs.netapp.com/ontap-9/index.jsp
#		https://pypi.org/project/netapp-ontap/
#		https://library.netapp.com/ecmdocs/ECMLP2858435/html/index.html
#
################################################################################

import json, os, sys
from netapp_ontap import config, HostConnection, NetAppRestError
from netapp_ontap.resources import Svm


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


### Step 3 - Create opeartion
# execute create operation
svm = Svm.from_dict(
{
  "name": global_vars["PRI_SVM"],
  "aggregates": [
    {
      "name": global_vars["PRI_AGGR"]
    }
],
  "comment": "Created with ONTAP PCL"
})

print("--> Starting SVM create operation")
try:
	svm.post()
	print("--> SVM \"{}\" created successfully".format(svm.name))
except NetAppRestError as err:
	print("--> Error: SVM was not created:\n{}".format(err))
print("")