from json_connector import *

from xml_json_factory.xml_connector import *


def connection_factory(filepath):

    if filepath.endswith('json'):

        connector = JSONConnector

    elif filepath.endswith('xml'):

        connector = XMLConnector

    else:

        raise ValueError('Cannot connect to {}'.format(filepath))

    return connector(filepath)


# wrapper for above factory
def connect_to(filepath):

    factory = None

    try:

        factory = connection_factory(filepath)

    except ValueError as ve:

        print(ve)

    return factory
