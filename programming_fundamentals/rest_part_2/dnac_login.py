import requests
from requests.auth import HTTPBasicAuth
from dnac_config import DNAC_IP, DNAC_USERNAME, DNAC_PASSWORD, DNAC_VERSION

requests.packages.urllib3.disable_warnings()

def get_auth_token():
    """
    Building out Auth request. Using requests.post to make a call to the Auth Endpoint
    """
    # Endpoint URL
    #url = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'
    url = 'https://' + DNAC_IP + '/dna/system/api/' +  DNAC_VERSION + '/auth/token'
    #print(url)

    # Make the POST Request
    resp = requests.post(url, auth=HTTPBasicAuth(DNAC_USERNAME, DNAC_PASSWORD))
    # Retrieve the Token from the returned JSON
    token = resp.json()['Token']
    # Print out the Token
    print("Token Retrieved: {}".format(token))
    # Create a return statement to send the token back for later use
    return token


if __name__ == "__main__":
 token_retrieved = get_auth_token()
 print(f"\nThe retrieved token is {token_retrieved}\n")
