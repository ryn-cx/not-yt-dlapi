<!-- TODO: Validate -->
# not-yt-dlapi

YouTube API wrapper.

## Alternatives
There are alternatives to this library that will better serve your needs because this
library only implements a small subset of YouTube's API. Here are the most common
alternatives and why they were not suitable for the requirements of the project this
library was written for.

| Library | Notes |
| --- | --- |
| [Python YouTube (pyyoutube)](https://github.com/sns-sdks/python-youtube/blob/master/pyyoutube/models/video.py) | Every field is nullable even when a field should always contain a value. |
| [Python YouTube API (python-youtube-api)](https://github.com/srcecde/python-youtube-api) | Designed for command line usage. |
| [Simple Youtube API (simple-youtube-api)](https://github.com/jonnekaunisto/simple-youtube-api) | Designed for searching and uploading videos and did not support the required endpoints. |
