from azure.mgmt.resource import ResourceManagementClient
# from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.common.credentials import ServicePrincipalCredentials
import os
import argparse
import datetime

def get_credentials():
    subscription_id = os.environ['AZURE_SUBSCRIPTION_ID']
    credentials = ServicePrincipalCredentials(
        client_id=os.environ['AZURE_CLIENT_ID'],
        secret=os.environ['AZURE_CLIENT_SECRET'],
        tenant=os.environ['AZURE_TENANT_ID']
    )
    return credentials, subscription_id

def run(resource_group_name):
    credentials, subscription_id = get_credentials()
    resource_client = ResourceManagementClient(credentials, subscription_id)
    compute_client = ComputeManagementClient(credentials, subscription_id)
    # network_client = NetworkManagementClient(credentials, subscription_id)

    # for  item in resource_client.resource_groups.list():
    #     print(item)
    disks = compute_client.disks.list_by_resource_group(resource_group_name, custom_headers=None, raw=False)
    for disk  in disks:
        print("Today's Date",datetime.datetime.now())
        # print(disk.managed_by, disk.disk_state)
        print("Disk Created Date:", disk.time_created)
        date_format = "%Y-%m-%d %H:%M:%S.%f"
        a = datetime.datetime.strptime(str(datetime.datetime.now()), date_format)
        b = datetime.datetime.strptime(str(disk.time_created).split('+')[0], date_format)
        delta = b - a
        print("Disk created before {} days".format(int(delta.days)))
        if not disk.managed_by and disk.disk_state == 'Unattached' and int(delta.days) > 7:
            print("[INFO] Deleting unattached disk {} in resource group {}".format(disk.name, resource_group_name))
            disks = compute_client.disks.delete(resource_group_name, disk.name, custom_headers=None, raw=False, polling=True)
        else:
            print("[INFO]  Skiiping!! Disk {} is attached  to source {} and  belongs to resource group {}".format(disk.name, disk.managed_by, resource_group_name))

if __name__ ==  "__main__":

    os.environ['AZURE_SUBSCRIPTION_ID'] = ""
    os.environ['AZURE_CLIENT_ID'] = ""
    os.environ['AZURE_CLIENT_SECRET'] = ""
    os.environ['AZURE_TENANT_ID'] = ""

    parser = argparse.ArgumentParser()
    parser.add_argument('--resource-group',
                        help='Resource Group Name')

    args = parser.parse_args()
    # print(args)
    resource_group_name = args.resource_group
    run(resource_group_name)