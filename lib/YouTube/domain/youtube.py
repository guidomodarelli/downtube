"""
This module defines the YouTube interface for various YouTube operations,
such as downloading videos, playlists, audio, subtitles, thumbnails, and metadata.
"""

from abc import ABC, abstractmethod
from pathlib import Path
from enum import Enum

class QUALITY(Enum):
    """
    Enum for video/audio quality options.
    """
    BEST = "best"
    LOWEST = "lowest"

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
    def download_video(self, url: str, quality: QUALITY) -> None:
        """
        Downloads a video from YouTube.

        Args:
            url (str): The URL of the video to download.
        """
        raise NotImplementedError("This method is not yet implemented.")

    @abstractmethod
    def download_playlist(self, url: str, quality: QUALITY) -> None:
        """
        Downloads a playlist from YouTube.

        Args:
            url (str): The URL of the playlist to download.
        """
        raise NotImplementedError("This method is not yet implemented.")

    def download_audio(self, url: str, quality: QUALITY) -> None:
        """
        Downloads audio only from a YouTube video.

        Args:
            url (str): The URL of the video to extract audio from.
            best (bool): Flag to indicate whether to download the best quality audio.
        """
        raise NotImplementedError("This method is not yet implemented.")

    def download_description(self, url: str) -> None:
        """
        Downloads the description of a YouTube video.
        Args:
            url (str): The URL of the video to download the description from.
        """
        raise NotImplementedError("This method is not yet implemented.")
