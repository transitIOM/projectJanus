import requests
from bs4 import BeautifulSoup
from loguru import logger


def get_routes():
    base_url = "https://bustimes.org/"
    response = requests.get(base_url + "operators/bus-vannin")
    soup = BeautifulSoup(response.content, "html.parser")
    routes = soup.find_all("strong", attrs={"class": "name is-short"})
    route_dict = dict()
    for route in routes:
        a_href = route.find_parent("a")["href"]
        url = str(base_url + a_href[1:])
        route_dict[route.text.strip('\n')] = url
    return route_dict


def get_stops(route_url):
    stop_list = []
    response = requests.get(route_url)
    soup = BeautifulSoup(response.content, "html.parser")

    try:
        stops = soup.find_all("h2", limit=2)[1].find_all_previous("th", attrs={"class": "stop-name"})
    except IndexError:
        stops = soup.find_all("th", attrs={"class": "stop-name"})

    for stop in stops:
        freedom = True
        cock = stop.parent.get("class")
        if cock == ["minor"]:
            freedom = False
        elif cock == ["minor od"]:
            continue
        timed = freedom
        stop_list.append((stop.text.strip('\n'), timed))
    return stop_list


def get_all_stops():
    routes = get_routes()
    length = len(routes)
    i = 0
    dict_all = dict()
    for route_name in routes:
        i = i + 1
        logger.info("%1 / %2 Getting stops for route: {}".format(route_name).replace("%1", str(i)).replace("%2", str(length)))
        url = routes[route_name]
        route_stops = get_stops(url)
        dict_all[route_name] = (url, route_stops)
    return dict_all


if __name__ == '__main__':
    all_stops = get_all_stops()
    print(all_stops)