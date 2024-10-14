class MutualFriendProfileIterator:  
    def __init__(self, profile_collection):
        self.profile_collection = profile_collection
        self.current_mutual_friend_profile_position = 0
    
    def has_next(self) -> bool:
        return self.current_mutual_friend_profile_position < len(self.profile_collection.get_profiles())
    
    def get_next(self):
        print("Iterating through a graph DFS / BFS")
        if not self.has_next():
            return None
        profile = self.profile_collection.get_profiles()[self.current_mutual_friend_profile_position]
        self.current_mutual_friend_profile_position += 1
        return profile