from iterable_collection import IterableCollection
from friend_profile_iterator import FriendProfileIterator
from mutual_friend_profile_iterator import MutualFriendProfileIterator
from family_profile_iterator import FamilyProfileIterator

class ProfileCollection(IterableCollection):
    
    def __init__(self, profiles, profile_id):
        self.profiles = profiles
        self.profile_id = profile_id
    
    def get_profiles(self):
        return self.profiles
    
    def create_friend_profile_iterator(self):
        return FriendProfileIterator(self)
    
    def create_mutual_friend_profile_iterator(self):
        return MutualFriendProfileIterator(self)
    
    def create_family_profile_iterator(self):
        return FamilyProfileIterator(self)
