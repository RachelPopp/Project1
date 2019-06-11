import requests

url = "http://developer.echonest.com/api/v4/song/profile?api_key=YOUR_API_KEY&track_id=spotify:track:4toSP60xmDNCFuXly8ywNZ&bucket=id:spotify&bucket=audio_summary"

print(requests.get(url).json())