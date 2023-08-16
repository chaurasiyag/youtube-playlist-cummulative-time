from pytube import YouTube,Playlist

class Playlist_Cummulative_time:
    def __init__(self, playlist_url) -> None:
        self.playlist_url = playlist_url
    
    def get_video_list(self):
        return Playlist(self.playlist_url).video_urls
    
    def cummulative_time(self):
        time = 0
        videos_list = self.get_video_list()
        for url in videos_list:
            youtube_obj = YouTube(url)
            time += youtube_obj.length
        print("No of videos in the playlist: ",len(videos_list))
        print("Playlist Cummulative Time in Second", time)
        print("Playlist Cummulative Time in Minute", time/60)
        print("Playlist Cummulative Time in Hour", time/3600)


    


