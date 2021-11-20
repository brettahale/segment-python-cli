from .api_model import ApiModel

class Regulations(ApiModel):

    def __init__(self, workspace):
        super().__init__(workspace.api, f'{workspace.model_path}/regulations')

    def regulation(self, id):
        return Regulation(self, id)

    def create(self, payload):
        return self.send_request('POST', payload=payload)

    def list(self):
        return self.send_request('GET')


class Regulation(ApiModel):

    def __init__(self, regulations, id):
        super().__init__(regulations.api, f'{regulations.model_path}/{id}')

    def get(self):
        return self.send_request('GET')

    def delete(self):
        return self.send_request('DELETE')
