import requests
import json
import itertools
from bs4 import BeautifulSoup

website_text = requests.get(
    "https://en.wikipedia.org/wiki/List_of_tz_database_time_zones").text

soup = BeautifulSoup(website_text, "html.parser")

table = soup.find('table', {'class': 'wikitable sortable'})

tbody = table.find('tbody')

tr_list = tbody.find_all('tr')
print(len(tr_list))


out = []

for tr in tr_list:
    # get cols 1, 2, 5
    td_ResultSet = tr.select('td')
    if len(td_ResultSet) > 5:
        latlong = td_ResultSet[1].decode_contents().strip()
        if len(latlong) < 6:
            continue
        tz_name = td_ResultSet[2].find("a").decode_contents().strip()
        utc_offset = td_ResultSet[5].find("a").decode_contents().strip()

        if utc_offset[0] == "−":
            utc_offset[0] = "-"

        ll = []

        for k, g in itertools.groupby(
                latlong, key=str.isdigit):

            l = ""
            if k:
                # it's a digit
                l = int("".join(list(g)))
            else:
                l = "".join(list(g))
                # it's a sign

            ll.append(l)

        lat = ll[1]
        if ll[0] == "−":
            lat = -lat
        long = ll[3]
        if ll[2] == "−":
            long = -long

        out.append({
            "lat": lat,
            "long": long,
            "tz_name": tz_name,
            "utc_offset": utc_offset
        })

f = open('locs.json', 'w')
f.write(json.dumps(out))
f.close()
