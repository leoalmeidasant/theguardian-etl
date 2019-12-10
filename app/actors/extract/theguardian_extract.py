import logging

import requests


class Extract(object):
    @staticmethod
    def run(uri, payload):
        logging.info("Extract.run() - Getting data from The Guardian API")

        response = requests.get(uri, params=payload)
        pages = [response.json()["response"]["results"]]

        logging.info("Extract.run() - Page count: {}".format(response.json()["response"]["pages"]))

        if response.json()["response"]["pages"] <= 1:
            return pages
        else:
            page_count = response.json()["response"]["pages"]
            current_page = response.json()["response"]["currentPage"]
            while current_page < page_count:
                next_page = current_page + 1
                payload["page"] = next_page
                response = requests.get(uri, params=payload)
                pages.append(response.json()["response"]["results"])
                current_page = next_page

        return pages
