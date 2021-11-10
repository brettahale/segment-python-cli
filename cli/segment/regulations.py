from .api_model import ApiModel

class Regulations(ApiModel):
    def __init__(self, workspace):
        super().__init__(workspace.api, f'{workspace.model_path}/regulations')

    def create(self, payload):
        return self.send_request('POST', payload=payload)

    def list(self):
        return self.send_request('GET')
