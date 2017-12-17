"""requires_auth.py"""
from functools import wraps
from flask import request, _app_ctx_stack
from jose import jwt
from endpoints.auxiliaries.errors import AuthError
from requests import get


def get_token_auth_header():
    """Extracts the access token from the Authorization header."""
    auth = request.headers.get('Authorization', None)
    if not auth:
        raise AuthError({'code': 'authorization_header_missing',
                         'description': 'Authorization header is expected.'},
                        401)

    parts = auth.split()
    if parts[0].lower() != 'bearer':
        raise AuthError({'code': 'invalid_header',
                         'description': 'Authorization header must start with Bearer.'},
                        401)
    elif len(parts) == 1:
        raise AuthError({'code': 'invalid_header',
                         'description': 'Token not found.'},
                        401)
    elif len(parts) > 2:
        raise AuthError({'code': 'invalid_header',
                         'description': 'Authorization header must be Bearer token.'},
                        401)

    token = parts[1]
    return token

def requires_auth(functor):
    """Determine if the access token is valid."""

    @wraps(functor)
    def decorated(*args, **kwargs):
        """Decorater inner method."""
        token = get_token_auth_header()
        jwks = get('https://watson-login.eu.auth0.com/.well-known/jwks.json').json()

        unverified_header = jwt.get_unverified_header(token)
        rsa_key = {}
        for key in jwks['keys']:
            if key['kid'] == unverified_header['kid']:
                rsa_key = {
                    'kty': key['kty'],
                    'kid': key['kid'],
                    'use': key['use'],
                    'n': key['n'],
                    'e': key['e']
                }

        if rsa_key:
            try:
                payload = jwt.decode(
                    token,
                    rsa_key,
                    algorithms=['RS256'],
                    audience='https://watson-service.eu-gb.mybluemix.net',
                    issuer='https://watson-login.eu.auth0.com/'
                )
            except jwt.ExpiredSignatureError:
                raise AuthError({'code': 'token_expired',
                                 'description': 'Token is expired.'},
                                401)
            except jwt.JWTClaimsError:
                raise AuthError({'code': 'invalid_claims',
                                 'description': 'Incorrect claims.'},
                                401)
            except Exception:
                raise AuthError({'code': 'invalid_header',
                                 'description': 'Unable to parse authentication token.'},
                                400)

            _app_ctx_stack.top.current_user = payload
            return functor(*args, **kwargs)
        raise AuthError({'code': 'invalid_header',
                         'description': 'Unable to find appropriate key.'},
                        400)

    return decorated
