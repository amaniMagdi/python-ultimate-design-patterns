from youtube_video_provider import YouTubeVideoProvider
from twitch_video_provider import TwitchVideoProvider
from sd_video_quality import SDVideoQuality
from hd_video_quality import HDVideoQuality

# Testing the implementation
def main():
    # Create video quality objects
    sd_quality = SDVideoQuality()
    hd_quality = HDVideoQuality()

    # Create video providers with different qualities
    youtube_provider_sd = YouTubeVideoProvider(sd_quality)
    youtube_provider_hd = YouTubeVideoProvider(hd_quality)

    twitch_provider_sd = TwitchVideoProvider(sd_quality)
    twitch_provider_hd = TwitchVideoProvider(hd_quality)

    # Test YouTube provider with SD and HD qualities
    print("Testing YouTube with SD Quality:")
    youtube_provider_sd.playback("youtube_video_1")
    print()

    print("Testing YouTube with HD Quality:")
    youtube_provider_hd.playback("youtube_video_2")
    print()

    # Test Twitch provider with SD and HD qualities
    print("Testing Twitch with SD Quality:")
    twitch_provider_sd.playback("twitch_video_1")
    print()
    
    print("Testing Twitch with HD Quality:")
    twitch_provider_hd.playback("twitch_video_2")


if __name__ == "__main__":
    main()