import json
import sys
from os import path
from typing import List

sys.path.append(path.abspath('../../../'))
from lib.models.base import baseEvent
from lib.infrastructure.repository import bronzeEventLayerRepository
from lib.infrastructure.azure import azBlobClient
from lib.services import bronzeEventLayer, log

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


def main(events: List[func.EventHubEvent]):
    """ Initialize """
    global broEventLayer
    global silEventLayer
    global golEventLayer
    global storage
    global logging

    logging = log.Log()

    logging.info(getLabel(), 'Initialize')

    """ Initialize: BronzeEventLayer """
    if params.params['layer']['bronzeEventLayer']['inputSchema'] is None:
        script_dir = path.dirname(__file__)
        with open(path.join(script_dir, params.params['layer']['bronzeEventLayer']['inputSchemaFilePath']), 'r') as json_file:
            params.params['layer']['bronzeEventLayer']['inputSchema'] = json.load(json_file)

    storage = azBlobClient.AzBlobClient(
        conString=params.params['layer']['bronzeEventLayer']['storage']['azure']['blob']['conString']
    )

    broEventLayer = bronzeEventLayer.BronzeEventLayer(
        inputSchema=params.params['layer']['bronzeEventLayer']['inputSchema'],
        outputSchema=params.params['layer']['bronzeEventLayer']['inputSchema'],
        processLayerRepository=bronzeEventLayerRepository.BronzeEventLayerRepository(
            azBlobClient=storage,
        )
    )
    """ Initialize: SilverEventLayer """

    """ Initialize: GoldEventLayer """

    for item in events:
        """ Procesing """
        itemBody = json.loads(item.get_body().decode('utf-8'))
        e = baseEvent.BaseEvent(data=itemBody['data'], meta=itemBody['meta'])
        """ Procesing: BronzeEventLayer """
        """ Procesing: BronzeEventLayer checking input """
        if broEventLayer.isInputValid(inputEvent=e):
            logging.info(
                getLabel(),
                'event: ' + str(e.meta.uuid) + '  ' + ' Event input is valid'
            )
            pass
        """ Procesing: BronzeEventLayer store and process """

        """ Procesing: SilverEventLayer """
        """ Procesing: SilverEventLayer check input """
        """ Procesing: SilverEventLayer store and process """
        """ Procesing: GoldEventLayer """
        """ Procesing: GoldEventLayer check input """
        """ Procesing: GoldEventLayer store and process """
