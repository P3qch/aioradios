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
import asyncio
from typing import List

from .http import HTTP
from .errors import NotInitialized, RequiredMissing



class RadioBrowser:
    """
    The radio-browser class. Used for all requests.

    ...

    Attributes
    ----------
    session : aiohttp.ClientSession
        The aiohttp session to use for the requests.
    fmt: str
        The format to return, could be xml or json.
    """

    def __init__(self, session=None, fmt='json'):
        """
        Parameters
        ----------
        session : aiohttp.ClientSession, optional
            The aiohttp session to use for the requests. If None a new session is automatically created.
        fmt: str, optional
            The format to return, could be xml or json.
        """
        self.http = HTTP(fmt, session=session)
        self.__intialized = False

    async def init(self):
        """
        Initialize the ClientSession.
        """
        await self.http.init()
        self.__intialized = True

    async def countries(self, search=None, orderby: str = 'name', reverse: bool = False, hidebroken: bool = False) -> List[dict]:
        """
        Get the available country list.

        Parameters
        ----------
        search : str, optional
            The keyword to search by. If None returns the whole list. (Default is None)
        orderby : str, optional
            Name of the attribute the result list will be sorted by. (Default is 'name')
        reverse : bool, optional
            reverse the result list if set to true (Default is False)
        hidebroken : bool, optional
            Do not count broken stations (Default is False)

        Raises
        ------
        NotInitialized
            If not initialized
        """
        if not self.__intialized:
            raise NotInitialized("Please initialize the RadioBrowser.")

        reverse = str(reverse).lower()
        hidebroken = str(hidebroken).lower()

        params = {
            'order': orderby,
            'reverse': reverse,
            'hidebroken': hidebroken
        }

        if search:
            return await self.http.request(f"countries/{search}", params=params)
        else:
            return await self.http.request("countries/", params=params)

    async def countryCodes(self, search=None, orderby: str = 'name', reverse: bool = False, hidebroken: bool = False) -> List[dict]:
        """
        Get the available country code list.

        Parameters
        ----------
        search : str, optional
            The keyword to search by. If None returns the whole list. (Default is None)
        orderby : str, optional
            Name of the attribute the result list will be sorted by. (Default is 'name')
        reverse : bool, optional
            reverse the result list if set to true (Default is False)
        hidebroken : bool, optional
            Do not count broken stations (Default is False)

        Raises
        ------
        NotInitialized
            If not initialized
        """
        if not self.__intialized:
            raise NotInitialized("Please initialize the RadioBrowser.")

        reverse = str(reverse).lower()
        hidebroken = str(hidebroken).lower()

        params = {
            'order': orderby,
            'reverse': reverse,
            'hidebroken': hidebroken
        }

        if search:
            return await self.http.request(f"countrycodes/{search}", params=params)
        else:
            return await self.http.request("countrycodes/", params=params)

    async def codecs(self, search=None, orderby: str = 'name', reverse: bool = False, hidebroken: bool = False) -> List[dict]:
        """
        Get the available codec list.

        Parameters
        ----------
        search : str, optional
            The keyword to search by. If None returns the whole list. (Default is None)
        orderby : str, optional
            Name of the attribute the result list will be sorted by. (Default is 'name')
        reverse : bool, optional
            reverse the result list if set to true (Default is False)
        hidebroken : bool, optional
            Do not count broken stations (Default is False)

        Raises
        ------
        NotInitialized
            If not initialized
        """
        if not self.__intialized:
            raise NotInitialized("Please initialize the RadioBrowser.")

        reverse = str(reverse).lower()
        hidebroken = str(hidebroken).lower()

        params = {
            'order': orderby,
            'reverse': reverse,
            'hidebroken': hidebroken
        }

        if search:
            return await self.http.request(f"codecs/{search}", params=params)
        else:
            return await self.http.request("codecs/", params=params)

    async def states(self, search=None, orderby: str = 'name', reverse: bool = False, hidebroken: bool = False, country=None) -> List[dict]:
        """
        Get the available state list.

        Parameters
        ----------
        search : str, optional
            The keyword to search by. If None returns the whole list. (Default is None)
        orderby : str, optional
            Name of the attribute the result list will be sorted by. (Default is 'name')
        reverse : bool, optional
            reverse the result list if set to true (Default is False)
        hidebroken : bool, optional
            Do not count broken stations (Default is False)
        country : str, optional
            filter states by country name (Default is None)

        Raises
        ------
        NotInitialized
            If not initialized
        """
        if not self.__intialized:
            raise NotInitialized("Please initialize the RadioBrowser.")

        if country and not search:
            raise RequiredMissing("To filter by country, you have to provide a search keyword.")

        reverse = str(reverse).lower()
        hidebroken = str(hidebroken).lower()

        params = {
            'order': orderby,
            'reverse': reverse,
            'hidebroken': hidebroken,
            'country': country
        }

        if search and country:
            return await self.http.request(f"codecs/{country}/{search}", params=params)
        elif search and not country:
            return await self.http.request(f"codecs/{search}", params=params)
        else:
            return await self.http.request("codecs/", params=params)


    async def languages(self, search=None, orderby: str = 'name', reverse: bool = False, hidebroken: bool = False) -> List[dict]:
        """
        Get the available language list.

        Parameters
        ----------
        search : str, optional
            The keyword to search by. If None returns the whole list. (Default is None)
        orderby : str, optional
            Name of the attribute the result list will be sorted by. (Default is 'name')
        reverse : bool, optional
            reverse the result list if set to true (Default is False)
        hidebroken : bool, optional
            Do not count broken stations (Default is False)

        Raises
        ------
        NotInitialized
            If not initialized
        """
        if not self.__intialized:
            raise NotInitialized("Please initialize the RadioBrowser.")

        reverse = str(reverse).lower()
        hidebroken = str(hidebroken).lower()

        params = {
            'order': orderby,
            'reverse': reverse,
            'hidebroken': hidebroken
        }

        if search:
            return await self.http.request(f"languages/{search}", params=params)
        else:
            return await self.http.request("languages/", params=params)


    async def tags(self, search=None, orderby: str = 'name', reverse: bool = False, hidebroken: bool = False) -> List[dict]:
        """
        Get the available tag list.

        Parameters
        ----------
        search : str, optional
            The keyword to search by. If None returns the whole list. (Default is None)
        orderby : str, optional
            Name of the attribute the result list will be sorted by. (Default is 'name')
        reverse : bool, optional
            reverse the result list if set to true (Default is False)
        hidebroken : bool, optional
            Do not count broken stations (Default is False)

        Raises
        ------
        NotInitialized
            If not initialized
        """
        if not self.__intialized:
            raise NotInitialized("Please initialize the RadioBrowser.")

        reverse = str(reverse).lower()
        hidebroken = str(hidebroken).lower()

        params = {
            'order': orderby,
            'reverse': reverse,
            'hidebroken': hidebroken
        }

        if search:
            return await self.http.request(f"tags/{search}", params=params)
        else:
            return await self.http.request("tags/", params=params)

    async def stations(self, orderby: str = 'name', reverse: bool = False, offset=0, limit = 100000) -> List[dict]:
        """
        Get a full list of all stations.

        Parameters
        ----------
        orderby : str, optional
            Name of the attribute the result list will be sorted by. (Default is 'name')
        reverse : bool, optional
            reverse the result list if set to true (Default is False)
        offset : int, optional 
            Starting value of the result list from the database. For example, if you want to do paging on the server side. (default: 0)
        limit : int, optional
            Number of returned datarows (stations) starting with offset (default 100000)

        Raises
        ------
        NotInitialized
            If not initialized
        """
        if not self.__intialized:
            raise NotInitialized("Please initialize the RadioBrowser.")

        reverse = str(reverse).lower()


        params = {
            'order': orderby,
            'reverse': reverse,
            'offset': offset,
            'limit': limit
        }


        return await self.http.request("stations/", params=params) 


    async def search(self, **kwargs) -> List[dict]:
        """
        Advanced search.
        It will search for the station whose attribute
        contains the search term.
        See details at:

        https://de1.api.radio-browser.info/#Advanced_station_search
        
        Parameters
        ----------
        name : str, optional
            Name of the station.
        name_exact : bool, optional
            Only exact matches, otherwise all matches (default: False).
        country : str, optional 
            Country of the station.
        country_exact : bool, optional 
            Only exact matches, otherwise all matches (default: False).
        countrycode : str, optional 
            2-digit countrycode of the station (see ISO 3166-1 alpha-2)
        state : str, optional 
            State of the station.
        state_exact : bool, optional Only exact matches, otherwise all
            matches. (default: False)
        language : str, optional
            Language of the station.
        language_exact : bool, optional
            Only exact matches, otherwise all matches. (default: False)
        tag : str, optional 
            Tag of the station.
        tag_exact : bool, optional 
            Only exact matches, otherwise all matches. (default: False)
        tag_list : str, optional 
            A comma-separated list of tag.
        bitrate_min : int, optional 
            Minimum of kbps for bitrate field of stations in result. (default: 0)
        bitrate_max : int, optional
            Maximum of kbps for bitrate field of stations in result. (default: 1000000)
        order : str, optional
            The result list will be sorted by: name,
            url, homepage, favicon, tags, country, state, language, votes,
            codec, bitrate, lastcheckok, lastchecktime, clicktimestamp,
            clickcount, clicktrend, random
        reverse : bool, optional 
            Reverse the result list if set to true. (default: false)
        offset : int, optional 
            Starting value of the result list from the database. For example, if you want to do paging on the server side. (default: 0)
        limit : int, optional
            Number of returned datarows (stations) starting with offset (default 100000)
        hidebroken : bool, optional
            do list/not list broken stations.
            Note: Not documented in the "Advanced Station Search".

        Example:
        ```
        from aioradios import RadioBrowser
        rb = RadioBrowser()
        result = await rb.search(name='Radio Record', limit = 2)
        print(result[0])

        > {'changeuuid': '9629d8d7-0601-11e8-ae97-52543be04c81', 'stationuuid': '9629d8d4-0601-11e8-ae97-52543be04c81', 'name': 'Radio Record'...

        Raises
        ------
        NotInitialized
            If not initialized
        """
        if not self.__intialized:
            raise NotInitialized("Please initialize the RadioBrowser.")
        di = dict(kwargs)
        for key, value in di.items():
            if isinstance(value, bool):
                di[key] = str(value).lower() 

        return await self.http.request('stations/search', params = )

    async def search_by_uuid(self, uuids):
        """
        A list of radio stations that have an exact UUID match.

        Parameters
        ----------
        uuids : str
            comma-separated list of UUIDs

        Raises
        ------
        NotInitialized
            If not initialized
        """
        if not self.__intialized:
            raise NotInitialized("Please initialize the RadioBrowser.")

        return await self.http.request('stations/byuuid', params={'uuids':uuids})

    async def vote_for_station(self, uuid):
        """
        Increase the vote count for the station by one. 
        Can only be done by the same IP address for one station every 10 minutes. 
        If it works, the changed station will be returned as result

        Parameters
        ----------
        uuid : str
            The station uuid to vote for.
        
        Raises
        ------
        NotInitialized
            If not initialized
        """
        if not self.__intialized:
            raise NotInitialized("Please initialize the RadioBrowser.")
        return await self.http.request('vote/'+uuid)
