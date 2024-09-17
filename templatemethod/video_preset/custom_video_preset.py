from video_preset import VideoPreset

class CustomVideoPreset(VideoPreset):
    def _apply_color_correction(self):
        print("Apply my favorite color correction...")

    def _render_video(self):
        print("Render video for FHD...")

        