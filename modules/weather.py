import re
import urllib
from xml.dom import minidom

def __init__(self):
    print "Weather Initialized!"

def say(user, channel, msg):
    regexp = re.compile('^weather ([\w]+)', re.IGNORECASE)
    print "user %s channel %s msg %s" % (user, channel, msg)
    if regexp.match(msg):
        city = re.findall(regexp,msg)[0].upper()
        print "Matched weather!"
        return get_weather_string(city)

def get_weather_string(city):
    string = "";
    try:
        url = "http://w1.weather.gov/xml/current_obs/%s.xml" % city
        print "Fetching %s" % url
        data = urllib.urlopen(url)
        xmldoc = minidom.parse(data)
    except:
        string = "Error fetching data from NOAA"
        return string

    conditions = {}
    obs = xmldoc.getElementsByTagName('temperature_string')[0]
    conditions['temp'] = obs.childNodes[0].data
    obs = xmldoc.getElementsByTagName('location')[0]
    conditions['location'] = obs.childNodes[0].data
    obs = xmldoc.getElementsByTagName('observation_time')[0]
    conditions['observationtime'] = obs.childNodes[0].data
    obs = xmldoc.getElementsByTagName('relative_humidity')[0]
    conditions['humidity'] = obs.childNodes[0].data
    obs = xmldoc.getElementsByTagName('wind_string')[0]
    conditions['wind'] = obs.childNodes[0].data
    obs = xmldoc.getElementsByTagName('dewpoint_string')[0]
    conditions['dew'] = obs.childNodes[0].data
    try:
        obs = xmldoc.getElementsByTagName('heat_index_string')[0]
        conditions['heat'] = obs.childNodes[0].data
    except:
        conditions['heat'] = ""
    obs = xmldoc.getElementsByTagName('visibility_mi')[0]
    conditions['vis'] = obs.childNodes[0].data
    say = "Current conditions for %(location)s %(observationtime)s. \
%(temp)s %(humidity)s%% Humidity. Wind: %(wind)s \
Dewpoint: %(dew)s Heat Index %(heat)s Visibility: \
%(vis)s mi" % conditions
    return say
