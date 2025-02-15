# PY HackerNews Summarizer

Hackernews post and comment thread summarizer

Usage
=====
### Install dependencies
```
pip install -r requirements.txt
```

### Export GEMINI API Key from [AIStudio](https://aistudio.google.com/)
```
export GEMINI_API_KEY=<INSERT-API-KEY>
```

### Summarize Hackernews Posts
```
python summarizer.py -s <post_id>
```

#### Sample
```
Sample: python summarizer.py -s 43018572
```