# dyndns-godaddypy

Docker container to update the DNS subdomainsrecords for a GoDaddy domain to point to a dynamic IP address.

This container uses GoDaddyPy Python library. Check @ https://github.com/eXamadeus/godaddypy 

## How to Use:

- Update the *docker-compose.yml* file with the following info:
  - **DGDP_DOMAIN**: your domain
  - **DGDP_APIKEY**: API key from GoDaddy (see below)
  - **DGDP_APISECRET**: API secret from GoDaddy (see below)
  - **DGDP_SLEEPTIME**: sleep time before trying to update the IP address again (in seconds).
  - **DGDP_SUBDOMAINS**: comma separated subdomains.

The other environment variables were not tested. 

## How to Request API Key and Secret

Go to https://developer.godaddy.com/keys/ and request a production API key and secret. If the generated pair does not work, delete and request a new one.

## Running Outside a Container.

You need to have *Pyhton* and *pip* installed.

- Go to *script* folder.
- **$ pip install -r requirements.txt**
- **$ python app.py**

## Considerations

The record is updated immediately on GoDaddy domain configuration, but it takes some time to propagate the DNS records.

The script only updates records already existent. Check GoDaddyPy lib to adapt the script to your needs (including creating new records on the code).
