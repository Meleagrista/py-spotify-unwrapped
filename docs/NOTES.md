# Development notes
1. The core library is `spotipy` from *[spotipy-dev](https://github.com/spotipy-dev/spotipy?tab=readme-ov-file)*.
2. **Spotify** has deprecated several of their endpoints, so some features are not available.
3. The **Spotify Web API** has the [scopes](https://developer.spotify.com/documentation/web-api/concepts/scopes) for each call documented in the [API documentation](https://developer.spotify.com/documentation/web-api/reference/get-current-users-profile).
4. This [API](https://reccobeats.com/docs/apis/extract-audio-features) can be used to extract audio features like **Spotify Web API**.
5. To compensate for the missing features [datasets](https://www.kaggle.com/search?q=spotify+features+in%3Adatasets+sortBy%3Adate) can be used as well to extract audio features from songs in the set.
6. Other way to extract data is to request your user data, like *[yussufbiyik](https://github.com/yussufbiyik/how-much-time-you-spent-listening-music-on-spotify?tab=readme-ov-file)* suggested.
7. This [website](https://www.statsforspotify.com/track/recent) cane be good to visualize the data you can access.
8. This [website](http://organizeyourmusic.playlistmachinery.com) has a lot of information now deprecated, maybe it can be accessed through API calls to fill the gaps.
9. Actually, the last website's Bearer Auth token works to bypass the deprecated endpoints, so it can be used to get the data.