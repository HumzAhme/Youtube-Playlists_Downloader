# 🎥 YouTube Playlist Downloader (MP4 / MP3)

A Python script to download entire **YouTube playlists** with reliability.  
Built on top of [yt-dlp](https://github.com/yt-dlp/yt-dlp), with improvements:

- 📂 Creates a **folder with playlist name**  
- ⏭ **Skips already-downloaded files**  
- 🔄 **Waits for internet reconnect** (VPN/IP switch, disconnect, etc.) instead of skipping  
- 📝 Logs permanently failed videos (deleted/private/blocked) into `failed.txt`  
- 🎵 Choose format: **MP4** (best video+audio) or **MP3** (audio-only with FFmpeg)  

---

## 🛠 Requirements

1. **Python 3.8+** → [Download](https://www.python.org/downloads/)  
   Ensure you tick ✅ *"Add Python to PATH"* during installation.

2. **yt-dlp** (Python package)  
   ```bash
   pip install yt-dlp
