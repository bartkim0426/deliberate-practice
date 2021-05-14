from http import HTTPStatus

import httpx


graphql_url = 'https://api.github.com/graphql'
query = '''
{
    viewer {
        login
    }
}
'''

def call_graphql(query: str, token: str):
    '''
    call github graphql for query

    params:
        query: valid graphql query
        token: github public access token
    '''
    res = httpx.post(
        graphql_url,
        headers={'Authorization': f'bearer {token}'},
        json={
            'query': query
        }
    )
    if res.status_code == HTTPStatus.OK:
        return res.json()
    else:
        raise Exception(f'Query failed: {res.status_code}/{res.json()}')
