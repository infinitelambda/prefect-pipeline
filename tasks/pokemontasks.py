import requests
import prefect
from prefect import Task

class ExtractPokemon(Task):
    def run(self, **kwargs):
        logger = prefect.context.get("logger")
        url = "https://pokeapi.co/api/v2/pokemon?limit=151"
        response = requests.get(url)
        if response.ok: 
            return response.json()
        logger.warning(
            "Could not load pokemon list! Error {}".format(response.status_code)
        )
        return {"results": []}


class TransformPokemon(Task):
    def run(self, pokemon):
        logger = prefect.context.get("logger")
        url = pokemon["url"]
        name = pokemon["name"].title()
        logger.info("Getting {} from {}".format(name, url))
        response = requests.get(url)
        if response.ok:
            return response.json()
        logger.warning(
            "Could not load pokemon {}! Error {}".format(name, response.status_code)
        )
        return {} 
        
        
class LoadPokemon(Task):
    def run(self, pokemon):
        logger = prefect.context.get("logger")
        logger.info(len(pokemon))

