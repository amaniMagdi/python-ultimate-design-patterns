from video_provider import VideoProvider

class YouTubeVideoProvider(VideoProvider):
    def __init__(self, video_quality):
        self.video_quality = video_quality

    def playback(self, video_id):
        self.video_quality.render()
        print("Playback YouTube video...")