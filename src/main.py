import tempfile
from datetime import datetime
from pathlib import Path

from src.core.automation.butter import fill_butter_template
from src.core.scrapping.spotify import SpotifyScrapper

def main():
    spotify = SpotifyScrapper(15)
    template_data = {"month": datetime.now().strftime("%B").capitalize()}

    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        template_data['temp_pptx_path'] = str(tmpdir / "spotify-wrapped-temp-output.pptx")

        template_data.update(spotify.get_top_tracks(tmpdir))
        template_data.update(spotify.get_top_artists(tmpdir))
        template_data.update(spotify.get_top_genres())

        fill_butter_template(template_data)

if __name__ == "__main__":
    main()
