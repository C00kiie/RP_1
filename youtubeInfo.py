import requests
APIKey = "<APIKEY>"


class YoutubeInfo:
    ID = 0
    Title = ""
    Description = ""
    PublishedAt = ""
    FetchingURL = ""
    chnanelTitle = ""
    tags = []
    def IDFetch(self, arg):
        IDRequest = "https://www.googleapis.com/youtube/v3/videos?id=" + arg + "&key=" + APIKey + "&part=snippet"
        self.FetchingURL = IDRequest
        if len(list(arg)) == 11:
            Data = requests.request(url=IDRequest, method="Get")
            Data = Data.json()
            self.ID = Data['items'][0]['id']
            self.Title = Data['items'][0]['snippet']['title']
            self.Description = Data['items'][0]['snippet']['description']
            self.PublishedAt = Data['items'][0]['snippet']['publishedAt']
            self.channelID = Data['items'][0]['snippet']['channelId']
            self.channelTitle = Data['items'][0]['snippet']['channelTitle']
            # tags, a list of items
            tags = []
            Array = Data['items'][0]['snippet']['tags']
            for i in Array:
                tags.append(i)
            self.tags = tags
        else:
            print("Wrong ID")


