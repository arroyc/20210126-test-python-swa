import logging
import requests
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    response = requests.get("https://raw.githubusercontent.com/anthonychu/python-func-async/master/host.json")
    return func.HttpResponse(response.text)