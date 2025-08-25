# coding: utf-8
import os, requests, time, datetime
from cycle_2020.utils.loader import evaluate_filing, logger

ACCEPTABLE_FORMS = ['F3','F3X','F3P','F24', 'F5']
BAD_COMMITTEES = ['C00401224','C00694323','C00630012'] #actblue; winred; it starts today
API_KEY = os.environ.get('FEC_API_KEY')

LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()
logger.setLevel(LOGLEVEL)

def get_past_filing_list(start_date, end_date, max_fails=10, waittime=10, myextra=None):
    #gets list of available filings from the FEC.
    #TODO: institute an API key pool or fallback?
    url = "https://api.open.fec.gov/v1/filings/?per_page=100&sort=receipt_date"
    url += "&api_key={}".format(API_KEY)
    url += "&min_receipt_date={}".format(start_date)
    url += "&max_receipt_date={}".format(end_date)

    filings = []
    page = 1
    fails = 0

    while True:
        #get new filing ids from FEC API
        resp = requests.get(url+"&page={}".format(page))
        page += 1
        if myextra:
            myextra=myextra.copy()
        try:
            files = resp.json()
        except:
            #failed to convert respons to JSON
            fails += 1
            if fails >= max_fails:
                if myextra:
                    myextra['TAGS']='bloomberg-fec, result:fail'
                logger.warning('Failed to download valid JSON from FEC site {} times'.format(max_fails),
                               extra=myextra)
                return resp
            time.sleep(waittime)
        try:
            results = files['results']
        except KeyError:
            fails += 1
            if fails >= max_fails:
                if myextra:
                    myextra['TAGS']='bloomberg-fec, result:fail'
                logger.warning('Failed to download valid JSON from FEC site {} times'.format(max_fails),
                               extra=myextra)
                return resp
            time.sleep(waittime)
            continue

        if len(results) == 0:
            break
        for f in results:
            if evaluate_filing(f):
                if f['file_number'] and int(f['file_number']) > 0:
                    filings.append(f['file_number'])
    return filings
    
