import requests
zfs_user='root'
zfs_password='welcome1'

url="https://192.168.59.103:215/api/access/v1"
response=requests.get(url, auth=('zfs_username', 'zfs_password'),verify=False)

print response.json()
