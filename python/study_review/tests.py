import os
import tempfile
from unittest import TestCase, mock

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
    # TODO: setup에서 생성된 tempfile이 unit test 실행시에는 제거되어 있음
    문서 한 번 읽어보고 진행
    https://docs.python.org/ko/3/library/tempfile.html
    '''
    # def _write_env(self, path: str, env: dict):

    def setUp(self):
        # create temp env file
        env_file = tempfile.TemporaryFile()
        self.env_filename = env_file.name

        self.test_env = {'key': 'value'}

        with open(self.env_filename, 'a') as f:
            for k, v in self.test_env.items():
                f.write(f'{k}={v}\n')

    def tearDown(self):
        # remove temp env file
        pass
        # os.remove(self.env_filename)

    def test_get_env_data_as_dict(self):
        self.assertTrue(os.path.exists(self.env_filename))

        envs = get_env_data_as_dict(self.env_filename)

        self.assertEqual(envs, self.test_env)




query = 'query { viewer { login }}'
@mock.patch.dict(os.environ, {'GITHUB_TOKEN': ''})
class GraphQLTestCase(TestCase):
    def setUp(self):
        # setup env
        pass
