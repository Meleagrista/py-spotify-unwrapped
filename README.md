<div align="center">
  <!--suppress CheckImageSize -->
  <img src="/docs/assets/project-logo-01.png" alt="logo" width="200" height="auto"/>
  <h1>Spotify Unwrapped</h1>
  <p>
    Personalized Spotify Wrapped-style video generation from listening data, currently in a rudimentary state.
  </p>
  <p>
    <a href="">
    <img src="https://img.shields.io/badge/experimental-%23FFA500?label=status" alt="state" />
    </a>
    <a href="">
      <img src="https://img.shields.io/github/last-commit/Meleagrista/py-spotify-unwrapped" alt="last update" />
    </a>
    <a href="https://github.com/Meleagrista/py-spotify-unwrapped/stargazers">
      <img src="https://img.shields.io/github/stars/Meleagrista/py-spotify-unwrapped" alt="stars" />
    </a>
    <a href="https://github.com/Meleagrista/py-spotify-unwrapped/network/members">
      <img src="https://img.shields.io/github/forks/Meleagrista/py-spotify-unwrapped" alt="forks" />
    </a>
    <a href="https://github.com/Meleagrista/py-spotify-unwrapped/blob/master/LICENSE.txt">
      <img src="https://img.shields.io/github/license/Meleagrista/py-spotify-unwrapped" alt="license" />
    </a>
  </p>

  <h4>
    <a href="https://github.com/Meleagrista/py-spotify-unwrapped/blob/master/docs/CHALLEGE.md">Challege</a>
    <span> · </span>
    <a href="https://github.com/Meleagrista/py-spotify-unwrapped/blob/master/docs/OBSERVATIONS.md">Observations</a>
  </h4>
</div>

