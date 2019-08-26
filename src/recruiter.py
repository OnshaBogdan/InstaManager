from random import randrange

from instapy import InstaPy
from instapy import smart_run


class Recruiter:
    posts_in_step = 10  # follow/unfollow by iteration (+- 20%)
    sleep_step = 600  # seconds
    follows_by_post = 20

    def __init__(self, username, password, sources):
        self.username = username
        self.password = password
        self.sources = sources

    def follow(self):
        session = InstaPy(username=self.username,
                          password=self.password,
                          headless_browser=True)
        with smart_run(session):
            session.set_user_interact(amount=1,
                                      percentage=60,
                                      randomize=True,
                                      media='Photo')

            posts_amount = self.int_to_range(self.posts_in_step)
            sleep_delay = self.int_to_range(self.sleep_step)

            session.follow_likers(self.sources, photos_grab_amount=posts_amount,
                                  follow_likers_per_photo=self.follows_by_post,
                                  randomize=True,
                                  sleep_delay=sleep_delay,
                                  interact=True, )

    def unfollow(self):
        session = InstaPy(username=self.username,
                          password=self.password,
                          headless_browser=True)
        session.set_skip_users(skip_private=True,
                               skip_no_profile_pic=True,
                               skip_business=True,
                               business_percentage=100)

        with smart_run(session):
            users_amount = self.int_to_range(self.posts_in_step)
            sleep_delay = self.int_to_range(self.sleep_step)
            session.unfollow_users(amount=users_amount, nonFollowers=True, style="RANDOM", unfollow_after=42 * 60 * 60,
                                   sleep_delay=sleep_delay)

    def int_to_range(self, num):  # +-20%
        range_from = int(num - num / 5)
        range_to = int(num + num / 5)

        return randrange(range_from, range_to, 1)
