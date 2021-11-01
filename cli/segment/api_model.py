import os
from pathlib import Path


class ApiModel():
    def __init__(self, api, model_path):
        self.api = api
        self.model_path = model_path

    def send_request(self, method: str, path='', path_suffix='', **kwargs):
        if path_suffix:
            path = f'{self.model_path}{path_suffix}'
        else:
            path = f'{self.model_path}/{path}'
        return self.api.send_request(method, path, **kwargs)

    def write_to_file(self, path=[], data=None):
        #should merge existing file?
        file_path = os.path.join(*path)
        dir_name = os.path.dirname(file_path)
        Path(dir_name).mkdir(parents=True, exist_ok=True)
        with open(file_path, 'w+') as f:
            read_data = f.write(data)
