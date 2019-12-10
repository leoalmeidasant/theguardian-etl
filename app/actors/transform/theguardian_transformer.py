import logging
from datetime import timezone, datetime


class Transform(object):

    @staticmethod
    def run(pages):

        rows = []
        logging.info("Transform.run() - Building dict with required fields and adding extractTime")
        for page in pages:
            for row in page:
                tr_row = dict(
                    webUrl=row["webUrl"],
                    webPublicationDate=row["webPublicationDate"],
                    webTitle=row["webTitle"],
                    sectionName=row["sectionName"],
                    apiUrl=row["apiUrl"],
                    id=row["id"],
                    isHosted=row["isHosted"],
                    sectionId=row["sectionId"],
                    type=row["type"],
                    extractTime=int(datetime.now(tz=timezone.utc).timestamp() * 1000)
                )
                rows.append(tr_row)

        return rows
