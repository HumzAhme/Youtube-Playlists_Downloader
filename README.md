# 🎥 YouTube Playlist Downloader (MP4 / MP3)

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)  
![yt-dlp](https://img.shields.io/badge/yt--dlp-latest-brightgreen.svg)  
![License](https://img.shields.io/badge/license-MIT-orange.svg)

---

A **Python-powered YouTube Playlist Downloader** that makes it easy to grab full playlists in the **best quality** with automatic error handling.  

✨ **Features:**
- 📂 Creates a **folder named after the playlist**  
- ⏭ **Skips already-downloaded files**  
- 🔄 Waits if internet/VPN disconnects, then **resumes automatically**  
- 📝 Logs permanently failed videos into `failed.txt`  
- 🎵 Download as **MP4** (video+audio) or **MP3** (audio only)  
- ⚡ Uses [yt-dlp](https://github.com/yt-dlp/yt-dlp) for fast, reliable downloads  

---

## 📖 Table of Contents

1. [Requirements](#-requirements)  
2. [Installation](#-installation)  
3. [Usage](#-usage)  
4. [Output Structure](#-output-structure)  
5. [Full Script](#-full-script)  
6. [Example Run](#-example-run)  
7. [Troubleshooting](#-troubleshooting)  
8. [FAQ](#-faq)  
9. [Roadmap](#-roadmap--ideas)  
10. [Contributing](#-contributing)  
11. [License](#-license)  

---

## 🛠 Requirements

- **Python 3.8+**  
- **yt-dlp** (latest)  
- **FFmpeg** (for MP4 merging & MP3 conversion)  

---

## 📦 Installation

1. Clone or download this repository:
   ```bash
   git clone https://github.com/yourusername/youtube-playlist-downloader.git
   cd youtube-playlist-downloader


## Install dependencies:

    pip install yt-dlp


## Install FFmpeg:

Download from gyan.dev builds
Extract → move bin folder to e.g. C:\ffmpeg\bin
Add C:\ffmpeg\bin to PATH
Verify:

` ffmpeg -version `

## ▶️ Usage

Run the script:

` python downloader.py `


You will be prompted to:

- Enter a playlist URL
- Choose download format → mp4 or mp3

# 📂 Output Structure

A folder is created with the playlist name:

My Playlist/
├── 1 - First Video.mp4
├── 2 - Second Video.mp4
├── 3 - Third Video.mp4
├── My Playlist_failed.txt


Videos already in the folder are skipped

Permanently failed links are logged in *_failed.txt
