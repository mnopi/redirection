class TwitterBotsBaseRouter(object):
    def allow_relation(self, obj1, obj2, **hints):
        """Allow any relation if a model in twitterbots is involved"""

        if obj1._meta.app_label == 'redirect' or obj2._meta.app_label == 'redirect':
            return True
        return None

    def allow_migrate(self, db, model):
        """We don't create the twitterbot tables via Django."""

        return model._meta.app_label != 'redirect'


class TwitterBotsJoskoRouter(TwitterBotsBaseRouter):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'redirect':
            return 'twitter_bots_josko'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'redirect':
            return 'twitter_bots_josko'
        return None


class TwitterBotsYerayRouter(TwitterBotsBaseRouter):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'redirect':
            return 'twitter_bots_yeray'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'redirect':
            return 'twitter_bots_yeray'
        return None


class TwitterBotsRamonRouter(TwitterBotsBaseRouter):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'redirect':
            return 'twitter_bots_ramon'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'redirect':
            return 'twitter_bots_ramon'
        return None