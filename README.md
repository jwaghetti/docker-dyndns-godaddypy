# docker-dyndns-godaddypy

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

Copyright (C) 2017-2018 Jean Waghetti.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
