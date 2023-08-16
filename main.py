from playlist import Playlist_Cummulative_time
import sys

if __name__ == '__main__':
    playlist_url = sys.argv[1]
    run = Playlist_Cummulative_time(playlist_url=playlist_url)
    run.cummulative_time()
    