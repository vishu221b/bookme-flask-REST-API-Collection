import mongoengine as meng
import datetime
from .book import Book
from .EmbeddedModels import *


class User(meng.Document):
    created_at = meng.ComplexDateTimeField(default=datetime.datetime.now)
    first_name = meng.StringField(required=True, min_length=1, max_length=50)
    last_name = meng.StringField(required=False, max_length=50, default="")
    date_of_birth = meng.DateTimeField(required=True)
    phone_number = meng.LongField(required=True)
    email = meng.EmailField(required=True, unique=True)
    username = meng.StringField(required=True, unique=True)
    alt_username = meng.StringField(required=False)
    password = meng.StringField(required=True)
    last_updated_at = meng.ComplexDateTimeField(default=datetime.datetime.now)
    is_admin = meng.BooleanField(default=False)
    is_active = meng.BooleanField(default=True)
    last_updated_by = meng.ReferenceField('self')
    marked_active_inactive_by_admin = meng.BooleanField(default=False)
    fav_books = meng.ListField(meng.ReferenceField(Book))
    all_followers = meng.EmbeddedDocumentListField(Followers, default=[])
    all_following = meng.EmbeddedDocumentListField(Following, default=[])
    blocked_users = meng.EmbeddedDocumentListField(Blocked, default=[])
    profile_picture = meng.URLField()

    meta = {
        'db_alias': 'bms_ent',
        'collection': 'user'
    }
