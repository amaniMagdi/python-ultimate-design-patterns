from blog import Blog
from newsletter import Newsletter
from subscription_type import SubscriptionType
from blog_management import BlogManagement
from user import User


def main():
    blog_management = BlogManagement()

    mona = User("Mona")
    noha = User("Noha")


    blog_management.subscribe(SubscriptionType.NEW_BLOGS, noha)
    blog_management.subscribe(SubscriptionType.NEWSLETTER, mona)

    new_blog = Blog("database schemas")
    new_newsletter = Newsletter("python is fine!")

    blog_management.write_new_blog(new_blog)
    blog_management.write_newsletter(new_newsletter)

if __name__ == "__main__":
    main()