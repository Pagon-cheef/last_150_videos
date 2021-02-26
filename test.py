import requests


api_key = "AIzaSyC_g1lwI-xOgwrDZTvZVZft5rJq_gpdWLE"
channel_id = "UCbXgNpp0jedKWcQiULLbDTA"

# url = f"https://www.googleapis.com/youtube/v3/search?key={api_key}" \
#       f"&channelId={channel_id}&part=snippet&order=date&maxResults=50"

url = f"https://www.googleapis.com/youtube/v3/search?key={api_key}"


params = {
        "channelId": channel_id,
        "part": "snippet",
        "order": "date",
        "maxResults": 50
}

res = requests.get(url, params=params)

print(res.url)
