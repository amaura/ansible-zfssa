#!/usr/bin/python

# Ansible ZFSSA module



DOCUMENTATION = '''
---
module: zfssa
short_description: Create projects and shares on Oracle ZFS Appliance
'''


from ansible.module_utils.basic import *

def main():

    module = AnsibleModule(argument_spec={})
    response = {"hello": "world"}
    module.exit_json(changed=False, meta=response)


if __name__ == '__main__':  
    main()
