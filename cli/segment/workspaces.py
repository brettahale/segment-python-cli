from .api_model import ApiModel
from .sources import Source, Sources
from .functions import Function, Functions
from .regulations import Regulations

class Workspaces(ApiModel):
    def __init__(self, api):
        super().__init__(api, f'workspaces')

    def workspace(self, name):
        return Workspace(self, name)

    def list(self):
        return self.send_request('GET')


class Workspace(ApiModel):
    def __init__(self, workspaces, name):
        self.name = name
        super().__init__(workspaces.api, f'{workspaces.model_path}/{name}')

    @property
    def sources(self):
        return Sources(self)

    def source(self, name):
        return self.sources.source(name)

    @property
    def functions(self):
        return Functions(self)

    def function(self, name):
        return self.functions.function(name)

    @property
    def regulations(self):
        return Regulations(self)

#     @property
#     def tracking_plans(self):
#         return TrackingPlans(self)
#
#     def tracking_plan(self, plan_id):
#         return self.tracking_plans.tracking_plan(plan_id)
#

#
#     def regulation(self, regulation_id):
#         return self.regulations().regulation(regulation_id)
#
#     @property
#     def roles(self):
#         return Roles(self)
#
#     @property
#     def invites(self):
#         return Invites(self)
#
#     def invite(self, invite_id):
#         self.invites.invite(invite_id)
#
#     def batch_get_summary_metrics(self, source_destination_pairs):
#         return WorkSpaceEventDeliveryMetrics(self) \
#             .batch_get_summary(source_destination_pairs)
#
#     @property
#     def suppressed_users(self):
#         return SuppressedUsers(self)

    def get(self):
        return self.send_request('GET')
