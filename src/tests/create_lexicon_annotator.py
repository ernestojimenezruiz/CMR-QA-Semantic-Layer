from lexicon.lexicon_ontology import ExtractLexiconOntology
from lexicon.store_lexicon import StoreLexiconOntology


folder_ontos="/home/ejimenez-ruiz/Documents/UK_BioBank/CMR-QA-ontology"
uri_onto="http://www.semanticweb.org/ukbiobank/ocmr_isg/CMR-QA"
#uri_onto="http://www.semanticweb.org/ejimenez-ruiz/ontologies/2018/test"

extractor = ExtractLexiconOntology(folder_ontos, uri_onto) 
extractor.extractLexicon()

fileLex = 'cmr-qa.lex'

writer = StoreLexiconOntology(extractor.getLexiconForClasses(), extractor.getSemGroupsForClasses(), fileLex)