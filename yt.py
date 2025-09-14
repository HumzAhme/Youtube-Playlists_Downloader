import os
import yt_dlp
import socket
import time

def wait_for_connection(host="www.youtube.com", port=80, delay=5):
    """Wait until the internet is reachable before continuing."""
    while True:
        try:
            socket.create_connection((host, port), timeout=5)
            return  # internet is back
        except OSError:
            print(f"🌐 No internet. Retrying in {delay} seconds...")
            time.sleep(delay)

def download_playlist(playlist_url, download_type):
    # First get playlist info
    ydl_opts_info = {"quiet": True, "extract_flat": True}
    with yt_dlp.YoutubeDL(ydl_opts_info) as ydl:
        info = ydl.extract_info(playlist_url, download=False)
        playlist_title = info.get("title", "playlist")
        entries = info.get("entries", [])

    # Create a folder for the playlist
    os.makedirs(playlist_title, exist_ok=True)

    # Failed log file
    failed_log_path = os.path.join(playlist_title, f"{playlist_title}_failed.txt")

    # Set format depending on user choice
    if download_type == "mp4":
        ydl_opts = {
            "format": "bv*+ba/best",
            "merge_output_format": "mp4",
            "outtmpl": os.path.join(playlist_title, "%(playlist_index)s - %(title)s.%(ext)s"),
            "overwrites": False,
            "ignoreerrors": False,
        }
        file_ext = "mp4"
    else:  # mp3
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": os.path.join(playlist_title, "%(playlist_index)s - %(title)s.%(ext)s"),
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
            "overwrites": False,
            "ignoreerrors": False,
        }
        file_ext = "mp3"

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for idx, entry in enumerate(entries, start=1):
            if not entry:
                continue

            url = entry.get("url")
            title = entry.get("title", f"video_{idx}")
            outname = os.path.join(playlist_title, f"{idx} - {title}.{file_ext}")

            # Skip if file already exists
            if os.path.exists(outname):
                print(f"⏭ Skipping (already downloaded): {outname}")
                continue

            # Try downloading with network check
            while True:
                try:
                    print(f"▶ Downloading {idx}/{len(entries)}: {title}")
                    ydl.download([url])
                    break  # success → move to next video
                except Exception as e:
                    if "getaddrinfo failed" in str(e):
                        print(f"⚠ Network error for {url}, waiting to retry...")
                        wait_for_connection()
                        continue  # retry same video
                    else:
                        print(f"❌ Failed permanently: {url}")
                        with open(failed_log_path, "a", encoding="utf-8") as f:
                            f.write(url + "\n")
                        break  # move to next video

    print("\n✅ Playlist download finished!")
    if os.path.exists(failed_log_path):
        print(f"⚠ Some links failed permanently. See: {failed_log_path}")


if __name__ == "__main__":
    playlist_url = input("Enter YouTube playlist URL: ").strip()
    download_type = input("Download as mp4 or mp3? ").strip().lower()
    if download_type not in ["mp4", "mp3"]:
        print("❌ Invalid choice! Defaulting to mp4.")
        download_type = "mp4"
    download_playlist(playlist_url, download_type)
