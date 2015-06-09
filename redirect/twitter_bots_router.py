__author__ = 'Josko'


class TwitterBotsRouter(object):
    """A router to control all database operations on models in
    the phasionate application"""

    def db_for_read(self, model, **hints):
        """Point all operations on wordpress models to 'wordpress'"""

        if model._meta.app_label == 'redirect':
            return 'twitter_bots_prod'
        return None

    def db_for_write(self, model, **hints):
        """Point all operations on wordpress models to 'wordpress'"""

        if model._meta.app_label == 'redirect':
            return 'twitter_bots_prod'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Allow any relation if a model in wordpress is involved"""

        if obj1._meta.app_label == 'redirect' or obj2._meta.app_label == 'redirect':
            return True
        return None

    def allow_migrate(self, db, model):
        """We don't create the wordpress tables via Django."""

        return model._meta.app_label != 'redirect'
