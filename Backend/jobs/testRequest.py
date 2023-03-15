import requests

class Server:
    def __init__(self) -> None:
        self.headers = {"Content-Type": "application/json"}
        self.url = 'https://api.tarkov.dev/graphql'

    def runQuery(self,query):
        response:requests.post = requests.post(self.url, headers=self.headers,json={'query':query})

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Query failed to run by returning code of {}. {}".format(response.status_code,query))
        

new_query = """
{
    items(name: "m855a1") {
        id
        name
        shortName
        iconLink
        basePrice
    }
}
"""

