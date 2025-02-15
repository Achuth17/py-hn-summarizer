from hackernews import HackerNews
from hackernews import Item

from typing import List

import io


class HNClient:
    def __init__(self):
        self.hn = HackerNews()

    def get_story(self, id: int):
        return self.hn.get_item(id, expand=True)

    def get_top_story_urls(self, count: int):        
        top_stories = self.hn.top_stories(limit=count)
        urls = []
        for story in top_stories:
            if story.item_type == 'story':
                urls.append(story.url)
        return urls
    
    def get_top_story_comments(self, item: Item):
        comments = []
        for comment in item.kids:            
            if not comment.text or comment.deleted or comment.dead:
                continue
            comments.append(comment)
        return comments
    
    def serialize_comments(self, comments: List[Item]) -> str:
        buffer = io.StringIO()
        for comment in comments:
            formatted_comment = f"{comment.item_id} : {comment.text}\n"
            buffer.write(formatted_comment)
            buffer.write("\n")
        return buffer.getvalue()
    

