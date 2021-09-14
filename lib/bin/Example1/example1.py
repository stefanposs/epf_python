import os, sys
sys.path.append(os.getcwd())
import asyncio
import aiohttp
from jsonschema import Draft3Validator, Draft7Validator, Draft6Validator
from dotenv import load_dotenv
from pathlib import Path
from lib.models import *
from lib.services import *
from lib.infrastructure.azure import *
from lib.infrastructure.repository import *

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)


def deleteBlob():

    az = azBlobClient.AzBlobClient(
        conString=os.getenv('CONNECTION_STRING'),
    )
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        az.deleteBlob(
            fileName='iiii',
        )
    )


def createCosmosDbItem():
    az = azCosmosDbSqlClient.AzCosmosDbSqlClient(
        conString=os.getenv('COSMOSDB_CONNECTION_STRING'),
        containerName='FamilyContainer',
        databaseName='AzureSampleFamilyDatabase'
    )
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        az.databaseExist()
    )
    loop.run_until_complete(
        az.containerExist()
    )
    loop.run_until_complete(
        az.createItem(itemContent='{"name":"Hans", "lastName":"Maier", "meta": { "uuid":"2221212122"}}', itemId='2221212122')
    )

def cosmosDbItemExist():
    az = azCosmosDbSqlClient.AzCosmosDbSqlClient(
        conString=os.getenv('COSMOSDB_CONNECTION_STRING'),
        containerName='FamilyContainer',
        databaseName='AzureSampleFamilyDatabase'
    )
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(
        az.itemExist(itemId='2221212122')
    )
    print(str(res))

def deleteCosmosDbItem():
    az = azCosmosDbSqlClient.AzCosmosDbSqlClient(
        conString=os.getenv('COSMOSDB_CONNECTION_STRING'),
        containerName='FamilyContainer',
        databaseName='AzureSampleFamilyDatabase'
    )
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(
        az.deleteItemById(itemId='2221212122')
    )
    print(str(res))

def updateCosmosDbItem():
    az = azCosmosDbSqlClient.AzCosmosDbSqlClient(
        conString=os.getenv('COSMOSDB_CONNECTION_STRING'),
        containerName='FamilyContainer',
        databaseName='AzureSampleFamilyDatabase'
    )
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        az.databaseExist()
    )
    loop.run_until_complete(
        az.containerExist()
    )
    loop.run_until_complete(
        az.replaceItemById(itemContent='{"name":"Jörg", "lastName":"Koch", "meta": { "uuid":"2221212122"}}', itemId='2221212122')
    )

if __name__ == '__main__':
    log = log.Logging()
    import logging
    logging.info("jjj")
    # deleteBlob()
    createCosmosDbItem()
    cosmosDbItemExist()
    updateCosmosDbItem()
    deleteCosmosDbItem()
"""
    schema = {
    "type": "array",
    "items": {"enum": [1, 2, 3]},
    "maxItems": 2,
    }
    schema = {
        "$schema": "https://json-schema.org/schema#",

        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "email": {"type": "string"},
        },
        "required": ["email"]
    }
    print (Draft6Validator.check_schema(schema))
    v = Draft7Validator(schema)
    for error in sorted(v.iter_errors([2, 3, 4]), key=str):
        print(error.message)
"""