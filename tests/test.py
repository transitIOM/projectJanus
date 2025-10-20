from janus.parser import stops

scraper = stops.busTimesScraper

class TestClass:
    def test_one():
        assert scraper.get_routes == True