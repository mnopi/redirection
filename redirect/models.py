# from django.db import models
#
# # Create your models here.
# class Page(models.Model):
#     uri = models.CharField(max_length=255, null=False, blank=False, default='none', db_index=True)
#
#     # twitter card
#     PHOTO = 1
#     SUMMARY_LARGE_IMAGE = 2
#     SUMMARY = 3
#     APP = 4
#     CARD_TYPES = (
#         (PHOTO, 'photo'),
#         (SUMMARY_LARGE_IMAGE, 'summary_large_image'),
#         (SUMMARY, 'summary'),
#         (APP, 'app'),
#     )
#     card_type = models.PositiveIntegerField(null=True, blank=True, choices=CARD_TYPES, default=None)
#     card_img_file = models.ImageField(upload_to='pages_imgs', blank=True, null=True)
#     card_img_url = models.URLField(max_length=200, blank=True, null=True)
#     card_title = models.CharField(max_length=140, blank=True, null=True)
#     card_description = models.TextField(max_length=500, blank=True, null=True)
#
#     def __unicode__(self):
#         return self.uri
#
#
# class PageAlias(models.Model):
#     uri = models.CharField(max_length=255, null=False, blank=False, default='none', db_index=True)
#     page = models.ForeignKey(Page, related_name='aliases')
#
#     class Meta:
#         verbose_name_plural = 'pages aliases'
#
#     def __unicode__(self):
#         return '%s -> %s' % (self.uri, self.page.uri)
#
#
# class Redirection(models.Model):
#     page = models.ForeignKey(Page, related_name='redirections')
#     url = models.URLField(max_length=200, null=True, blank=True)
#
#     ANDROID = 1
#     IOS = 2
#     OTHERS = 3
#     PLATFORMS = (
#         (ANDROID, 'android'),
#         (IOS, 'ios'),
#         (OTHERS, 'others'),
#     )
#     platform = models.PositiveIntegerField(null=True, blank=True, choices=PLATFORMS)
#     language = models.CharField(max_length=2, null=True, blank=True)
#
#     def __unicode__(self):
#         platform_str = ' @%s' % self.get_platform_str()
#         return '%s%s -> %s' % (self.page, platform_str, self.url)
#
#     def get_platform_str(self):
#         return self.get_platform_display() if self.platform else 'all'
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=80)
    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        managed = False
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'auth_permission'

