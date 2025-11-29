import json
import uuid

from loguru import logger

from janus.ODM.models import Stop, StopName


def add_stop(file_path: str) -> set[str]:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    stops = set()

    for row in data["tables"][0]["rows"][1:]:
        if row and row[0] != "Place":
            stops.add(row[0])

    logger.info("stops: {}".format(stops))
    return stops


def de_duplicate(stops: set[str]) -> set[str]:
    droplist = set()
    for stop in stops:
        result = Stop.find({"stop_names.name": stop}).to_list()
        # logger.info("result: {}".format(result))
        if result:
            logger.warning("duplicate stop {}".format(stop))
            droplist.add(stop)

    for stop in droplist:
        stops.discard(stop)

    return stops


if __name__ == "__main__":
    de_duplicate(add_stop("../../janus/output.json"))