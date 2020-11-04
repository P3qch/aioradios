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
import asyncio
from random import choice
from aiodns import DNSResolver
from typing import List
import socket

from .errors import noHostFound

async def get_radiobrowser_base_urls() -> List[str]:
    """
    Get all base urls of all currently available radiobrowser servers

    Returns: 
    List[str]: a list of string URLS
    """
    loop = asyncio.get_event_loop()
   
    resolver = DNSResolver(loop=loop)
    hosts = []

    # get all hosts from DNS
    ips = await loop.getaddrinfo('all.api.radio-browser.info',
                             80, family=0, type=0, proto=socket.IPPROTO_TCP)
    
    for ip_tupple in ips:
        ip = ip_tupple[4][0]

        host_addr = await resolver.gethostbyaddr(ip)
     
        if host_addr.name not in hosts:
            hosts.append(host_addr.name)

   
    hosts.sort()
    
    return list(map(lambda x: "https://" + x, hosts))

async def pick_url():

    urls = await get_radiobrowser_base_urls()

    if len(urls) == 0:
        raise noHostFound("No hosts found.")

    return choice(urls)