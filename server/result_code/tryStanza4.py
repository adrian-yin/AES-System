from stanza.server import CoreNLPClient


ann = client.annotate(text)

# get the first sentence
sentence = ann.sentence[0]

# get the constituency parse of the first sentence
print('---')
print('constituency parse of first sentence')
constituency_parse = sentence.parseTree
print(constituency_parse)