from .api_model import ApiModel
from .filters import Filters

class Destinations(ApiModel):
    def __init__(self, source):
        super().__init__(source.api, f'{source.model_path}/destinations')

    def destination(self, name):
        return Destination(self, name)

    def create(self, payload):
        return self.send_request('POST', payload=payload)

    def list(self,page_size=None, page_token=None):
        return self.send_request('GET',
            params={'page_size': page_size, 'page_token': page_token})

class Destination(ApiModel):
    def __init__(self, destinations, name):
        super().__init__(destinations.api, f'{destinations.model_path}/{name}')

    @property
    def filters(self):
        return Filters(self)

    def filter(self, name):
        self.filters.filter(name)

#     @property
#     def event_delivery_metrics(self):
#         return EventDeliveryMetricsModel(self)

    def get(self):
        return self.send_request('GET')

    def update(self, payload):
        return self.send_request('PATCH', payload=payload)

    def delete(self,name):
        return self.send_request('DELETE')