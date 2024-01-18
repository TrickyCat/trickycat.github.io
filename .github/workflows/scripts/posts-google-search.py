from oauth2client.service_account import ServiceAccountCredentials
import httplib2
import os
import json

GOOGLE_SEARCH_INDEXING_API = {
    'SCOPES' : [ "https://www.googleapis.com/auth/indexing" ],
    'ENDPOINT': "https://indexing.googleapis.com/v3/urlNotifications:publish",
    'KEYFILE': None
}

try:
    GOOGLE_SEARCH_INDEXING_API['KEYFILE'] = json.loads(os.environ['GOOGLE_SEARCH_INDEXING_API_KEYFILE'])
    ALL_CHANGED_POST_FILES = os.environ['ALL_CHANGED_POST_FILES'].split(' ')
    BASE_URL = os.environ['BLOG_BASE_URL']

    # Drop trailing slash if any
    if BASE_URL[-1] == '/':
        BASE_URL = BASE_URL[:-1]

except:
    print(f'Some required env vars were not resolved 👿')
    exit(1)

# '_posts/2022-03-20-hello-world.md' => '2022/03/20/hello-world.html'
def postFilePathToUrlPath(s: str):
    return (s.replace('_posts/', '')
            .replace('-', '/', 3)
            .replace('.md', '.html'))

credentials = ServiceAccountCredentials.from_json_keyfile_dict(GOOGLE_SEARCH_INDEXING_API['KEYFILE'], scopes=GOOGLE_SEARCH_INDEXING_API['SCOPES'])
http = credentials.authorize(httplib2.Http())

def submitRequest(absoluteUrl: str):
    reqBody = f"""{{
  "url": "{absoluteUrl}",
  "type": "URL_UPDATED"
}}"""
    print(f'Request to be submitted:\n{reqBody}')
    respHeaders, respBody = http.request(GOOGLE_SEARCH_INDEXING_API['ENDPOINT'], method="POST", body=reqBody)
    print(f'Response headers: {respHeaders}')
    print(f'Response body: {respBody}')

for postFile in ALL_CHANGED_POST_FILES:
    if not postFile: continue

    print('\n-----------------\n')

    relativeUrl = postFilePathToUrlPath(postFile)
    absoluteUrl = f'{BASE_URL}/{relativeUrl}'
    
    print(f'Post file: {postFile}')
    print(f'Relative URL: {relativeUrl}')
    print(f'Absolute URL: {absoluteUrl}')
    
    submitRequest(absoluteUrl)

    print('\n-----------------\n')