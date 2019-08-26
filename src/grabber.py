from itertools import islice
from math import ceil

from instaloader import Instaloader, Profile


class Grabber:
    def __init__(self, username, sources, percentage=50):
        self.username = username
        self.sources = sources
        self.percentage = percentage

    def configure(self, loader):
        loader.save_metadata = False
        loader.download_videos = False
        loader.download_geotags = False
        loader.download_comments = False
        loader.download_profilepic = False
        loader.download_video_thumbnails = False
        loader.post_metadata_txt_pattern = ""

    def download(self):
        for profile in self.sources:
            loader = Instaloader()
            loader.dirname_pattern = f"../Media/{self.username}/"
            self.configure(loader)

            profile = Profile.from_username(loader.context, profile)
            posts_sorted_by_likes = sorted(profile.get_posts(), key=lambda p: p.likes)

            for post in islice(posts_sorted_by_likes, ceil(profile.mediacount * self.percentage / 100)):
                loader.download_post(post, profile)
