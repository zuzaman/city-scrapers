import pytest

from tests.utils import file_response
from documenters_aggregator.spiders.ccc import CccSpider

def test_tests():
    print('Please write some tests for this spider or at least disable this one.')
    assert False


"""
Uncomment below
"""

# test_response = file_response('files/ccc.html')
# spider = CccSpider()
# parsed_items = [item for item in spider.parse(test_response) if isinstance(item, dict)]


# def test_name():
    # assert parsed_items[0]['name'] == 'EXPECTED NAME'


# def test_description():
    # assert parsed_items[0]['description'] == 'EXPECTED DESCRIPTION'


# def test_start_time():
    # assert parsed_items[0]['start_time'] == 'EXPECTED START DATE AND TIME'


# def test_end_time():
    # assert parsed_items[0]['end_time'] == 'EXPECTED END DATE AND TIME'


# def test_id():
    # assert parsed_items[0]['id'] == 'EXPECTED ID'


# @pytest.mark.parametrize('item', parsed_items)
# def test_all_day(item):
    # assert item['all_day'] is False


# @pytest.mark.parametrize('item', parsed_items)
# def test_classification(item):
    # assert item['classification'] is None


# @pytest.mark.parametrize('item', parsed_items)
# def test_status(item):
    # assert item['status'] == 'tentative'


# def test_location():
    # assert parsed_items[0]['location'] == {
        # 'url': 'EXPECTED URL',
        # 'name': 'EXPECTED NAME',
        # 'coordinates': {
            # 'latitude': 'EXPECTED LATITUDE',
            # 'longitude': 'EXPECTED LONGITUDE',
        # },
    # }

# @pytest.mark.parametrize('item', parsed_items)
# def test__type(item):
    # assert parsed_items[0]['_type'] == 'event'