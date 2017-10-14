from pycorenlp import StanfordCoreNLP
import logging
logging.basicConfig(level=logging.DEBUG)

nlp = StanfordCoreNLP('http://localhost:9000')
sentence='put your text here.'

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
