import pickle
import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

credentials = None
__G_DRIVE_TOKEN_FILE = "token.pickle"
__OAUTH_SCOPE = ['https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/cloud-platform','https://www.googleapis.com/auth/iam','https://www.googleapis.com/auth/admin.directory.group','https://www.googleapis.com/auth/admin.directory.group.member']

if os.path.exists(__G_DRIVE_TOKEN_FILE):
    with open(__G_DRIVE_TOKEN_FILE, 'rb') as f:
        credentials = pickle.load(f)
        if credentials is None or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
else:
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', __OAUTH_SCOPE)
    credentials = flow.run_console(port=0)

# Save the credentials for the next run
with open(__G_DRIVE_TOKEN_FILE, 'wb') as token:
    pickle.dump(credentials, token)
