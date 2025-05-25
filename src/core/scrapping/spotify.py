import os
from collections import Counter
from pathlib import Path

import requests
import spotipy

from dotenv import load_dotenv
from spotipy import SpotifyOAuth

load_dotenv()

YOUR_APP_CLIENT_ID = os.getenv("YOUR_APP_CLIENT_ID")
YOUR_APP_CLIENT_SECRET = os.getenv("YOUR_APP_CLIENT_SECRET")


class SpotifyScrapper:
    def __init__(self, max_length: int = 15):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=YOUR_APP_CLIENT_ID,
            client_secret=YOUR_APP_CLIENT_SECRET,
            redirect_uri="http://127.0.0.1:8000/callback",
            scope="user-library-read,user-top-read,user-read-recently-played",
        ))
        self._max_length = max_length

    def _truncate(self, text: str) -> str:
        return text[:self._max_length].strip() + "..." if len(text) > self._max_length else text

    @staticmethod
    def _download_image(url: str, save_dir: Path, filename: str) -> str:
        if not url:
            raise ValueError("URL cannot be empty")
        save_dir.mkdir(parents=True, exist_ok=True)
        local_path = save_dir / filename
        try:
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()
            with open(local_path, "wb") as f:
                f.write(resp.content)
            return str(local_path)
        except Exception as e:
            raise e

    def get_top_tracks(self, download_dir: Path) -> dict[str, str]:
        spotify_data = {}
        top_tracks = self.sp.current_user_top_tracks(limit=5, time_range='short_term')
        for idx, track in enumerate(top_tracks['items'], start=1):
            spotify_data[f"track_0{idx}"] = self._truncate(track['name'])
            spotify_data[f"track_artist_0{idx}"] = self._truncate(", ".join(artist['name'] for artist in track['artists']))

            album_images = track.get('album', {}).get('images', [])
            track_image_url = album_images[0]['url'] if album_images else ""
            local_track_image = self._download_image(track_image_url, download_dir, f"track_0{idx}.jpg")
            spotify_data[f"track_image_0{idx}"] = local_track_image

        return spotify_data

    def get_top_artists(self, download_dir: Path) -> dict[str, str]:
        spotify_data = {}
        top_artists = self.sp.current_user_top_artists(limit=5, time_range='short_term')
        for idx, artist in enumerate(top_artists['items'], start=1):
            spotify_data[f"artist_0{idx}"] = self._truncate(artist['name'])

            artist_images = artist.get('images', [])
            artist_image_url = artist_images[0]['url'] if artist_images else ""
            local_artist_image = self._download_image(artist_image_url, download_dir, f"artist_0{idx}.jpg")
            spotify_data[f"artist_image_0{idx}"] = local_artist_image

        return spotify_data

    def get_top_genres(self) -> dict[str, str]:
        spotify_data = {}
        all_genres = []
        total_artists = 0
        count = 1
        while True:
            offset = 50 * count
            response = self.sp.current_user_top_artists(limit=50, offset=offset, time_range='short_term')
            artists = response.get('items', [])
            if len(artists) == 0:
                break
            total_artists += len(artists)
            for artist in artists:
                all_genres.extend(artist.get('genres', []))
            count += 1
        genre_counts = Counter(all_genres)
        top_genres = genre_counts.most_common(5)
        for idx, genre in enumerate(top_genres, start=1):
            spotify_data[f"genre_0{idx}"] = self._truncate(genre[0].capitalize())

        return spotify_data
