import os

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(
        os.environ['WEBSITE_RUN_FROM_PACKAGE'],
        status_code=200
    )
