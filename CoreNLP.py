from pycorenlp import StanfordCoreNLP
import logging
logging.basicConfig(level=logging.DEBUG)

nlp = StanfordCoreNLP('http://localhost:9000')

sentences="76% Cabernet Sauvignon, 15% Merlot, 9% Cabernet Franc. Sexy wine. Red currant flavors. Power and elegance together. Tons of lush, decadent fruit. K&L's Ralph Sands adds: All of the above, with a powerful strike on the palate and great freshness!"

output = nlp.annotate(sentences, properties={
  'annotators': 'tokenize,ssplit,pos,depparse,parse',
  'outputFormat': 'json'
  })

for i,sentence in enumerate(output['sentences']):
    for token in sentence['tokens']:
        print(token['word'],end=' ')
    print ()
    constituency_tree = str(sentence['parse'])
    while '  ' in constituency_tree:
        constituency_tree=constituency_tree.replace('  ',' ')
    print (constituency_tree.replace('\r\n',''))
    print ()