# Table of Contents
- [About the Project](#about-the-project)
  - [Project Status](#project-status)
  - [Build With](#build-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
    - [Spotify for Developers](#spotify-for-developers)
    - [Poetry](#poetry)
 - [Usage](#usage)
- [Installation](#installation)
- [Roadmap](#roadmap)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

# About the Project
This project tries to generate a monthly _wrapped_ experience inspired by **Spotify’s** official year-in-review. By analyzing your personal listening data, it generates a visual summary of your music habits each month, closely mirroring the style and layout of Spotify's own recap.

## Project Status
Originally developed as a challenge within a strict timeframe, the implementation is quite rough. However, several solutions were considered and documented. I may return to the project in the future to refine and improve it further.

> [!IMPORTANT]
> Although the project meets its original objective, the current implementation is highly inefficient. It demands significant processing time and relies on a rigid template, which results in a mediocre final output.

## Build With
[![Python][python-badge]][python-url]
[![Poetry][poetry-badge]][poetry-url]

> Also using the following libraries...

![Spotipy][spotipy-badge]
![Playwright][playwright-badge]

# Getting Started
Follow these steps to set up and run the project locally.

## Prerequisites
Before running this project, ensure you have the following tools installed.

### Spotify for Developers
To run the program you need either the identification and key of a **Spotify Web API** app or to create one yourself. You can check the [documentation](https://github.com/spotipy-dev/spotipy?tab=readme-ov-file#quick-start) for `spotipy` to see what is needed to set up a **Spotify** app.

> [!WARNING]
> This section is not finished and pending of change.

### Poetry
Poetry is used for dependency management, it is needed to install and manage the libraries for the project.

- **Linux / macOS:**
  ```bash
  curl -sSL https://install.python-poetry.org | python3 -
  ```

- **Windows**   
Download and run the installer from the official [website](https://python-poetry.org/docs/#installing-with-pipx).

After installation, ensure Poetry is added to your `PATH`:
  ```bash
  export PATH="$HOME/.local/bin:$PATH"
  ```

> [!NOTE] 
> Poetry is not actually required, you can create an environment based on the dependencies of `pyproject.toml`

## Installation
Follow these steps to set up the project on your local machine.

1. **Clone the repository.**
    ```bash
    git clone https://github.com/Meleagrista/py-spotify-unwrapped.git
    ```

2. **Navigate to the project directory.**
    ```bash
    cd py-spotify-unwrapped
    ```

3. **Set up the environment**     
   If you're using **Poetry**, install the dependencies with:
    ```bash
    poetry install
    ```

4. Set the neccesary credentials.
   1. Create a `.env` file in the root directory (if it doesn't already exist) and fill in the required variables:
  
      ```plaintext
      YOUR_APP_CLIENT_ID=<your_spotify_app_client_id>
      YOUR_APP_CLIENT_SECRET=<your_spotify_app_client_secret>
      ```
    2. Obtain a session for the Butter website:
       - Visit [spotifyunhinged.com](https://www.spotifyunhinged.com) and log in.
       - Export your browser session and save it to the `session/` folder.
       - Rename the file to `butter_state.json`.

# Usage
Follow the steps below to get started and use the project effectively.
```bash
```

> [!WARNING]
> This section is not finished and pending of change.

# Roadmap
The following features and enhancements are planned for development.
- [ ] Add a template for video generation using a front-end framework or language.
- [ ] Update the login flow for a more streamlined user experience.
- [ ] Update credential cache management.

# License
This project is licensed under the **GNU General Public License v3.0**. See the [LICENSE.txt](./LICENSE) file for full license details.

# Contact
Feel free to reach out if you have any questions or feedback.

Martín do Río Rico - [mdoriorico@gmail.com](mailto:mdoriorico@gmail.com)

# Acknowledgements
Special thanks to the following projects and resources that inspired or supported this project.

- [spotipy](https://github.com/spotipy-dev/spotipy) – A light weight library for the **Spotify Web API**.
- [Spotify Unhinged](https://www.spotifyunhinged.com) – A video template for a **Spotify** review.
- [Awesome Readme Template](https://github.com/Louis3797/awesome-readme-template) – A great starting point for crafting high-quality README files.
- [Best-README-Template](https://github.com/othneildrew/Best-README-Template) – Another excellent template resource for project documentation.
- [Shields.io](https://shields.io/) – For providing useful badges to enhance the README.

<!-- MARKDOWN SHORTCUTS -->

<!-- Status -->
[experimental]: https://img.shields.io/badge/experimental-%23FFA500?label=status
[stable]: https://img.shields.io/badge/stable-%237ED957?label=status
[unstable]: https://img.shields.io/badge/unstable-%23FF4C4C?label=status
[archived]: https://img.shields.io/badge/archived-%23A0A0A0?label=status

<!-- Tech stack -->
[python-badge]: https://img.shields.io/badge/python-%233776AB?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://www.python.org
[poetry-badge]: https://img.shields.io/badge/poetry-%2360A5FA?style=for-the-badge&logo=poetry&logoColor=white
[poetry-url]: https://python-poetry.org

<!-- Custom badges -->
[spotipy-badge]: https://img.shields.io/badge/Spotipy-%23868686?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8%2BCjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB2aWV3Qm94PSIwIDAgNDk2IDUxMiI%2BCiAgPHBhdGggZmlsbD0iIzFlZDc2MCIgZD0iTTI0OCA4QzExMS4xIDggMCAxMTkuMSAwIDI1NnMxMTEuMSAyNDggMjQ4IDI0OCAyNDgtMTExLjEgMjQ4LTI0OFMzODQuOSA4IDI0OCA4WiIvPgogIDxwYXRoIGQ9Ik00MDYuNiAyMzEuMWMtNS4yIDAtOC40LTEuMy0xMi45LTMuOS03MS4yLTQyLjUtMTk4LjUtNTIuNy0yODAuOS0yOS43LTMuNiAxLTguMSAyLjYtMTIuOSAyLjYtMTMuMiAwLTIzLjMtMTAuMy0yMy4zLTIzLjYgMC0xMy42IDguNC0yMS4zIDE3LjQtMjMuOSAzNS4yLTEwLjMgNzQuNi0xNS4yIDExNy41LTE1LjIgNzMgMCAxNDkuNSAxNS4yIDIwNS40IDQ3LjggNy44IDQuNSAxMi45IDEwLjcgMTIuOSAyMi42IDAgMTMuNi0xMSAyMy4zLTIzLjIgMjMuM3ptLTMxIDc2LjJjLTUuMiAwLTguNy0yLjMtMTIuMy00LjItNjIuNS0zNy0xNTUuNy01MS45LTIzOC42LTI5LjQtNC44IDEuMy03LjQgMi42LTExLjkgMi42LTEwLjcgMC0xOS40LTguNy0xOS40LTE5LjRzNS4yLTE3LjggMTUuNS0yMC43YzI3LjgtNy44IDU2LjItMTMuNiA5Ny44LTEzLjYgNjQuOSAwIDEyNy42IDE2LjEgMTc3IDQ1LjUgOC4xIDQuOCAxMS4zIDExIDExLjMgMTkuNy0uMSAxMC44LTguNSAxOS41LTE5LjQgMTkuNXptLTI2LjkgNjUuNmMtNC4yIDAtNi44LTEuMy0xMC43LTMuNi02Mi40LTM3LjYtMTM1LTM5LjItMjA2LjctMjQuNS0zLjkgMS05IDIuNi0xMS45IDIuNi05LjcgMC0xNS44LTcuNy0xNS44LTE1LjggMC0xMC4zIDYuMS0xNS4yIDEzLjYtMTYuOCA4MS45LTE4LjEgMTY1LjYtMTYuNSAyMzcgMjYuMiA2LjEgMy45IDkuNyA3LjQgOS43IDE2LjVzLTcuMSAxNS40LTE1LjIgMTUuNHoiLz4KPC9zdmc%2B

[playwright-badge]:https://img.shields.io/badge/Playwright-%23868686?style=for-the-badge&logo=data:image/png;base64,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
