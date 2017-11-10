# -*- coding: utf-8 -*-
"""
All spiders should yield data shaped according to the Open Civic Data
specification (http://docs.opencivicdata.org/en/latest/data/event.html).
"""
import scrapy
import requests
import json
import datetime as dt


class CityclerkSpider(scrapy.Spider):
    name = 'cityclerk'
    long_name = "Chicago City Clerk"
    ocd_url = 'https://ocd.datamade.us/'
    ocd_tp = 'events/?'
    ocd_d = 'start_date__gt=' + str(dt.date.today()) + '&'
    ocd_srt = 'sort=start_date&'
    ocd_jur = 'jurisdiction=ocd-jurisdiction/'
    ocd_loc = 'country:us/state:il/place:chicago/government'

    allowed_domains = [ocd_url]
    start_urls = [ocd_url + ocd_tp + ocd_d + ocd_srt + ocd_jur + ocd_loc]

    def parse(self, response):
        """
        This is not a traditional spider, rather, this is a glorified wrapper
        around the Open Civic Data API to which the Chicago City Clerk
        Legistar site info has already been scraped.
        We will attempt to return all events that have been uploaded in the
        future, i.e. past today's date.
        """
        data = json.loads(response.text)

        for item in data['results']:
            yield {
                '_type': 'event',
                'id': item['id'],
                'name': item['name'],
                'description': item['description'],
                'classification': item['classification'],
                'start_time': item['start_date'],
                'end_time': item['end_date'],
                'all_day': item['all_day'],
                'status': item['status'],
                'location': self._parse_location(item),
                'sources': self._parse_sources(item)
            }

        # self._parse_next(response) yields more (responses to parse
        max_page = data['meta']['max_page']
        page = data['meta']['page']
        while page < max_page:
            yield self._parse_next(response, page)

    def _parse_next(self, response, pgnum):
        """
        Get next page.
        """
        pgnum = pgnum + 1
        next_url = self.start_urls[0] + '&page=' + pgnum
        return scrapy.Request(next_url, callback=self.parse, dont_filter=True)

    def _parse_location(self, item):
        """
        Grab location from the event detail page.
        """
        pgurl = self.ocd_url + item['id']
        e_pg = requests.get(pgurl)
        if e_pg.status_code != 200:
            loc = {'url': '',
                   'name': '',
                   'coordinates': None,
                   }
        else:
            d_pg = e_pg.json()
            loc = d_pg['location']
        return loc

    def _parse_sources(self, item):
        """
        Grab sources from event detail page.
        """
        pgurl = self.ocd_url + item['id']
        e_pg = requests.get(pgurl)
        if e_pg.status_code != 200:
            sourcelist = [{'note': 'ocd-api', 'url': pgurl}]
        else:
            d_pg = e_pg.json()
            sourcelist = d_pg['sources']
            sourcelist.append({'note': 'ocd-api', 'url': pgurl})
            sourcelist[0], sourcelist[2] = sourcelist[2], sourcelist[0]
        return sourcelist
