![Challenge banner](/docs/assets/challenge-banner.jpg)

# Observations
> These are informal observations and findings made during the development process.

## Day 1 — 24-05-2025
- The main library for the **Spotify API** is `spotipy` from [spotipy-dev](https://github.com/spotipy-dev/spotipy?tab=readme-ov-file).  
- Several **Spotify API** endpoints are deprecated, limiting available features.  
    - An alternative API for extracting audio features is available at [reccobeats](https://reccobeats.com/docs/apis/extract-audio-features).  
    - **Kaggle** datasets provide additional audio feature data to compensate for missing **Spotify** features.  
    - Downloading the user data, as demonstrated in [yussufbiyik](https://github.com/yussufbiyik/how-much-time-you-spent-listening-music-on-spotify?tab=readme-ov-file)'s project, offer another approach to data extraction.  
- The **Spotify API** scopes are well documented in the [official docs](https://developer.spotify.com/documentation/web-api/concepts/scopes).  
- The site [statsforspotify.com](https://www.statsforspotify.com/track/recent) offers useful visualization of accessible **Spotify** data.  
- The site [organizeyourmusic.playlistmachinery.com](http://organizeyourmusic.playlistmachinery.com) contains extensive info, though much is now deprecated.  
-   Its _Bearer Auth_ token can be used to bypass some deprecated endpoints and access data.  


## Day 2 — 25-05-2025
- There is a `.pptx` template from the site [ditchthattextbook.com](https://ditchthattextbook.com/spotify-wrapped/); templates for this kind of project are rare.  
- The site [spotifyunhinged.com](https://www.spotifyunhinged.com) has uses a video template via a web editor.  
    - Considering recreating the video template in **React**, but lack of experience and deadline constraints are concerns.  
    - I used `playwright` to automate website interactions; however, it requires an active session.  
- According to the [Spotify documentation](https://developer.spotify.com/documentation/web-api/concepts/quota-modes), new users must be registered in the Dashboard to use the app.  