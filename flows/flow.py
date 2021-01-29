from datetime import timedelta
from prefect import Flow
from prefect import task

from tasks.pokemontasks import ExtractPokemon, TransformPokemon, LoadPokemon
from utils.config import kubernetes_run, azure_store

extract_pokemon = ExtractPokemon()
transform_pokemon = TransformPokemon()
load_pokemon = LoadPokemon()


with Flow("PokeFlow", run_config=kubernetes_run ,storage=azure_store) as flow:
         extracted_pokemon = extract_pokemon()
         transformed_pokemon = transform_pokemon.map(extracted_pokemon['results'])
         loaded_pokemon = load_pokemon(transformed_pokemon)
