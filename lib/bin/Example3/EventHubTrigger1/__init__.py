import asyncio
import json
import sys
import uuid
from os import path
from typing import List


sys.path.append(path.abspath('../../../'))
from lib.models.base.baseEvent import BaseEvent
from lib.infrastructure.repository.bronzeEventLayerRepository import BronzeEventLayerRepository
from lib.infrastructure.azure.azBlobClient import AzBlobClient
from lib.services.bronzeEventLayer import BronzeEventLayer
from lib.services.log import Log

import azure.functions as func

"""
parameter file
"""
from . import params


def getLabel() -> str:
    return str(
        params.params['domain'] + '.' + params.params['buildingBlock'] + '.' + params.params['aggregate'] + '.' + params.params['mode'] + '.' +
        params.params['env'])


"""
main
"""


async def main(events: List[func.EventHubEvent]):
    """ Initialize """
    global bronzeEventLayer
    global silerEventLayer
    global goldEventLayer
    global storage
    global logging
    global bronzeProcessLayerRepository

    logging = Log()

    logging.info(getLabel(), 'Initialize')

    """ Initialize: BronzeEventLayer """
    if params.params['layer']['bronzeEventLayer']['inputSchema'] is None:
        script_dir = path.dirname(__file__)
        with open(path.join(script_dir, params.params['layer']['bronzeEventLayer']['inputSchemaFilePath']), 'r') as json_file:
            params.params['layer']['bronzeEventLayer']['inputSchema'] = json.load(json_file)

    storage = AzBlobClient(
        conString=params.params['layer']['bronzeEventLayer']['storage']['azure']['blob']['conString']
    )
    bronzeProcessLayerRepository = BronzeEventLayerRepository(
        azBlobClient=storage,
    )
    bronzeEventLayer = BronzeEventLayer(
        inputSchema=params.params['layer']['bronzeEventLayer']['inputSchema'],
        outputSchema=params.params['layer']['bronzeEventLayer']['inputSchema'],
        processLayerRepository=bronzeProcessLayerRepository
    )
    """ Initialize: SilverEventLayer """

    """ Initialize: GoldEventLayer """

    for item in events:
        """ Procesing """
        itemBody = json.loads(item.get_body().decode('utf-8'))
        e = BaseEvent(data=itemBody['data'], meta=itemBody['meta'])
        """ Procesing: BronzeEventLayer """
        """ Procesing: BronzeEventLayer checking input """
        # bronzeEventLayer.processed(event=e)
        if bronzeEventLayer.isInputValid(inputEvent=e):
            e.meta.uuid = str(uuid.uuid4())
            #e.meta.layer = dict(BaseLayer(name=__name__, entryTimeStampUtc='', message='valid'))

            logging.info(
                getLabel(),
                'event: ' + str(e.json()) + ',  ' + 'Event input is valid'
            )
            """ Procesing: BronzeEventLayer store and process """
            try:
                await bronzeEventLayer.processed(event=e)
                logging.info(
                    getLabel(),
                    'event: ' + str(e.meta.uuid) + ',  ' + 'Event is processed and stored'
                )
            except Exception as err:
                logging.error(
                    getLabel(),
                    'event: ' + str(e.meta.uuid) + ',  ' + 'Event cannot processed and stored'
                )
        else:
            logging.error(
                getLabel(),
                'event: ' + str(e.meta.uuid) + ', ' + 'Event is not valid'
            )

        """ Procesing: SilverEventLayer """
        """ Procesing: SilverEventLayer check input """
        """ Procesing: SilverEventLayer store and process """
        """ Procesing: GoldEventLayer """
        """ Procesing: GoldEventLayer check input """
        """ Procesing: GoldEventLayer store and process """
