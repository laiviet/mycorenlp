import random
from multiprocessing import Pool
from mycorenlp.client import CoreNLPClient

START_PORT = 9000
END_PORT = 9009
DEFAULT_ANNOTATORS = "tokenize ssplit lemma pos ner depparse".split()
DEFAULT_PROPERTIES = {}


clients = [CoreNLPClient(start_server=True,
                         endpoint='http://localhost:{}'.format(port),
                         thread=2,
                         annotators=DEFAULT_ANNOTATORS,
                         properties=DEFAULT_PROPERTIES) for port in range(START_PORT, END_PORT+1)]


def annotate(text, annotators=None, output_format=None, properties=None):
    client = clients[random.randint(0, END_PORT-START_PORT)]
    result = client.annotate(text=text,
                             annotators=annotators,
                             output_format=output_format,
                             properties=properties)
    return result


class MultipleCoreNLPClient():
    """
    A wrapper client to multiple NLP server
    """

    def __init__(self):
        super(MultipleCoreNLPClient, self).__init__()

    def annotate(self, texts, ):
        p = Pool(10)
        results = p.map(annotate, texts)
        return results
