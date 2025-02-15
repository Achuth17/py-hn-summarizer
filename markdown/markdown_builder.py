import html2text
import requests


class MarkdownBuilder:
    def __init__(self):
        pass

    def _fetch_url_contents(self, url: str):    
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            ""

    def _convert_contents_to_markdown(self, contents: str):
        h = html2text.HTML2Text()
        h.ignore_links = True
        h.ignore_images = True
        return h.handle(contents)
    
    def parse_and_fetch_contents(self, url: str):
        html_contents = self._fetch_url_contents(url)
        markdown_contents = self._convert_contents_to_markdown(html_contents)
        return markdown_contents