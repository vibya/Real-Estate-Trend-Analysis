import requests
import xmltodict
import pandas as pd
import urllib
from urllib.parse import urlparse, urlunparse
from src.config import APIKEY_GSCHOOLS


class GreatSchoolsApi(object):
    """ A python interface into the Great Schools API
    """

    def __init__(self):

        self._base_url = "https://api.greatschools.org/"

    def browse_schools(self, state, city, school_type=None, school_level=None, sort=None, limit=None):

        # cast components
        state = state.upper()
        city = city.title().replace("-", "_").replace(" ", "-")

        # set components
        components = ["schools", state, city, school_type, school_level]

        # build call url
        url = self.build_url(self._base_url, components) + "?"

        # set parameters
        params = dict(key=APIKEY_GSCHOOLS)

        if sort:
            params["sort"] = sort
        if limit:
            params["limit"] = limit

        # get response
        response = self.request_url(url, params)

        # parse response xml
        data = response.content.decode('utf-8')
        data = xmltodict.parse(data)["schools"]["school"]

        return pd.DataFrame(data=data)

    def nearby_schools(self, state, zip=None, city=None, address=None, lat=None, lon=None,
                       school_type=None, school_level=None, radius=None, limit=None):
        # cast components
        state = state.upper()
        components = ["schools", "nearby"]

        # build call url
        url = self.build_url(self._base_url, components) + "?"

        # set parameters
        params = dict(key=APIKEY_GSCHOOLS, state=state)
        if zip:
            params["zip"] = zip
        if city:
            city = urllib.parse.quote_plus(f"{city.title()}")
            params["city"] = city
        if address:
            address = urllib.parse.quote_plus(f"{address.title()}")
            params["address"] = address
        if lat:
            params["lat"] = lat
        if lon:
            params["lon"] = lon
        if school_type:
            params["schoolType"] = school_type
        if school_level:
            params["levelCode"] = school_level
        if radius:
            params["radius"] = radius
        if limit:
            params["limit"] = limit

        # get response
        response = self.request_url(url, params)

        # parse response xml
        data = response.content.decode('utf-8')
        data = xmltodict.parse(data)["schools"]["school"]
        return pd.DataFrame(data)

    def school_profile(self):
        pass

    def school_test_score(self, state, gsid):

        # cast components
        state = state.upper()
        components = ["school", "tests", state, gsid]

        # build call url
        url = self.build_url(self._base_url, components) + "?"

        # set parameters
        params = dict(key=APIKEY_GSCHOOLS)
        # get response
        response = self.request_url(url, params)
        # parse response xml
        data = response.content.decode('utf-8')
        data = xmltodict.parse(data)

        return data["testResults"]

    def build_url(self, url, components):

        # break url into constituent parts
        (scheme, netloc, path, params, query, fragment) = urlparse(url)
        if components:
            # filter components with None values
            c = [component for component in components if component]
            if not path.endswith("/"):
                path += "/"
            path += "/".join(c)
        # Return the rebuilt URL
        return urlunparse((scheme, netloc, path, params, query, fragment))

    def request_url(self, url, params):

        try:
            response = requests.get(url, params=params)
        except requests.RequestException:
            pass

        return response


gsp = GreatSchoolsApi()

# get schools in Austin
state = "tx"
city = "austin"
school_type = "public"
school_level = "high-schools"
schools_df = gsp.browse_schools(state, city, school_type, school_level, limit=10)

# get school score
state = "tx"
gsid = schools_df["gsId"][0]
school_score = gsp.school_test_score(state, gsid)

# find nearby schools
state = "tx"
zip = 78703
radius = 1

nearbyschools_df = gsp.nearby_schools(state, zip=zip, radius=radius)