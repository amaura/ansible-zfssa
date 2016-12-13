#!/usr/bin/python

# Ansible ZFSSA module



DOCUMENTATION = '''
---
module: zfssa
short_description: Create projects and shares on Oracle ZFS Appliance
'''

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from ansible.module_utils.basic import *


def main():
    zfs_user='root'
    zfs_password='welcome1'

    fields = {
        "hostname": {"required": True, "type": "str"},
        }



    module = AnsibleModule(argument_spec=fields)

    url="https://"+module.params['hostname']+":215/api/access/v1"
    response=requests.get(url, auth=('zfs_username', 'zfs_password'),verify=False)


    module.exit_json(changed=False, meta=response.json())


if __name__ == '__main__':
    main()
