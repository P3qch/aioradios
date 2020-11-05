# aioradios

aioradio is an asynchronous API wrapper for www.radio-browser.info

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install aioradios.

```bash
pip install aioradios
```

## Example usage

in:
```python
from aioradios import RadioBrowser

async def main():
    rb = RadioBrowser()
    await rb.init()

    radio = rb.search(name='UpBeatRadio', limit=1)
```
out:
```json
[
   {
      "changeuuid":"29c0910a-2fae-4623-8054-eaee674fe602",
      "stationuuid":"ad95f623-c7fd-4ecb-98d5-32242708ce63",
      "name":"UpBeatRadio",
      "url":"http://live.upbeat.pw/",
      "url_resolved":"http://live.upbeat.pw/",
      "homepage":"https://upbeat.pw/",
      "favicon":"http://upbeatradio.net/UpBeat.png",
      "tags":"",
      "country":"UK",
      "countrycode":"",
      "state":"",
      "language":"english",
      "votes":0,
      "lastchangetime":"2020-06-23 12:38:08",
      "codec":"MP3",
      "bitrate":128,
      "hls":0,
      "lastcheckok":1,
      "lastchecktime":"2020-11-04 04:14:11",
      "lastcheckoktime":"2020-11-04 04:14:11",
      "lastlocalchecktime":"2020-11-03 19:16:54",
      "clicktimestamp":"2020-10-22 15:09:37",
      "clickcount":8,
      "clicktrend":0
   }
]
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Documentation
For documentation do:
```py
from aioradios import RadioBrowser
help(RadioBrowser())
```

## License
[MIT](https://choosealicense.com/licenses/mit/)