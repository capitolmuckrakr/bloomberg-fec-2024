# fec

## About
This app allows for importing and searching expenditures, independent expenditures and contributions from electronic FEC filings. It was forked from an app developed by the New York Times. It relies on a forked version of the NYT's [fec2json](https://github.com/capitolmuckrakr/fec2json) library.

#### Why not just use the FEC website? 
The FEC website has been substantially improved recently, but it still lacks several main features we desire.
1. It takes several days for itemizations to be processed, so it is impossible to search transactions right away
1. There are some search fields that are important to me that do not exist in the FEC
1. We want to be able to do more with independent expenditure summing and categorizing
1. We want to be able to add additional data, such as our own donor ids

If you don't *really* need to deploy and maintain your own standalone campaign finance infrastructure, however, I recommend using tools developped by the FEC including their [site](https://www.fec.gov/data/?search=), their [api](https://api.open.fec.gov/developers/) or their [bulk data](https://classic.fec.gov/finance/disclosure/ftp_download.shtml). Or use ProPublica's [site](https://projects.propublica.org/itemizer/) or [api](https://www.propublica.org/datastore/api/campaign-finance-api).

### Setup instructions (updated for CNN fork)
1. pull this repo
1. `mkvirtualenv fec --python $(which python3)`
1. get a FEC API key [here](https://api.data.gov/signup/)
1. email APIinfo@fec.gov and ask them to upgrade you to 120 api calls per minute
1. add the following to your `$VIRTUAL_ENV/bin/postactivate`:
    ```bash
    export DJANGO_SETTINGS_MODULE=config.dev.settings
    export fec_DB_NAME=bloomberg_fec
    export fec_DB_USER=bloomberg_fec
    export FEC_API_KEY=your-api-key
    ```
1. `pip install -r requirements.txt`
1. `createuser -s bloomberg_fec `
1. `createdb -U bloomberg_fec bloomberg_fec`
1. `add2virtualenv . && add2virtualenv config && add2virtualenv fec`
1. `django-admin migrate`

