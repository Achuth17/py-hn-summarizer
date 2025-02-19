import os

import logging
import pathlib
import time

from markdown.markdown_builder import MarkdownBuilder
from hn.hn_client import HNClient
from gemini.gemini_client import GeminiClient


class HnSummarizer():    

    def __init__(self):
        self.markdownBuilder = MarkdownBuilder()
        self.hn_client = HNClient()
        self.gemini_client = GeminiClient()
        with open("prompts/prompt.txt", "r") as f:
            self.prompt_template = f.read()
    
    def _create_library_if_not_found(self, path: str):        
        pathlib.Path(path).mkdir(parents=True, exist_ok=True) 
        return

    def _find_summary_in_cache(self, story_id: int) -> bool:
        self._create_library_if_not_found("library/")
        summary_cache_template = "library/{}.md"
        summary_file = summary_cache_template.format(str(story_id))
        if os.path.exists(summary_file):
            logging.info("Summary for story {} exists in cache.".format(story_id))
            return True
        else:
            logging.info("Summary for story {} does not exist in cache.".format(story_id))
            return False
    
    def _write_to_library(self, story_id: int, summary: str) -> None:
        self._create_library_if_not_found("library/")
        summary_cache_template = "library/{}.md"
        summary_file = summary_cache_template.format(str(story_id))
        with open(summary_file,'w') as f:
            f.write(summary)
            f.close()
    
    def _read_from_library(self, story_id: int) -> str:
        summary_cache_template = "library/{}.md"
        summary_file = summary_cache_template.format(str(story_id))
        summary = ""
        with open(summary_file,'r') as f:
            summary = f.read()            
        return summary

    
    def cache_top_posts_summary(self, count: int) -> bool:
        top_story_ids = self.hn_client.get_top_story_ids(count)
        logging.info("Top stories are: {}".format(top_story_ids))
        for story_id in top_story_ids:
            logging.info("Summarizing post: {}".format(story_id))
            self.summarize_post(story_id, True)
            time.sleep(5)
        return True


    def summarize_post(self, story_id: int, skip_response: bool = False) -> str:
        if self._find_summary_in_cache(story_id):
            if skip_response:
                return ""
            else:
                self._read_from_library(story_id)
        markdownBuilder = MarkdownBuilder()
        hn_client = HNClient()
        gemini_client = GeminiClient()
        story = hn_client.get_story(story_id)
        logging.info("Fetched story: {}".format(story_id))
        markdown_contents = markdownBuilder.parse_and_fetch_contents(story.url)
        if not markdown_contents:
            return
        logging.info("Converted story contents to markdown: {}".format(story_id))
        comments = hn_client.get_top_story_comments(story)
        logging.info("Fetched comments: {}".format(story_id))
        serialized_comments = hn_client.serialize_comments(comments)
        logging.info("Serialized story comments: {}".format(story_id))
        
        prompt = self.prompt_template
        prompt = prompt.replace("ARTICLE_CONTENTS", markdown_contents)
        prompt = prompt.replace("COMMENT_CONTENTS", serialized_comments)
        logging.info("Constructed prompt for story: {}".format(story_id))

        gemini_summary = gemini_client.ask_gemini(prompt)
        logging.info("Got Gemini response for story: {}".format(story_id))
        self._write_to_library(story_id, gemini_summary)
        logging.info("Story summary written to library: {}".format(story_id))
        if skip_response:
            return ""
        else:
            return gemini_summary
        