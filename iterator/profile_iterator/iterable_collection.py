from abc import ABC, abstractmethod

class IterableCollection(ABC):
    
    @abstractmethod
    def create_friend_profile_iterator(self):
        pass
    
    @abstractmethod
    def create_mutual_friend_profile_iterator(self):
        pass
    
    @abstractmethod
    def create_family_profile_iterator(self):
        pass