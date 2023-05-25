import requests
import json
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64


class MpesaC2bCredential:
    consumer_key = 'revnHXMvZ5M8ozXvfafWZS7RUvUV5RPS'
    consumer_secret = 'Wzo8PzAFlQbwLGnp'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'


class MpesaAccessToken:
    r = requests.get(MpesaC2bCredential.api_URL,
                     auth=HTTPBasicAuth(MpesaC2bCredential.consumer_key, MpesaC2bCredential.consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']


class LipanaMpesaPpassword:
    lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
    Business_short_code = "1600996"
    passkey = 'T97YItM0x3GZjYpmCNq8t5LzEV3I04Z9/fUVtP2n2fOqacUpLR6DF+Olkc42Ott0JzVt8Lj0Ba+BnGI5SPH0/sTKZBMYcXgj2FRKOBGKRHt+MZ8O6gd62GlVg6CTnXKWNtXpE7PZU3LCCrngbRTS5zpDz17cWRw0VRqrlagS3boU08c98NGmnTZq8XdE+ktkVm1zPjAl++NDCYXXU/dy5qgD9IeDeE7OHWLRb/9u3cGhbnWFMsAMw3WPagBnp9Slkkrcn9LC3ckoMcbVUc/tpeml4hGGLsWWLNxFH7Gz8hP9fV4iYJrXRjhDvG9NgIq6lOVoSH3fz1wP52ba65lxEw=='

    data_to_encode = Business_short_code + passkey + lipa_time

    online_password = base64.b64encode(data_to_encode.encode())
    decode_password = online_password.decode('utf-8')