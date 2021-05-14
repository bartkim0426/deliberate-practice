import os
import tempfile
from unittest import TestCase, mock
from test.support import EnvironmentVarGuard

from graphql_client import call_graphql


def get_env_data_as_dict(path: str) -> dict:
    '''
    helper function for get github token to env from .env file

    param:
        path: path of file that contains environment variables

    return:
        dict: key-value pair of environment variables in env file
    '''
    with open(path, 'r') as f:
        env = {}
        for line in f.readlines():
            if not line.startswith('#'):
                key, value = line.replace('\n', '').split('=')
                env[key] = value
        return env


class UtilsTestCase(TestCase):
    '''
    test for help function
    '''
    # def _write_env(self, path: str, env: dict):

    def setUp(self):
        # create temp env file
        _, self.env_filename = tempfile.mkstemp()

        self.test_env = {'key': 'value'}

        with open(self.env_filename, 'a') as f:
            for k, v in self.test_env.items():
                f.write(f'{k}={v}\n')

    def tearDown(self):
        # remove temp env file
        os.remove(self.env_filename)

    def test_get_env_data_as_dict(self):
        self.assertTrue(os.path.exists(self.env_filename))

        envs = get_env_data_as_dict(self.env_filename)

        self.assertEqual(envs, self.test_env)


class MockResopnse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


@mock.patch.dict(os.environ, {'GITHUB_TOKEN': ''})
class GraphQLTestCase(TestCase):
    def setUp(self):
        # read env from .env fiie
        test_env = get_env_data_as_dict('./.env')
        self.env = mock.patch.dict('os.environ', test_env)

    def test_env_set(self):
        with self.env:
            self.assertNotEqual(os.environ.get('GITHUB_TOKEN'), '')

    @mock.patch('httpx.post')
    def test_call_graphql(self, mock_http):
        '''
        # TODO: mock 안되는 부분부터 진행
        문서 한 번 읽어보고 진행
        https://docs.python.org/ko/3/library/tempfile.html
        '''
        mock_http = mock.Mock()
        mock_http.status_code = 200
        mock_http.json = mock.MagicMock(return_value="{'data': {'viewer': {'login': 'bartkim0426'}}}")
        with self.env:
            query = 'query { viewer { login }}'
            token = os.environ.get('GITHUB_TOKEN')
            result = call_graphql(query, token)

            self.assertEqual(result['data']['viewer']['login'], 'bartkim0426')

