from flask import Flask, request
from markupsafe import escape
import requests



class Server:
    app = Flask(__name__)
    def __init__(self) -> None:
        self.headers = {"Content-Type": "application/json"}
        self.url = 'https://api.tarkov.dev/graphql'

    
    @app.route('/')
    def queryEndpoint():
        item = request.args.get("item","m855a1")
        new_query = "{ items(name:" + r'"' + item + r'"' + " ) { id name shortName iconLink basePrice } }"
        response = Server.runQuery(new_query)
        responseName = ""
        try:
            responseName = response["data"]["items"][0]["name"]
        except:
            pass
        return response


    @staticmethod
    def runQuery(query):
        url = 'https://api.tarkov.dev/graphql'
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, headers=headers, json={'query': query})
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Query failed to run by returning code of {}. {}".format(response.status_code, query))

