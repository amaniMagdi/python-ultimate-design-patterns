from profile import Profile
from profile_collection import ProfileCollection

def main():
    # Sample profiles
    profiles = [
        Profile(profile_id="1", name="Alice"),
        Profile(profile_id="2", name="Bob"),
        Profile(profile_id="3", name="Charlie"),
        Profile(profile_id="4", name="Diana"),
    ]
    
    # Create ProfileCollection
    profile_collection = ProfileCollection(profiles, "1")
    
    # Create an iterator for mutual friends
    mutual_friend_iterator = profile_collection.create_mutual_friend_profile_iterator()
    
    print("Iterating through mutual friends:")
    # Iterate through the profiles
    while mutual_friend_iterator.has_next():
        profile = mutual_friend_iterator.get_next()
        if profile:
            print(f"Profile ID: {profile.profile_id}, Name: {profile.name}")

if __name__ == "__main__":
    main()
