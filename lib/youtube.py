from abc import ABC, abstractmethod
from pathlib import Path

class YouTube(ABC):
    """
    Interface for YouTube operations.
    """

    @abstractmethod
    def __init__(self, download_path: Path) -> None:
        """
        Initializes the YouTube interface.

        Args:
            download_path (Path): The path where downloaded files will be saved.
        """
        self.download_path = download_path
        self.download_path.mkdir(parents=True, exist_ok=True)

    @abstractmethod
    def download_video(self, url: str) -> None:
        """
        Downloads a video from YouTube.

        Args:
            url (str): The URL of the video to download.
        """
        raise NotImplementedError("This method is not yet implemented.")

    @abstractmethod
    def download_playlist(self, url: str) -> None:
        """
        Downloads a playlist from YouTube.

        Args:
            url (str): The URL of the playlist to download.
        """
        raise NotImplementedError("This method is not yet implemented.")

    def download_audio(self, url: str) -> None:
        """
        Downloads audio only from a YouTube video.

        Args:
            url (str): The URL of the video to extract audio from.
        """
        raise NotImplementedError("This method is not yet implemented.")

    def download_with_options(self, url: str, resolution: str = None, format: str = None,
                            subtitles: bool = False, audio: bool = True,
                            thumbnails: bool = False, metadata: bool = False,
                            description: bool = False, tags: bool = False) -> None:
        """
        Downloads a video with various options.

        Args:
            url (str): The URL of the video to download.
            resolution (str, optional): The resolution of the video (e.g., "1080p").
            format (str, optional): The format of the video (e.g., "mp4", "webm").
            subtitles (bool, optional): Whether to download subtitles. Defaults to False.
            audio (bool, optional): Whether to include audio. Defaults to True.
            thumbnails (bool, optional): Whether to include thumbnails. Defaults to False.
            metadata (bool, optional): Whether to include metadata. Defaults to False.
            description (bool, optional): Whether to include the description. Defaults to False.
        """
        raise NotImplementedError("This method is not yet implemented.")