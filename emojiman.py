import random

import emoji
import tweepy

import settings


def main():
    auth = tweepy.OAuthHandler(*settings.oauth)
    auth.set_access_token(*settings.access_token)
    api = tweepy.API(auth)

    me = api.me()

    name = me.name

    emojis = [v for k, v in emoji.EMOJI_UNICODE.iteritems() if not k.startswith(':flag_for_')]

    print 'Current name:', repr(name)

    for e in emojis:
        if name.endswith(e):
            name = name[:-len(e)]

    name += random.choice(emojis)

    print 'New name:', repr(name)

    api.update_profile(name=name)


if __name__ == '__main__':
    main()
