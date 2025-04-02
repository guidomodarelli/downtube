"""
Implementation of the YouTube interface using yt-dlp.
"""

from pathlib import Path
import yt_dlp # type: ignore

from lib.YouTube.domain.youtube import YouTube, QUALITY

class YtdlpYouTube(YouTube):
    """
    Implementation of the YouTube interface using yt-dlp library.
    """

    def __init__(self, download_path: Path) -> None:
        """
        Initializes the YtdlpYouTube implementation.

        Args:
            download_path (Path): The path where downloaded files will be saved.
        """
        super().__init__(download_path)
        self.ydl_opts = {
            'outtmpl': str(self.download_path) + '/%(title)s.%(ext)s',
            'quiet': False,
            'no_warnings': False,
        }

    def download_video(self, url: str, quality: QUALITY = QUALITY.BEST) -> None:
        """
        Downloads a video from YouTube using yt-dlp.

        Args:
            url (str): The URL of the video to download.
            quality (QUALITY): The quality of the video to download.
        """
        options = self.ydl_opts.copy()

        if quality == QUALITY.BEST:
            options['format'] = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
        elif quality == QUALITY.LOWEST:
            options['format'] = 'worstvideo+worstaudio/worst'

        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])

    def download_playlist(self, url: str, quality: QUALITY = QUALITY.BEST) -> None:
        """
        Downloads a playlist from YouTube using yt-dlp.

        Args:
            url (str): The URL of the playlist to download.
            quality (QUALITY): The quality of the videos to download.
        """
        options = self.ydl_opts.copy()
        options['ignoreerrors'] = True
        options['outtmpl'] = str(self.download_path) + '/%(playlist_title)s/%(playlist_index)s-%(title)s.%(ext)s'

        if quality == QUALITY.BEST:
            options['format'] = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
        elif quality == QUALITY.LOWEST:
            options['format'] = 'worstvideo+worstaudio/worst'

        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])

    def download_audio(self, url: str, quality: QUALITY = QUALITY.BEST) -> None:
        """
        Downloads audio only from a YouTube video using yt-dlp.

        Args:
            url (str): The URL of the video to extract audio from.
            quality (QUALITY): The quality of the audio to download.
        """
        options = self.ydl_opts.copy()
        options['format'] = 'bestaudio/best' if quality == QUALITY.BEST else 'worstaudio/worst'
        options['outtmpl'] = str(self.download_path) + '/%(title)s.%(ext)s'
        options['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192' if quality == QUALITY.BEST else '64',
        }]

        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])

    def download_description(self, url: str) -> None:
        """
        Downloads the description of a YouTube video using yt-dlp.

        Args:
            url (str): The URL of the video to download the description from.
        """
        options = {
            'quiet': True,
            'no_warnings': True,
            'skip_download': True,
            'writeinfojson': True,
            'outtmpl': str(self.download_path) + '/%(title)s'
        }

        with yt_dlp.YoutubeDL(options) as ydl:
            info = ydl.extract_info(url, download=True)
            video_title = info.get('title', 'video')

            # Create a clean description file
            desc_file = self.download_path / f"{video_title}.description.txt"
            with open(desc_file, 'w', encoding='utf-8') as f:
                f.write(info.get('description', ''))
