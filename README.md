# PY HackerNews Summarizer

Hackernews post and comment thread summarizer with attribution.

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
python summarizer.py -s 43018572

Post: https://techcrunch.com/2025/02/11/tumblr-to-join-the-fediverse-after-wordpress-migration-completes/ 

HN Thread: https://news.ycombinator.com/item?id=43018572

**Summary**

*   Tumblr plans to integrate with the fediverse after completing its migration to WordPress infrastructure.
*   This integration will use the ActivityPub protocol, allowing Tumblr users to federate their blogs like WordPress.com users.
*   The migration to WordPress aims to improve efficiency and enable consistent feature development across Tumblr and WordPress.
*   Tumblr confirms fediverse integration is a key reason for the WordPress migration.
*   Post-migration, Tumblr will support existing WordPress ActivityPub plugins.
*   Tumblr declined to comment on potential integration with Bluesky's AT Protocol.
*   Automattic has not provided a timeline for the migration completion.

**Discussion Summary**

*   **Skepticism about Tumblr's Future and Migration Viability** (https://news.ycombinator.com/item?id=43021099, https://news.ycombinator.com/item?id=43054470)
    *   Questions the rationale behind Automattic investing in new features like fediverse integration for Tumblr, given doubts about its profitability.
    *   Points out Tumblr's user base is considered resistant to monetization.
    *   Mentions past issues with the CEO antagonizing a significant portion of Tumblr users.
    *   Expresses skepticism about the migration to WordPress even happening, suggesting it hasn't commenced yet.

*   **Suggestions for Tumblr's Strategic Direction** (https://news.ycombinator.com/item?id=43053948)
    *   Proposes Tumblr should aim to be a user-controlled alternative to platforms like Twitter and Bluesky.
    *   Suggests providing users with their own Top-Level Domains (TLDs) for greater control.
    *   Criticizes Automattic's focus on WordPress infrastructure (WPEngine) as potentially missing a more impactful strategic opportunity for Tumblr.

*   **Doubts Regarding Efficiency and User Experience Claims** (https://news.ycombinator.com/item?id=43055857)
    *   Challenges the article's assertion that running Tumblr on WordPress will improve efficiency while maintaining the existing user experience.
    *   Notes the lack of detailed explanation supporting this claim in the article.

*   **Anticipation of Fediverse Blocklisting Issues** (https://news.ycombinator.com/item?id=43053826)
    *   Raises concerns about potential blocklisting of Tumblr by parts of the fediverse upon integration.
    *   Refers to past instances of fediverse entities blocklisting Tumblr, suggesting a recurrence of such issues is expected.
```