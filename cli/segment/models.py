from .api_model import ApiModel

class Functions(ApiModel):
    def __init__(self, func_type, function):
        super().__init__(function.api, f'{function.model_path}/functions')

class DestinationFiltersModel(ApiModel):
    def __init__(self, destination):
        super().__init__(destination.api, f'{destination.model_path}/filters')

    def destination_filter(self, name):
        return DestinationFilterModel(self, name)

    def create(self, payload):
        return self.send_request('POST', payload=payload)

    def list(self):
        return self.send_request('GET')

class DestinationFilterModel(ApiModel):
    def __init__(self, destinations, name):
        super().__init__(destinations.api, f'{destinations.model_path}/{name}')

    def get(self):
        return self.send_request('GET')

    def update(self, name, payload):
        return self.send_request('PATCH', payload=payload)

    def delete(self, name):
        return self.send_request('DELETE')

class GlobalDestinationFiltersModel(ApiModel):
    def __init__(self, api):
        super().__init__(api, f'filters')

    def preview(self, payload):
        return self.send_request('POST','preview', payload=payload)

