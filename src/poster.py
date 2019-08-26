from os import listdir
from os import remove
from random import randrange
from random import choice
from random import choices

from InstagramAPI import InstagramAPI


class Poster:

    def __init__(self, username, password, captions, tags):
        self.username = username
        self.password = password
        self.captions = captions
        self.tags = tags

    def get_next(self):
        path = f"Media/{self.username}"
        files_list = listdir(path)

        index = randrange(0, len(files_list), 1)
        photo_path = f'Media/{self.username}/{files_list[index]}'
        return photo_path

    def upload_photo(self):
        photo_path = self.get_next()
        api = InstagramAPI(self.username, self.password)
        api.login()
        caption = self.get_caption()
        api.uploadPhoto(photo_path, caption=caption)
        self.delete_file(photo_path)

    def get_caption(self):
        tags = ' '.join(self.get_tags())
        return choice(self.captions) + tags

    def get_tags(self, amount=10):
        return choices(self.tags, k=amount)

    def delete_file(self, path):
        remove(path)
