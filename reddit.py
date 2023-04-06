import praw
import requests
from io import BytesIO
import pywhatkit

from typing import cast

from praw.models.reddit.comment import Comment
from praw.models.reddit.redditor import Redditor
from praw.models import Submission

REDDIT_TOKEN="<your-api-token>"
REDDIT_ID="<your-id>"

subredit_name = "ProgrammerHumor"

# get top posts from subreddit
reddit = praw.Reddit(client_id=REDDIT_ID, client_secret=REDDIT_TOKEN, user_agent="abcd")
subreddit = reddit.subreddit(subredit_name)

print("Top submissions:")
for s in subreddit.top(limit=5):
    submission = cast(Submission, s)

    # get submission content
    text_content = submission.selftext

    # image conent 
    if submission.url.endswith(('png', 'jpg', 'jpeg', 'gif')):
        image_url = submission.url

        # Request the image and convert the response to an image file
        response = requests.get(image_url)
        image_file = BytesIO(response.content)

        # save to temp
        with open("temp.png", "wb") as f:
            f.write(image_file.getbuffer())

        # export to ascii
        pywhatkit.image_to_ascii_art("temp.png", "temp")

        pywhatkit.image_to

        # read ascii
        with open("temp.txt", "r") as f:
            ascii_content = f.read()
        
        print(f"image:\n{ascii_content}")


    print("\n\n----------------------------------")
    print("----------------------------------")
    print("----------------------------------")
    print("Title: ", submission.title)
    print("content:\n", text_content)



    comments = submission.comments.list()
    # sort by upvotes

    # get top 5 comments from posts
    print("---------- Comments ----------")

    for c in comments[:5]:
        comment = cast(Comment, c)

        author = cast(Redditor, comment.author)

        if author is None:
            print(f"Author is None")
        else:
            print(f"Author: {author.name}")

        print(f"content:\n{comment.body}")
        print("\n\n")

        """
        ``author``        Provides an instance of :class:`.Redditor`.
        ``body``          The body of the comment, as Markdown.
        ``body_html``     The body of the comment, as HTML.
        ``created_utc``   Time the comment was created, represented in `Unix Time`_.
        ``distinguished`` Whether or not the comment is distinguished.
        ``edited``        Whether or not the comment has been edited.
        ``id``            The ID of the comment.
        ``is_submitter``  Whether or not the comment author is also the author of the
                          submission.
        ``link_id``       The submission ID that the comment belongs to.
        ``parent_id``     The ID of the parent comment (prefixed with ``t1_``). If it is a
                          top-level comment, this returns the submission ID instead
                          (prefixed with ``t3_``).
        ``permalink``     A permalink for the comment. :class:`.Comment` objects from the
                          inbox have a ``context`` attribute instead.
        ``replies``       Provides an instance of :class:`.CommentForest`.
        ``saved``         Whether or not the comment is saved.
        ``score``         The number of upvotes for the comment.
        ``stickied``      Whether or not the comment is stickied.
        ``submission``    Provides an instance of :class:`.Submission`. The submission that
                          the comment belongs to.
        ``subreddit``     Provides an instance of :class:`.Subreddit`. The subreddit that
                          the comment belongs to.
        ``subreddit_id``  The subreddit ID that the comment belongs to.
        """

