#!/usr/bin/env python3

"""
Client for MIT People API

See https://developer.mit.edu/api-people
"""

__author__ = 'Micah Smith'
__license__ = 'MIT'

import configparser
import requests


def get_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config


class Client:

    _API_ROOT = 'https://mit-people-v3.cloudhub.io/people/v3'

    def __init__(self, client_id=None, client_secret=None):
        """MIT People API client object

        Args:
            client_id (str)
            client_secret (str)
        """
        if client_id is None:
            config = get_config()
            client_id = config['credentials']['client_id']
        if client_secret is None:
            config = get_config()
            client_secret = config['credentials']['client_secret']
        self._client_id = client_id
        self._client_secret = client_secret

    @property
    def _headers(self):
        return {
            'accept': 'application/json',
            'client_id': self._client_id,
            'client_secret': self._client_secret,
        }

    def _get(self, path, params=None):
        url = self._API_ROOT + str(path)
        headers = self._headers
        if params is None:
            params = {}
        res = requests.get(url, params=params, headers=headers)
        res.raise_for_status()
        return res.json()


    def people(self, familyName='', offset=0, limit=100,
                     affiliation=None, q=None, minimalData=False):
        """Retrieve information about people at MIT

        Args:
            familyName (str): the family name of the person
            offset (int): the offset of the first record to return
            limit (int): the maximum number of records to return
            affiliation (str): the affiliation type (student|staff|affiliate)
            q (str): used in conjunction with minimal data = true to return
                Cached Ldap data quickly. This is used as the search string. You
                can enter 2 values separated by either a space or plus sign(+).
            minimalData (bool): if set to true, then only ldap data is
                returned. This makes the search much faster.
        """
        path = '/people'
        params = {
            'familyName': familyName,
            'offset': offset, 
            'limit': limit,
            'minimalData': minimalData
        }
        if affiliation is not None:
            params['affiliation'] = affiliation
        if q is not None:
            params['q'] = q
        return self._get(path, params=params)

    def person(self, kerberosId):
        """Retrieve information about a person at MIT based on their kerberos ID

        Args:
            kerberosId (str): the kerberos ID
        """
        path = f'/people/{kerberosId}'
        return self._get(path)

        params = {'department': department}
        return self._get(path, params=params)

    def staff(self, department):
        """Retrieve staff for a department (or departments) at MIT

        Args:
            department (str): the department number, name, or short name
        """
        path = '/departments/staff'
        params = {'department': department}
        return self._get(path, params=params)

    def faculty(self, department):
        """Retrieve faculty for a department (or departments) at MIT

        Args:
            department (str): the department number, name, or short name
        """
        path = '/departments/faculty'
        params = {'department': department}
        return self._get(path, params=params)

    def postdocs(self, department):
        """Retrieve postdocs for a department (or departments) at MIT

        Args:
            department (str): the department number, name, or short name
        """
        path = '/departments/postdocs'
        params = {'department': department}
        return self._get(path, params=params)

    def graduateStudents(self, course):
        """Retrieve graduate students for a course at MIT

        Args:
            course (str): the course number
        """
        path = '/departments/graduateStudents'
        params = {'course': course}
        return self._get(path, params=params)

    def undergraduateStudents(self, course):
        """Retrieve undergraduate students for a course at MIT

        Args:
            course (str): the course number
        """
        path = '/departments/undergraduateStudents'
        params = {'course': course}
        return self._get(path, params=params)

    def students(self, course):
        """Retrieve all students for a course at MIT

        Args:
            course (str): the course number
        """
        path = '/departments/students'
        params = {'course': course}
        return self._get(path, params=params)


if __name__ == '__main__':
    import fire
    config = get_config()
    client = Client(config['credentials']['client_id'],
                    config['credentials']['client_secret'])
    fire.Fire(client)
