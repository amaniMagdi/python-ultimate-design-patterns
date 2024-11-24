from video_provider import VideoProvider

class TwitchVideoProvider(VideoProvider):
    def __init__(self, video_quality):
        self.video_quality = video_quality

    def playback(self, video_id):
        self.video_quality.render()
        print("Playback twitch video...")