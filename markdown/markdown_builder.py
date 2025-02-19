import html2text
import logging
import re
import requests

FORBIDDEN_URLS = [re.compile("^.*.pdf$"), re.compile("^.*github.com.*$")]

class MarkdownBuilder:

    def __init__(self):
        pass

    def _fetch_url_contents(self, url: str) -> str:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            ""

    def _convert_contents_to_markdown(self, contents: str) -> str:
        h = html2text.HTML2Text()
        h.ignore_links = True
        h.ignore_images = True
        return h.handle(contents)
    
    def parse_and_fetch_contents(self, url: str) -> str:
        if any(regex.match(url) for regex in FORBIDDEN_URLS):
            logging.info("Forbidden url found: {}".format(url))
            return
        html_contents = self._fetch_url_contents(url)
        if not html_contents:
            return ""
        markdown_contents = self._convert_contents_to_markdown(html_contents)
        return markdown_contents