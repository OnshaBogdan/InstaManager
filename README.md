# InstaManager
Leave it alone! This tool can:
- grab the content from multiple sources
- post the content in a certain time
- earn followers by mass-folowwing subs of multiple accounts


## Installation:
1. `git clone https://github.com/OnshaBogdan/InstaManager.git`
2. `cd InstaManager/`
3. `virtualenv -p python3 .venv`
4. `source .venv/bin/activate`
5. `pip install -r requirements.txt`
6. Update `data.json` to fit your needs:

    - `username` - instagram username
    - `password` - instagram password
    - `sources` - list of isntagram usernames to grab content from
    - `tags` - list of tags to use in post caption
    - `captions` - list of caption options
    - `post_time` - publication time
7. `python3 main.py`
