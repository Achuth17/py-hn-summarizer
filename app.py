from flask import Flask, request
from summarizer import HnSummarizer
import asyncio

app = Flask(__name__)

@app.route("/summarize", methods=['GET'])
def summarize():    
    post_id = int(request.args.get('post_id'))
    hn_summarizer = HnSummarizer()
    summary = hn_summarizer.summarize_post(post_id)
    return summary

if __name__ == '__main__':
    app.run(debug=True)