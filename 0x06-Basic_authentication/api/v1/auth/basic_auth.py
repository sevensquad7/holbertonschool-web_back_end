#!/usr/bin/env python3
"""
Basic API authentication module
"""

from base64 import b64decode
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    Basic Authentication
    """
    def extract_base64_authorization_header(self, authorization_header: str)\
            -> str:
        """
        Returns Base64 part of Authorization header
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if "Basic " not in authorization_header:
            return None
        return authorization_header.split("Basic ", 1)[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Returns decoded value of Base64 str
        """

        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            return b64decode(base64_authorization_header).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Returns user email and pswd from decoded Base64
        """
        if (decoded_base64_authorization_header and
                isinstance(decoded_base64_authorization_header, str) and
                ":" in decoded_base64_authorization_header):
            res = decoded_base64_authorization_header.split(":", 1)
            return (res[0], res[1])
        return (None, None)
