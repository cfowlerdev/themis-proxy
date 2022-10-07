# Themis Proxy Service

Proxy service for Themis Scraper tasks.

## Setting up Development
~~~sh
$ pyenv install 3.9.4
$ virtualenv -p ~/.pyenv/versions/3.9.4/bin/python3.9 venv
$ source venv/bin/activate
$ python -m pip install --upgrade pip
$ export THEMIS_PROXY_INJECT_JS=/Users/cfowler/Projects/Development/Themis/src/themis-proxy-service/src/addons/content.js
# Run
$ mitmdump -p 7999 -s ./src/addons/inject_js_addon.py 
~~~


## TODO
- Logging