class CoreProxy(models.Model):
    id = models.IntegerField(primary_key=True)
    proxy = models.CharField(max_length=21)
    proxy_provider = models.CharField(max_length=50)
    is_unavailable_for_registration = models.IntegerField()
    date_unavailable_for_registration = models.DateTimeField(blank=True, null=True)
    is_unavailable_for_use = models.IntegerField()
    date_unavailable_for_use = models.DateTimeField(blank=True, null=True)
    is_phone_required = models.IntegerField()
    date_phone_required = models.DateTimeField(blank=True, null=True)
    date_added = models.DateTimeField()
    is_in_proxies_txts = models.IntegerField()
    date_not_in_proxies_txts = models.DateTimeField(blank=True, null=True)
    proxies_group = models.ForeignKey('ProjectProxiesgroup', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'core_proxy'

class CoreTwitterbot(models.Model):
    id = models.IntegerField(primary_key=True)
    real_name = models.CharField(max_length=50)
    email = models.CharField(max_length=256)
    username = models.CharField(max_length=50)
    date = models.DateTimeField()
    password_twitter = models.CharField(max_length=20)
    is_manually_registered = models.IntegerField()
    password_email = models.CharField(max_length=20)
    user_agent = models.TextField()
    birth_date = models.DateField(blank=True, null=True)
    gender = models.IntegerField()
    date_suspended_email = models.DateTimeField(blank=True, null=True)
    date_suspended_twitter = models.DateTimeField(blank=True, null=True)
    email_registered_ok = models.IntegerField()
    twitter_registered_ok = models.IntegerField()
    twitter_confirmed_email_ok = models.IntegerField()
    twitter_avatar_completed = models.IntegerField()
    twitter_bio_completed = models.IntegerField()
    is_suspended = models.IntegerField()
    is_suspended_email = models.IntegerField()
    is_being_created = models.IntegerField()
    is_dead = models.IntegerField()
    proxy_for_registration = models.ForeignKey(CoreProxy, related_name='twitter_bots_registered', blank=True, null=True)
    date_death = models.DateTimeField(blank=True, null=True)
    proxy_for_usage = models.ForeignKey(CoreProxy, related_name='twitter_bots_using', blank=True, null=True)
    num_suspensions_lifted = models.IntegerField()
    is_phone_verified = models.IntegerField()
    phone_number = models.CharField(max_length=50, blank=True)
    is_being_used = models.IntegerField()
    is_detected_as_automated = models.IntegerField()
    date_detected_as_automated = models.DateTimeField(blank=True, null=True)
    # twitter_access_token = models.CharField(max_length=100, blank=True)
    # twitter_access_token_secret = models.CharField(max_length=100, blank=True)
    date_registered_twitter = models.DateTimeField(blank=True, null=True)
    # consumer_key = models.CharField(max_length=100, blank=True)
    # consumer_secret = models.CharField(max_length=100, blank=True)
    next_ptweet_date = models.DateTimeField(blank=True, null=True)
    next_imgtweet_date = models.DateTimeField(blank=True, null=True)
    next_ftweet_date = models.DateTimeField(blank=True, null=True)
    next_mutweet_date = models.DateTimeField(blank=True, null=True)
    last_control_date = models.DateTimeField(blank=True, null=True)
    break_start = models.DateTimeField(blank=True, null=True)
    break_end = models.DateTimeField(blank=True, null=True)
    max_ptweets_per_day = models.IntegerField(blank=True, null=True)
    max_imgtweets_per_day = models.IntegerField(blank=True, null=True)
    max_ftweets_per_day = models.IntegerField(blank=True, null=True)
    max_mutweets_per_day = models.IntegerField(blank=True, null=True)
    next_followback_date = models.DateTimeField(blank=True, null=True)
    max_followbacks_per_day = models.IntegerField(blank=True, null=True)
    next_unfollow_date = models.DateTimeField(blank=True, null=True)
    max_unfollows_per_day = models.IntegerField(blank=True, null=True)
    next_retweet_date = models.DateTimeField(blank=True, null=True)
    max_retweets_per_day = models.IntegerField(blank=True, null=True)
    next_fav_date = models.DateTimeField(blank=True, null=True)
    max_favs_per_day = models.IntegerField(blank=True, null=True)
    day_start = models.DateTimeField(blank=True, null=True)
    next_follow_date = models.DateTimeField(blank=True, null=True)
    max_follows_per_day = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'core_twitterbot'

class CoreUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'core_user'

class CoreUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(CoreUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        managed = False
        db_table = 'core_user_groups'

class CoreUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(CoreUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        managed = False
        db_table = 'core_user_user_permissions'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user_id = models.IntegerField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    class Meta:
        managed = False
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'django_session'

class ProjectActiononotherstweet(models.Model):
    id = models.IntegerField(primary_key=True)
    bot = models.ForeignKey(CoreTwitterbot)
    action_performed = models.IntegerField()
    action_performed_ok = models.IntegerField()
    date_assigned = models.DateTimeField()
    date_performed = models.DateTimeField(blank=True, null=True)
    tweet_id = models.BigIntegerField(blank=True, null=True)
    twitteruser_id = models.BigIntegerField()
    twitteruser_name = models.CharField(max_length=50)
    action = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'project_actiononotherstweet'

class ProjectActionontwitteruser(models.Model):
    id = models.IntegerField(primary_key=True)
    bot = models.ForeignKey(CoreTwitterbot)
    action_performed = models.IntegerField()
    action_performed_ok = models.IntegerField()
    date_assigned = models.DateTimeField()
    date_performed = models.DateTimeField(blank=True, null=True)
    twitteruser_id = models.BigIntegerField()
    twitteruser_name = models.CharField(max_length=50)
    action = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'project_actionontwitteruser'

class ProjectBotpromomsgassigned(models.Model):
    id = models.IntegerField(primary_key=True)
    bot = models.ForeignKey(CoreTwitterbot)
    promo_msg = models.ForeignKey('ProjectPromomsg')
    class Meta:
        managed = False
        db_table = 'project_botpromomsgassigned'

class ProjectClickedmutweet(models.Model):
    id = models.IntegerField(primary_key=True)
    bot_sender = models.ForeignKey(CoreTwitterbot)
    mentioned_user = models.ForeignKey('ProjectTwitteruser')
    promo_msg = models.ForeignKey('ProjectPromomsg')
    msg_sent = models.CharField(max_length=140, blank=True)
    domain = models.ForeignKey('ProjectDomain')
    class Meta:
        managed = False
        db_table = 'project_clickedmutweet'

class ProjectDomain(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=200)
    project = models.ForeignKey('ProjectProject', blank=True, null=True)
    date_added = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'project_domain'

class ProjectExtractor(models.Model):
    id = models.IntegerField(primary_key=True)
    consumer_key = models.CharField(max_length=200)
    consumer_secret = models.CharField(max_length=200)
    access_token = models.CharField(max_length=200)
    access_token_secret = models.CharField(max_length=200)
    date_created = models.DateTimeField()
    twitter_bot = models.ForeignKey(CoreTwitterbot, unique=True)
    last_request_date = models.DateTimeField(blank=True, null=True)
    is_rate_limited = models.IntegerField()
    minutes_window = models.IntegerField(blank=True, null=True)
    mode = models.IntegerField()
    is_suspended = models.IntegerField()
    date_suspended = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'project_extractor'

class ProjectFeed(models.Model):
    id = models.IntegerField(primary_key=True)
    url = models.CharField(unique=True, max_length=200)
    name = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'project_feed'

class ProjectFeeditem(models.Model):
    id = models.IntegerField(primary_key=True)
    feed = models.ForeignKey(ProjectFeed)
    text = models.CharField(max_length=101)
    link = models.CharField(max_length=200, blank=True)
    date_saved = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'project_feeditem'

class ProjectFeedsgroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'project_feedsgroup'

class ProjectFeedsgroupFeeds(models.Model):
    id = models.IntegerField(primary_key=True)
    feedsgroup = models.ForeignKey(ProjectFeedsgroup)
    feed = models.ForeignKey(ProjectFeed)
    class Meta:
        managed = False
        db_table = 'project_feedsgroup_feeds'

class ProjectFeedsgroupProxiesGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    feedsgroup = models.ForeignKey(ProjectFeedsgroup)
    proxiesgroup = models.ForeignKey('ProjectProxiesgroup')
    class Meta:
        managed = False
        db_table = 'project_feedsgroup_proxies_groups'

class ProjectFollower(models.Model):
    id = models.IntegerField(primary_key=True)
    target_user = models.ForeignKey('ProjectTargetuser')
    twitter_user = models.ForeignKey('ProjectTwitteruser')
    date_saved = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'project_follower'

class ProjectFtweet(models.Model):
    id = models.IntegerField(primary_key=True)
    date_created = models.DateTimeField()
    date_sent = models.DateTimeField(blank=True, null=True)
    sent_ok = models.IntegerField()
    bot_sender = models.ForeignKey(CoreTwitterbot, blank=True, null=True)
    feed_item = models.ForeignKey(ProjectFeeditem, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'project_ftweet'

class ProjectHashtag(models.Model):
    id = models.IntegerField(primary_key=True)
    q = models.CharField(max_length=140)
    geocode = models.CharField(max_length=50, blank=True)
    lang = models.CharField(max_length=2, blank=True)
    result_type = models.IntegerField()
    max_id = models.BigIntegerField(blank=True, null=True)
    is_active = models.IntegerField()
    date_last_extraction = models.DateTimeField(blank=True, null=True)
    max_consecutive_pages_retrieved = models.IntegerField()
    current_round_user_count = models.IntegerField(blank=True, null=True)
    current_round_oldest_tweet_limit = models.DateTimeField(blank=True, null=True)
    next_round_oldest_tweet_limit = models.DateTimeField(blank=True, null=True)
    last_round_end_date = models.DateTimeField(blank=True, null=True)
    has_to_wait_timewindow_because_of_not_enough_new_twitterusers = models.IntegerField()
    num_consecutive_pages_without_enough_new_twitterusers = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'project_hashtag'

class ProjectHashtaggroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=140)
    class Meta:
        managed = False
        db_table = 'project_hashtaggroup'

class ProjectHashtaggroupHashtags(models.Model):
    id = models.IntegerField(primary_key=True)
    hashtaggroup = models.ForeignKey(ProjectHashtaggroup)
    hashtag = models.ForeignKey(ProjectHashtag)
    class Meta:
        managed = False
        db_table = 'project_hashtaggroup_hashtags'

class ProjectHashtaggroupProjects(models.Model):
    id = models.IntegerField(primary_key=True)
    hashtaggroup = models.ForeignKey(ProjectHashtaggroup)
    project = models.ForeignKey('ProjectProject')
    class Meta:
        managed = False
        db_table = 'project_hashtaggroup_projects'

class ProjectImgtweet(models.Model):
    id = models.IntegerField(primary_key=True)
    date_created = models.DateTimeField()
    date_sent = models.DateTimeField(blank=True, null=True)
    sent_ok = models.IntegerField()
    bot_sender = models.ForeignKey(CoreTwitterbot, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'project_imgtweet'

class ProjectMentionedtwitteruser(models.Model):
    id = models.IntegerField(primary_key=True)
    twitteruser_id = models.BigIntegerField()
    username = models.CharField(max_length=15)
    lang = models.CharField(max_length=2)
    date_mentioned = models.DateTimeField()
    project = models.ForeignKey('ProjectProject', blank=True, null=True)
    bot_used = models.ForeignKey(CoreTwitterbot, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'project_mentionedtwitteruser'

class ProjectMutweet(models.Model):
    id = models.IntegerField(primary_key=True)
    date_created = models.DateTimeField()
    date_sent = models.DateTimeField(blank=True, null=True)
    sent_ok = models.IntegerField()
    bot_sender = models.ForeignKey(CoreTwitterbot, blank=True, null=True)
    mentioned_twitteruser = models.ForeignKey('ProjectTwitteruser')
    promo_msg = models.ForeignKey('ProjectPromomsg')
    msg_sent = models.CharField(max_length=140, blank=True)
    domain = models.ForeignKey(ProjectDomain, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'project_mutweet'

class ProjectMutweetclick(models.Model):
    id = models.IntegerField(primary_key=True)
    clicked_mutweet = models.ForeignKey(ProjectClickedmutweet, related_name='clicks')
    date_clicked = models.DateTimeField()
    ip = models.CharField(max_length=20, null=False, blank=False)
    referer = models.CharField(max_length=256, null=False, blank=False, default='nuse')
    ANDROID = 0
    IOS = 1
    OTHERS = 2
    platform = models.IntegerField()
    raw_useragent = models.CharField(max_length=500)
    class Meta:
        managed = False
        db_table = 'project_mutweetclick'

class ProjectProject(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    has_tracked_clicks = models.IntegerField()
    is_running = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'project_project'

class ProjectProjectHashtags(models.Model):
    id = models.IntegerField(primary_key=True)
    project = models.ForeignKey(ProjectProject)
    hashtag = models.ForeignKey(ProjectHashtag)
    class Meta:
        managed = False
        db_table = 'project_project_hashtags'

class ProjectProjectTargetUsers(models.Model):
    id = models.IntegerField(primary_key=True)
    project = models.ForeignKey(ProjectProject)
    targetuser = models.ForeignKey('ProjectTargetuser')
    class Meta:
        managed = False
        db_table = 'project_project_target_users'

class ProjectPromo(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=140, blank=True)
    msg_generator_expression = models.CharField(max_length=500)
    link_all = models.CharField(max_length=300, blank=True)
    link_android = models.CharField(max_length=300, blank=True)
    link_ios = models.CharField(max_length=300, blank=True)
    link_others = models.CharField(max_length=300, blank=True)
    project = models.ForeignKey(ProjectProject)
    active = models.IntegerField()
    language = models.CharField(max_length=2)
    class Meta:
        managed = False
        db_table = 'project_promo'

class ProjectPromomsg(models.Model):
    id = models.IntegerField(primary_key=True)
    msg = models.CharField(max_length=140)
    promo = models.ForeignKey(ProjectPromo)
    class Meta:
        managed = False
        db_table = 'project_promomsg'

class ProjectProxiesgroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    max_tw_bots_per_proxy_for_registration = models.IntegerField()
    max_tw_bots_per_proxy_for_usage = models.IntegerField()
    min_days_between_registrations_per_proxy = models.IntegerField()
    webdriver = models.CharField(max_length=2)
    is_bot_creation_enabled = models.IntegerField()
    is_bot_usage_enabled = models.IntegerField()
    reuse_proxies_with_suspended_bots = models.IntegerField()
    min_days_between_registrations_per_proxy_under_same_subnet = models.IntegerField()
    mention_fail_time_window = models.CharField(max_length=10)
    destination_bot_checking_time_window = models.CharField(max_length=10)
    mctweet_to_same_bot_time_window = models.CharField(max_length=10)
    avatar_required_to_send_tweets = models.IntegerField()
    bio_required_to_send_tweets = models.IntegerField()
    make_delays = models.IntegerField()
    use_api = models.IntegerField()
    shorten_links = models.IntegerField()
    link_on_bio = models.IntegerField()
    prepend_full_name = models.IntegerField()
    take_breaks = models.IntegerField()
    send_mctweets = models.IntegerField()
    num_consecutive_tumentions_for_check_mentioning_works = models.IntegerField()
    max_updates_per_hour = models.CharField(max_length=10)
    do_favs = models.IntegerField()
    minutes_between_favs = models.CharField(max_length=10)
    do_retweets = models.IntegerField()
    minutes_between_retweets = models.CharField(max_length=10)
    max_bots_per_twitter_app = models.IntegerField()
    do_follows = models.IntegerField()
    max_follows_per_day = models.CharField(max_length=10)
    max_unfollows_per_day = models.CharField(max_length=10)
    break_start_hour = models.CharField(max_length=10)
    break_duration_hours = models.CharField(max_length=10)
    rotate_api_keys = models.IntegerField()
    max_hours_using_same_api_key = models.CharField(max_length=10, blank=True)
    minutes_between_follows = models.CharField(max_length=10)
    minutes_between_followbacks = models.CharField(max_length=10)
    minutes_between_unfollows = models.CharField(max_length=10)
    max_followbacks_per_day = models.CharField(max_length=10)
    send_mutweets = models.IntegerField()
    minutes_between_mutweets = models.CharField(max_length=10)
    max_mutweets_per_day = models.CharField(max_length=10)
    interleave_symbols_on_mutweet_msg = models.IntegerField()
    send_ptweets = models.IntegerField()
    minutes_between_ptweets = models.CharField(max_length=10)
    max_ptweets_per_day = models.CharField(max_length=10)
    send_ftweets = models.IntegerField()
    minutes_between_ftweets = models.CharField(max_length=10)
    max_ftweets_per_day = models.CharField(max_length=10)
    send_imgtweets = models.IntegerField()
    minutes_between_imgtweets = models.CharField(max_length=10)
    max_imgtweets_per_day = models.CharField(max_length=10)
    max_favs_per_day = models.CharField(max_length=10)
    max_retweets_per_day = models.CharField(max_length=10)
    max_total_followings = models.CharField(max_length=10)
    interleave_mistakes_on_mutweet_msg = models.IntegerField()
    interleave_symbols_every_words_num = models.CharField(max_length=10)
    interleave_mistakes_count = models.CharField(max_length=10)
    max_bots_per_api_key = models.CharField(max_length=10)
    class Meta:
        managed = False
        db_table = 'project_proxiesgroup'

class ProjectProxiesgroupProjects(models.Model):
    id = models.IntegerField(primary_key=True)
    proxiesgroup = models.ForeignKey(ProjectProxiesgroup)
    project = models.ForeignKey(ProjectProject)
    class Meta:
        managed = False
        db_table = 'project_proxiesgroup_projects'

class ProjectPtweet(models.Model):
    id = models.IntegerField(primary_key=True)
    date_created = models.DateTimeField()
    date_sent = models.DateTimeField(blank=True, null=True)
    sent_ok = models.IntegerField()
    bot_sender = models.ForeignKey(CoreTwitterbot, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'project_ptweet'

class ProjectTargetuser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=80)
    next_cursor = models.BigIntegerField(blank=True, null=True)
    followers_count = models.IntegerField(blank=True, null=True)
    extractor_used = models.ForeignKey(ProjectExtractor, blank=True, null=True)
    is_active = models.IntegerField()
    date_extraction_end = models.DateTimeField(blank=True, null=True)
    date_last_extraction = models.DateTimeField(blank=True, null=True)
    is_suspended = models.IntegerField()
    num_consecutive_pages_without_enough_new_twitterusers = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'project_targetuser'

class ProjectTugroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=140)
    class Meta:
        managed = False
        db_table = 'project_tugroup'

class ProjectTugroupProjects(models.Model):
    id = models.IntegerField(primary_key=True)
    tugroup = models.ForeignKey(ProjectTugroup)
    project = models.ForeignKey(ProjectProject)
    class Meta:
        managed = False
        db_table = 'project_tugroup_projects'

class ProjectTugroupTargetUsers(models.Model):
    id = models.IntegerField(primary_key=True)
    tugroup = models.ForeignKey(ProjectTugroup)
    targetuser = models.ForeignKey(ProjectTargetuser)
    class Meta:
        managed = False
        db_table = 'project_tugroup_target_users'

class ProjectTwitterapikey(models.Model):
    id = models.IntegerField(primary_key=True)
    consumer_key = models.CharField(unique=True, max_length=100, blank=True)
    consumer_secret = models.CharField(unique=True, max_length=100, blank=True)
    bot = models.ForeignKey(CoreTwitterbot)
    date_created = models.DateTimeField()
    max_bots_using = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'project_twitterapikey'

class ProjectTwitterbotaccesstoken(models.Model):
    id = models.IntegerField(primary_key=True)
    twitter_access_token = models.CharField(max_length=100, blank=True)
    twitter_access_token_secret = models.CharField(max_length=100, blank=True)
    bot = models.ForeignKey(CoreTwitterbot)
    twitter_api_key = models.ForeignKey(ProjectTwitterapikey)
    is_being_used = models.IntegerField()
    date_taken = models.DateTimeField(blank=True, null=True)
    next_change_date = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'project_twitterbotaccesstoken'

class ProjectTwitteruser(models.Model):
    id = models.IntegerField(primary_key=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    source = models.IntegerField()
    username = models.CharField(max_length=160)
    twitter_id = models.BigIntegerField()
    country = models.CharField(max_length=2, blank=True)
    language = models.CharField(max_length=2)
    city = models.CharField(max_length=80, blank=True)
    created_date = models.DateTimeField()
    full_name = models.CharField(max_length=160, blank=True)
    geo_enabled = models.IntegerField()
    time_zone = models.CharField(max_length=50, blank=True)
    last_tweet_date = models.DateTimeField(blank=True, null=True)
    followers_count = models.IntegerField(blank=True, null=True)
    tweets_count = models.IntegerField(blank=True, null=True)
    verified = models.IntegerField()
    date_saved = models.DateTimeField()
    has_clicked_mutweet = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'project_twitteruser'

class ProjectTwitteruserNew(models.Model):
    id = models.IntegerField(primary_key=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    source = models.IntegerField()
    username = models.CharField(max_length=160)
    twitter_id = models.BigIntegerField()
    country = models.CharField(max_length=2, blank=True)
    language = models.CharField(max_length=2)
    city = models.CharField(max_length=80, blank=True)
    created_date = models.DateTimeField()
    full_name = models.CharField(max_length=160, blank=True)
    geo_enabled = models.IntegerField()
    time_zone = models.CharField(max_length=50, blank=True)
    last_tweet_date = models.DateTimeField(blank=True, null=True)
    followers_count = models.IntegerField(blank=True, null=True)
    tweets_count = models.IntegerField(blank=True, null=True)
    verified = models.IntegerField()
    date_saved = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'project_twitteruser_new'

class ProjectTwitteruserhashashtag(models.Model):
    id = models.IntegerField(primary_key=True)
    hashtag = models.ForeignKey(ProjectHashtag)
    twitter_user = models.ForeignKey(ProjectTwitteruser)
    date_saved = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'project_twitteruserhashashtag'

class SouthMigrationhistory(models.Model):
    id = models.IntegerField(primary_key=True)
    app_name = models.CharField(max_length=255)
    migration = models.CharField(max_length=255)
    applied = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'south_migrationhistory'