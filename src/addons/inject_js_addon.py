import os
from bs4 import BeautifulSoup
from mitmproxy import ctx

inject_js_file = os.environ.get("THEMIS_PROXY_INJECT_JS", default="content.js")

class JSInjector:
    def __init__(self):
        # load in the javascript to inject
        with open(inject_js_file, 'r') as f:
            self.content_js = f.read()

    def response(self, flow):
        headers = dict(flow.response.headers)
        if not flow.response.status_code == 200:
            ctx.log.debug("Status code not 200. Skipping")
            return

        content_type = flow.response.headers.get("Content-Type", "")

        if not content_type.startswith("text/html"):
            ctx.log.debug("Content-Type [%s] not text/html. Skipping" % content_type)
            return

        # inject the script tag
        html = BeautifulSoup(flow.response.text, 'lxml')
        container = html.head or html.body
        if container:
            script = html.new_tag('script', type='text/javascript')
            script.string = self.content_js
            container.insert(0, script)
            flow.response.text = str(html)

            ctx.log.debug('Successfully injected javascript.')
        else:
            ctx.log.error("Unable to find HTML container. JS script will not be injected")

addons = [JSInjector()]
