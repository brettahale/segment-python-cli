import json
import requests
from .workspaces import Workspaces
from .models import Functions
from .sources import Sources

class SegmentConfigApi():
    def __init__(self, access_token=None, workspace=None, base_url='https://platform.segmentapis.com', version='v1beta'):
        self.access_token = access_token
#         self.workspace = workspace
        self.base_url = base_url
        self.version = version

    def send_request(self, verb, path, payload={}, params={}):
        #remove params that have null values (these are optional)
        params = {k: v for k, v in params.items() if v is not None}

        url = f'{self.base_url}/{self.version}/{path}'
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }

        req_config = {'headers': headers, 'params': params}
        if payload is not None:
            req_config['data'] = payload

        print(verb, url, req_config)
        response = requests.request(verb, url, **req_config)

        response.raise_for_status()
        return response.json()


    @property
    def integrations_catalog(self):
        return IntegrationsCatalog(self)

    @property
    def workspaces(self):
        return Workspaces(self)

    def workspace(self, name):
        return self.workspaces.workspace(name)

    @property
    def destination_filters(self):
        return GlobalDestinationFilters(self)

    def role_policies(self, role_name):
        return RolePolicies(role_name)

    def role_policy(self, policy_name):
        return RolePolicy(policy_name)