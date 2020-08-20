import requests
import json
import itertools
from bs4 import BeautifulSoup


def dms2degLat(dms):
    """ https://en.wikipedia.org/wiki/ISO_6709 """
    days = int(dms[:2])
    mins = int(dms[2:4])
    secs = int(dms[4:] or 0)
    return dms2deg(days, mins, secs)


def dms2degLong(dms):
    """ https://en.wikipedia.org/wiki/ISO_6709 """
    days = int(dms[:3])
    mins = int(dms[3:5])
    secs = int(dms[5:] or 0)
    return dms2deg(days, mins, secs)


def dms2deg(days, mins, secs):
    """ https://stackoverflow.com/questions/33997361/how-to-convert-degree-minute-second-to-degree-decimal """
    return float(days) + float(mins)/60 + float(secs)/(60*60)


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
            utc_offset = list(utc_offset)
            utc_offset[0] = "-"
            utc_offset = "".join(utc_offset)

        ll = []

        for k, g in itertools.groupby(
                latlong, key=str.isdigit):

            l = ""
            if k:
                # it's a digit
                l = "".join(list(g))
            else:
                l = "".join(list(g))
                # it's a sign

            ll.append(l)

        lat = ll[1]
        long = ll[3]

        lat = dms2degLat(lat)
        long = dms2degLong(long)

        if ll[0] == "−":
            lat = -lat
        if ll[2] == "−":
            long = -long

        lat = format(lat, '.3f')
        long = format(long, '.3f')

        # convert from DMS to degrees
        # lat_deg

        out.append({
            "lat": lat,
            "long": long,
            "tz_name": tz_name,
            "utc_offset": utc_offset
        })

f = open('locs.json', 'w')
f.write(json.dumps(out))
f.close()
