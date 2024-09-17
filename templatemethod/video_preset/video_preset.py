from abc import ABC, abstractmethod

class VideoPreset(ABC):
    """
    apply_preset() method containing the template steps, 
    note that methods starts with __ are private =>
    concrete classes can inherit private methods, but they cannot override them directly 
    due to name mangling.
    methods starts with _ are protected =>
    concrete classes can inherit protected methods, and can override them directly.
    """
    def apply_preset(self):
        self.__enhance_video_quality()
        self._apply_color_correction()
        self.__enhance_audio_quality()
        self.__apply_filters()
        self._render_video()

    def __enhance_video_quality(self):
        pass

    @abstractmethod
    def _apply_color_correction(self):
        pass

    def __enhance_audio_quality(self):
        print("enhancing audio quality...")

    def __apply_filters(self):
        pass

    @abstractmethod
    def _render_video(self):
        pass

