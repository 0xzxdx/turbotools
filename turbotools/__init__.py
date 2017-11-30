import requests

__title__ = 'turbotools'
__version__ = '0.0.1'
__author__ = 'ansheng'
__email__ = 'ianshengme@gmail.com'


class Turbotools(object):
    """turbotools api clss
    """
    def __init__(self, url, token, api_version='api-2.0'):
        self._url = '%s/%s' % (url, api_version)
        self._api_version = api_version
        self.headers = {}

        self._set_token(token)

        #: Create a session object for requests
        self.session = requests.Session()

    @property
    def api_version(self):
        """return api version
        """
        return self._api_version

    def _set_token(self, token):
        self.private_token = token if token else None
        if token:
            self.headers["PRIVATE-TOKEN"] = token
        elif "PRIVATE-TOKEN" in self.headers:
            del self.headers["PRIVATE-TOKEN"]