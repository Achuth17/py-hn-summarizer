import argparse
import logging
import sys


from summarizer import HnSummarizer

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser(description='Hackernews post and discussion summarizer')
    parser.add_argument('-s', '--story_id', type=int,  help='Hackernews post id from https://news.ycombinator.com/item?id=<post_id>')
    parser.add_argument('-t', '--top_posts', type=int, help='Number of top posts to summarize. Output will be written to library folder.')
    args = parser.parse_args()

    if not args.story_id and not args.top_posts:
        logging.error("--story-id or --top-posts required.")
        sys.exit(1)

    hn_summarizer = HnSummarizer()

    if args.top_posts:
        hn_summarizer.cache_top_posts_summary(args.top_posts)
    else:
        summary = hn_summarizer.summarize_post(args.story_id)
        logging.info(summary)