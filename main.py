import json
from threading import Thread
import schedule

from src import poster
from src import grabber
from src import recruiter


def post_schedule():
    with open('data.json', encoding="utf8") as file:
        data = json.load(file)
        post_time = data['post_time']

        for time in post_time:
            schedule.every().day.at(time).do(poster.upload_photo)

    while True:
        schedule.run_pending()
        time.sleep(5)


if __name__ == '__main__':
    with open('data.json', encoding="utf8") as file:
        data = json.load(file)
        grabber = grabber.Grabber(data['username'], data['sources'], 50)
        grabber.download()

        recruiter = recruiter.Recruiter(data['username'], data['password'], data['sources'])
        poster = poster.Poster(data['username'], data['password'], data['captions'], data['tags'])

    post_thread = Thread(target=post_schedule)
    post_thread.start()

    while 1:
        recruiter.follow()
        recruiter.unfollow()
