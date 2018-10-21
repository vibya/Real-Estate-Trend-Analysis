import quandl
import pandas as pd
from itertools import product
from pprint import pprint
from uszipcode import ZipcodeSearchEngine


def get_quandl_code(area_category, area_code, indicator_code):
    return f"ZILLOW/{area_category}{area_code}_{indicator_code}"


# init. an instance of ZipcodeSearchEngine
search = ZipcodeSearchEngine()

# define quandl api key
API_KEY = "XL_c6FZRjuz6WYRTJB_a"

# set cities to query
cities_states = [dict(state="Texas", city="Austin"),
                 dict(state="Texas", city="Huston"),
                 dict(state="Texas", city="Dallas")]

# get zip codes per query city
df = pd.DataFrame()
index = 0
for city_state in cities_states:
    zip_codes = search.by_city_and_state(state=city_state["state"],
                                         city=city_state["city"],
                                         returns=200)
    for zip_code in zip_codes:
        df = df.append(pd.DataFrame(zip_code.to_dict(), index=[index]))
        index += 1

zip_code = "78739"
area_category = "Z"
area_code = zip_code

# set quandl api key
quandl.ApiConfig.api_key = API_KEY

# set the indicator code to query
indicator_code = "ZHVIAH"
# get quandl code to query
quandl_code = get_quandl_code(area_category, area_code, indicator_code)
# get housing indicator
data = quandl.get(quandl_code, start_date="1800-01-01", end_date="2018-04-30")
pprint(data)
