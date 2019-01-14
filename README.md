# Semantic Layer for the UK Biobank Cardiovascular Magnetic Resonance Quality Assessment

Image quality assessment is fundamental as it affects the level of confidence in any output obtained from image analysis. 
Clinical research imaging scans  do  not  often  come  with  an  explicit  evaluation  of  their  quality,  however
reports are written associated to the patient/volunteer scans. This rich free-text documentation has the potential to 
provide automatic image quality assessment if efficiently processed and structured. This work aims at showing how the use
of Semantic Web technology for structuring free-text documentation can provide
means for automatic image quality assessment. We aim to design and implement
a **semantic layer** and a **knowledge graph** for a special dataset, the annotations made in the context of the
UK Biobank Cardiac Cine MRI pilot study. This semantic layer in combination with the representation power of the knowledge graph will be a powerful tool to automatically infer or validate quality scores for clinical images and
efficiently query image databases based on quality information extracted from the
annotations. Our approach has the potential to be extended to broader projects and ultimately employed in the clinical setting.

## Source dependencies
- [Python 3](https://www.python.org/)
- [Owlready2](https://pypi.org/project/Owlready2/): pip install Owlready2
- [RDFLib](https://rdflib.readthedocs.io/en/stable/gettingstarted.html): pip install rdflib

## CMR-QA Ontology
- Current version ([v0.4.6](https://github.com/ernestojimenezruiz/CMR-QA-Semantic-Layer/blob/master/ontology/CMR-QA.owl), November, 2018): [OWL format](https://raw.githubusercontent.com/ernestojimenezruiz/CMR-QA-Semantic-Layer/master/ontology/CMR-QA.owl) 
- CMR-QA in [BioPortal](http://purl.bioontology.org/ontology/CMR-QA)
- Created with [Protégé Desktop](https://protege.stanford.edu/)

## References

- Valentina Carapella, Ernesto Jiménez-Ruiz. **A Knowledge Graph for the Quality Assessment of Cardiovascular Magnetic Resonance Imaging Data**. AI in Cardiac Imaging Conference 2019. ([Poster]())
- Valentina Carapella, Ernesto Jiménez-Ruiz, Elena Lukaschuk, Nay Aung, Kenneth Fung, José Miguel Paiva, Mihir Sanghvi, Stefan Neubauer, Steffen E. Petersen, Ian Horrocks, Stefan K. Piechnik:
**Towards the Semantic Enrichment of Free-Text Annotation of Image Quality Assessment for UK Biobank Cardiac Cine MRI Scans**. 
LABELS/DLMIA@MICCAI 2016: 238-248. ([PDF](https://www.cs.ox.ac.uk/files/8298/ukbb-labels-2016_id7.pdf))
- Ernesto Jiménez-Ruiz, Valentina Carapella, Elena Lukaschuk, Nay Aung, Kenneth Fung, José Miguel Paiva, Mihir Sanghvi, Stefan Neubauer, Steffen E. Petersen, Ian Horrocks, Stefan K. Piechnik:
**Towards the Creation of the Cardiovascular Magnetic Resonance Quality Assessment Ontology (CMR-QA)**. SWAT4LS 2016. ([PDF](http://ceur-ws.org/Vol-1795/paper22.pdf)) ([Slides](https://www.slideshare.net/ernestojimenezruiz/towards-the-creation-of-the-cardiovascular-magnetic-resonance-quality-assessment-ontology-cmrqa))
