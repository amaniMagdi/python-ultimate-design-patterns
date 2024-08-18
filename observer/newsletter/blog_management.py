from typing import List, Dict
from subscription_type import SubscriptionType
from subscriber import Subscriber
from blog import Blog
from newsletter import Newsletter


class BlogManagement:
    def __init__(self):
        self.subscribers: Dict[SubscriptionType, List[Subscriber]] = {}
        self.blogs: List[Blog] = []
        self.newsletters: List[Newsletter] = []
        self.init_subscribers_types()

    def init_subscribers_types(self):
        for subscription_type in SubscriptionType:
            self.subscribers[subscription_type] = []

    def subscribe(self, subscription_type: SubscriptionType, subscriber: Subscriber):
        self.subscribers[subscription_type].append(subscriber)

    def unsubscribe(self, subscription_type: SubscriptionType, subscriber: Subscriber):
        self.subscribers[subscription_type].remove(subscriber)
    
    def notify_subscribers(self, subscription_type: SubscriptionType, message):
        for subscriber in self.subscribers[subscription_type]:
            subscriber.notify(message)
    
    def write_new_blog(self, blog: Blog):
        self.blogs.append(blog)
        self.notify_subscribers(SubscriptionType.NEW_BLOGS, "New blog is published...")

    def write_newsletter(self, newsletter: Newsletter):
        self.newsletters.append(newsletter)
        self.notify_subscribers(SubscriptionType.NEWSLETTER, "New newsletter is published...")
