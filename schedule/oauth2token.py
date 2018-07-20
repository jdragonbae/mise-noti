"""
Shows basic usage of the Google Calendar API. Creates a Google Calendar API
service object and outputs a list of the next 10 events on the user's calendar.
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import datetime
import pdb
from schedule.models import Schedule
from schedule.utils import get_micro_dust

def get_token(code):
    # Setup the Calendar API
    SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
    #store = file.Storage('token.json')
    #creds = store.get()
    #if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    flow.redirect_uri = "urn:ietf:wg:oauth:2.0:oob"
    credential = flow.step2_exchange(code=code, http=None)
    #    creds = tools.run_flow(flow, store)

    service = build('calendar', 'v3', http=credential.authorize(Http()))

    now = datetime.datetime.utcnow()
    tomorrow = now + datetime.timedelta(days=1)

    events_result = service.events().list(calendarId='primary', timeMin=now.isoformat()+'Z', timeMax=tomorrow.isoformat()+'Z',
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])
        if 'location' in event:
            location = event['location'].split(',')[0].strip()
            micro_dust = get_micro_dust(location)
            pdb.set_trace()
            Schedule.objects.create(scheTitle=event['summary'],location=location, time=start, micro_dust=micro_dust)
            



