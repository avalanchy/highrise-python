import requests


HIGHRISE_URL = 'https://{}.highrisehq.com/'


class HighriseAPIError(Exception):
    pass


class HighriseAPI(object):

    def __init__(self, subdomain, key, app_name=None, email=None):
        self.key = key
        self.req = requests.Request(
            method='GET',
            url=HIGHRISE_URL.format(subdomain),
            headers={
                'User-Agent': self._build_user_agent(app_name, email),
            },
            auth=(key, ''),
        )

    @staticmethod
    def _build_user_agent(app_name, email):
        header = 'Python SDK'
        if app_name:
            header += ' ' + app_name
        if email:
            header += ' (' + email + ')'
        return header

    def request(self, rtype):
        pass

    def me(self):
        self.req.url += 'me.xml'
        return requests.Session()\
                       .send(self.req.prepare())


api = HighriseAPI('<subdomain>', '<api_key>')
api.me()