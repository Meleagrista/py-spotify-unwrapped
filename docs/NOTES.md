# Development notes 
## Day 1
1. The core library is `spotipy` from *[spotipy-dev](https://github.com/spotipy-dev/spotipy?tab=readme-ov-file)*.
2. **Spotify** has deprecated several of their endpoints, so some features are not available.
3. The **Spotify Web API** has the [scopes](https://developer.spotify.com/documentation/web-api/concepts/scopes) for each call documented in the [API documentation](https://developer.spotify.com/documentation/web-api/reference/get-current-users-profile).
4. This [API](https://reccobeats.com/docs/apis/extract-audio-features) can be used to extract audio features like **Spotify Web API**.
5. To compensate for the missing features [datasets](https://www.kaggle.com/search?q=spotify+features+in%3Adatasets+sortBy%3Adate) can be used as well to extract audio features from songs in the set.
6. Other way to extract data is to request your user data, like *[yussufbiyik](https://github.com/yussufbiyik/how-much-time-you-spent-listening-music-on-spotify?tab=readme-ov-file)* suggested.
7. This [website](https://www.statsforspotify.com/track/recent) cane be good to visualize the data you can access.
8. This [website](http://organizeyourmusic.playlistmachinery.com) has a lot of information now deprecated, maybe it can be accessed through API calls to fill the gaps.
9. Actually, the last website's Bearer Auth token works to bypass the deprecated endpoints, so it can be used to get the data.
## Day 2
1. I got a `.pptx` template from this [website](https://ditchthattextbook.com/spotify-wrapped/), there is severe lack of templates for this kind of project.
2. I found a [website](https://www.spotifyunhinged.com) that uses a video template throught a web editor.
3. Ideally I would like to recreate the video template in something like **React**, but I have zero experience with it so it will make me go over the deadline.
4. I did use the `playwright` library to automate the interactions with the website, but it needs a session to work.
5. New users must be registered in the _Dashboard_ to be able to use the app as stated in the [documentation](https://developer.spotify.com/documentation/web-api/concepts/quota-modes).