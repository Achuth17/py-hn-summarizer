from markdown.markdown_builder import MarkdownBuilder
from hn.hn_client import HNClient
from gemini.gemini_client import GeminiClient

import argparse

def main():
    parser = argparse.ArgumentParser(description='Hackernews post and discussion summarizer')
    parser.add_argument('-s', '--story_id', type=int, required=True, help='Hackernews post id from https://news.ycombinator.com/item?id=<post_id>')
    args = parser.parse_args()


    markdownBuilder = MarkdownBuilder()
    hn_client = HNClient()
    gemini_client = GeminiClient()

    story = hn_client.get_story(args.story_id)
    comments = hn_client.get_top_story_comments(story)
    markdown_contents = markdownBuilder.parse_and_fetch_contents(story.url)   
    serialized_comments = hn_client.serialize_comments(comments)

    with open("prompts/prompt.txt", "r") as f:
        content = f.read()

    content = content.replace("ARTICLE_CONTENTS", markdown_contents)
    content = content.replace("COMMENT_CONTENTS", serialized_comments)

    gemini_summary = gemini_client.ask_gemini(content)
    print(gemini_summary)


if __name__=="__main__":
    main()