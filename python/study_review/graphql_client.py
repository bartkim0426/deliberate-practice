import httpx


'''
curl -H "Authorization: bearer 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" -X POST -d " \
 { \
   \"query\": \"query { viewer { login }}\" \
 } \
" https://api.github.com/graphql
'''


graphql_url = 'https://api.github.com/graphql'

def call_graphql(query: str):
    res = httpx.post(
        graphql_url,
        headers={'Authorization': 'bearer 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'},
        data={
            'query': 'query { viewer { login }}'
        }
    )
    return res
