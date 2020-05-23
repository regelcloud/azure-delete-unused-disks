#  Azure delete unused disks
This consist python function to delete unused disks of microsoft azure 

## Setup instruction

- Install and setup python virtual env
1. git clone https://github.com/regelcloud/azure-delete-unused-disks.git
2. cd azure-delete-unused-disks
3. python3 -m  venv venv
4. source venv/bin/activate

- Set Azure Credentials
1. open `delete_unused_disks.py`
2. Add below azure creds
```
    os.environ['AZURE_SUBSCRIPTION_ID'] = ""
    os.environ['AZURE_CLIENT_ID'] = ""
    os.environ['AZURE_CLIENT_SECRET'] = ""
    os.environ['AZURE_TENANT_ID'] = ""
```
3. Run script to cleanup unused disks from account>
`  python delete_unused_disks.py --resource-group <ResourceGroupName> `

## Support
In case of any issues or bugs please reach to us *sales@regelcloud.com*