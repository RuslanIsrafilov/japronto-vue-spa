
class Config(object):
    def __init__(self):
        self._config = {
            'app_container': 'static/app-container.html',
            'host': 'localhost',
            'port': 5432,
            'debug': True
        }

    def __getitem__(self, attr_name):
        return self._config[attr_name]

    def __getattr__(self, attr_name):
        return self._config[attr_name]

cfg = Config()
