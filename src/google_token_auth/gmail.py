import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

from google_token_auth.setup_logging import setup_logger

LOGGER = setup_logger('gmail_token_auth')


def get_token(creds_dir, scopes):
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    token_file_path = os.path.join(creds_dir, 'token.json')
    creds_file_path = os.path.join(creds_dir, 'credentials.json')
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(token_file_path):
        creds = Credentials.from_authorized_user_file(token_file_path, scopes)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                creds_file_path, scopes
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_file_path, 'w') as token:
            token.write(creds.to_json())
            LOGGER.info('Refreshed credentials')
            exit()
    return creds

