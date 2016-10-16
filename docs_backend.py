from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
class Backend:
    try:
        import argparse
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
    except ImportError:
        flags = None

    # If modifying these scopes, delete your previously saved credentials
    # at ~/.credentials/sheets.googleapis.com-python-quickstart.json
    SCOPES = 'https://www.googleapis.com/auth/drive'
    CLIENT_SECRET_FILE = 'client_sheets.json'
    APPLICATION_NAME = 'Google Sheets API Python Quickstart'

    def addToDB(self, filetype, filename, fileID, service):

        #Need to figure out a better way to pass these two params around!
        spreadsheetId = '10GBcsGi5RpmhJm323o5c9EPUj8U52voO3vFP9G01Gco'
        rangeName = 'Backend!A2:C'        
        service.spreadsheets().values().append(spreadsheetId=spreadsheetId, range='A1', insertDataOption='INSERT_ROWS',
        valueInputOption='RAW',
        body=
        {
            "values":
            [
                [ filetype, filename, fileID ]
            ]
        }).execute()

    #Given a filename and fileID, this will return.....
    #INCOMPLETE
    def readFromDB(self, filename, fileID):
        spreadsheetId = '10GBcsGi5RpmhJm323o5c9EPUj8U52voO3vFP9G01Gco'
        rangeName = 'Backend!A2:C'

        result = service.spreadsheets().values().get(
            spreadsheetId=spreadsheetId, range=rangeName).execute()

        values = result.get('values', [])
        if not values:
            print('No data found.')     
               
        else:
            for row in values:
                if()
                # Print columns A and E, which correspond to indices 0 and 4.
                print('%s, %s, %s' % (row[0], row[1], row[2]))

    def printDB(self, service):

        spreadsheetId = '10GBcsGi5RpmhJm323o5c9EPUj8U52voO3vFP9G01Gco'
        rangeName = 'Backend!A2:C'   

        result = service.spreadsheets().values().get(
            spreadsheetId=spreadsheetId, range=rangeName).execute()

        values = result.get('values', [])

        if not values:
            print('No data found.')
        else:
            print('Printing entire backend...');
            for row in values:
                # Print columns A and E, which correspond to indices 0 and 4.
                print('%s, %s, %s' % (row[0], row[1], row[2]))


    def get_credentials(self):
        """Gets valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.

        Returns:
            Credentials, the obtained credential.
        """
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                       'sheets.googleapis.com-python-quickstart.json')

        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            print("HEYYYYYY")
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            flow.user_agent = APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else: # Needed only for compatibility with Python 2.6
                credentials = tools.run(flow, store)
            print('Storing credentials to ' + credential_path)
        return credentials

    #This returns a service that can be passed to the methods up to.
    def connectToDB(self):
        """Shows basic usage of the Sheets API.

        Creates a Sheets API service object and prints the names and majors of
        students in a sample spreadsheet:
        https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
        """

        spreadsheetId = '10GBcsGi5RpmhJm323o5c9EPUj8U52voO3vFP9G01Gco'
        rangeName = 'Backend!A2:C'
        credentials = self.get_credentials()
        http = credentials.authorize(httplib2.Http())
        discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                        'version=v4')
        service = discovery.build('sheets', 'v4', http=http,
                                  discoveryServiceUrl=discoveryUrl)
        return service 
