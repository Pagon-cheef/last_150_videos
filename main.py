import json
import os
import requests


# Your API_KEY must be specified here
api_key = os.environ["YT_API_KEY"]

api_url = f"https://www.googleapis.com/youtube/v3/search?key={api_key}"

params = {
        "part": "snippet",
        "order": "date",
        "maxResults": 50
}


def save_to_json_file(file_name, data):
    with open("job.json", "w") as f:
        json.dump(data["items"], f, indent=4)


def save_to_txt_file(file_name, data):
    """
    Функция сохраняет результаты работы скрипта в текстовый файл.

    Parameters:
        file_name - (string) Имя сохраняемого файла
        data - (Dict) Словарь, из которого извлекаем для записи данные
    Returns:
        ???
    """
    for count, item in enumerate(data):
        try:
            link = f'https://www.youtube.com/watch?v={item["id"]["videoId"]}'
        except Exception:
            continue

        channel = item["snippet"]["channelTitle"]
        title = item["snippet"]["title"]

        with open("videos.txt", "a", encoding="utf-8") as file:
            file.write(f"{count + 1}) {channel}-{title}\n{link}\n")


def fetch_all_channel_videos(channel_url: str):
    """
    Fetches a playlist of videos from youtube
    We splice the results together in no particular order

    Parameters:
        parm1 - (string) playlistId
    Returns:
        playListItem Dict
    """

    page_token = None
    while True:
        next_page_token = f"&pageToken={page_token}" if page_token else ''

    res = requests.get(channel_url, params=params)
    data = res.json()

    # nextPageToken = data.get('nextPageToken')
    #
    # while nextPageToken:
    #     response = requests.get(url + f"&pageToken={nextPageToken}")
    #     data["items"] += response.json()["items"]
    #
    #     if "nextPageToken" in response:
    #         nextPageToken = True
    #     else:
    #         nextPageToken = False

    #     while 'nextPageToken' in res:
#             nextPage = youtube.playlistItems().list(
#             part="snippet",
#             playlistId=playlistId,
#             maxResults="50",
#             pageToken=nextPageToken
#             ).execute()
#             res['items'] = res['items'] + nextPage['items']
#
#             if 'nextPageToken' not in nextPage:
#                 res.pop('nextPageToken', None)
#             else:
#                 nextPageToken = nextPage['nextPageToken']

    return res


if __name__ == '__main__':
    url = "https://www.youtube.com/channel/UCbXgNpp0jedKWcQiULLbDTA"
    videos = fetch_all_channel_videos(url)
