from .api_model import ApiModel

class Functions(ApiModel):
    def __init__(self, workspace):
        super().__init__(workspace.api, f'{workspace.model_path}/functions')

    def function(self, name):
        return Function(self, name)

    def create(self, payload):
        return self.send_request('POST', payload=payload)

    def list(self, function_type='SOURCE', page_size=None, page_token=None):
        return self.send_request('GET',
            params={'type':function_type, 'page_size': page_size, 'page_token': page_token})


class Function(ApiModel):
    def __init__(self, functions, name):
        super().__init__(functions.api, f'{functions.model_path}/{name}')

    def delete(self, name):
        return self.send_request('DELETE')

    def get(self):
        return self.send_request('GET')

    def update(self, payload):
        return self.send_request('PATCH', payload=payload)

    def delete(self,name):
        return self.send_request('DELETE')
