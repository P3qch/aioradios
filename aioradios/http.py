"""
MIT License

Copyright (c) 2020 P3qch

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import aiohttp
from . import base_url
from .errors import UnsupportedFormat

class HTTP:
    def __init__(self, fmt, session = None):
        self.session = aiohttp.ClientSession() if not session else session
        self.fmt = fmt
    
    async def init(self):
        self.route = await base_url.pick_url()

    async def request(self, endpoint: str, params = {}):
        """
        A function to make a request to the API

        params:
        :endpoint: - the endpoint to request
        :fmt: - The return format. Can be JSON and XML
        """
 
        POSSIBLE_FORMATS = ('xml', 'json')

        if self.fmt.lower() not in POSSIBLE_FORMATS:
            raise UnsupportedFormat("Only xml and json formats are supported")

        headers = {"content-type": f"application/{self.fmt}", "User-Agent": "aioradios/dev"}

        async with self.session.get(f"{self.route}/{self.fmt}/{endpoint}", params=params, headers = headers) as resp:
            if self.fmt.lower() == 'json':
                return await resp.json()
            elif self.fmt.lower() == 'xml':
                return await resp.text()