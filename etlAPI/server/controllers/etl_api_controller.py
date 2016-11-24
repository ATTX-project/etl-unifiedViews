prefix = """
@base <http://helsinki.fi/library/> .
@prefix kaisa: <http://helsinki.fi/library/onto#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix sd: <http://www.w3.org/ns/sparql-service-description#> .
@prefix pwo: <http://purl.org/spar/pwo/> .
"""

static_workflow = """
kaisa:wf1
  a kaisa:Workflow ;
  dcterms:title "Acquisition and Mapping the VIRTA pubs data." ;
  dcterms:description "Workflow that uses VIRTA publication data in order to map titles and external identifiers for every publication and research fields."@en ;
  pwo:hasFirstStep kaisa:wf1_step1 ;
  pwo:hasStep
    kaisa:wf1_step2 ,
    kaisa:wf1_step1 ,
    kaisa:wf1_step3 ,
    kaisa:wf1_step4 .

kaisa:wf1_step1
  a kaisa:Step ;
  dcterms:title "VIRTA Publication Input Step" ;
  dcterms:description "DPU that gets the latest publication from VIRTA using the API."@en ;
  pwo:hasNextStep kaisa:wf1_step2 .

kaisa:wf1_step2
  a kaisa:Step ;
  dcterms:title "VIRTA Transformation Step" ;
  dcterms:description "DPU that transforms the VIRTA data into RDF format. At the same time it maps titles and external identifiers."@en ;
  pwo:hasNextStep kaisa:wf1_step3 .

kaisa:wf1_step3
  a kaisa:Step ;
  dcterms:title "Adding wf1 Metadata Step" ;
  dcterms:description "DPU that add necessary Metadata, to the specify provenance information."@en ;
  pwo:hasNextStep kaisa:wf1_step4 .

kaisa:wf1_step4
  a kaisa:Step ;
  dcterms:title "VIRTA Publication Output Step" ;
  dcterms:description "DPU that that contains the mapped data and writes it to the a file."@en .
"""

static_activity = """
kaisa:wf2_dataset1
  a kaisa:Dataset, sd:Dataset ;
  dcterms:title "VIRTA Publication Dataset" ;
  dcterms:description "National list of publication that are part of the official VIRTA collection."@en;
  dcterms:publisher "Ministry of Culture and Education" ;
  dcterms:source <http://virta.fi/data_dump.csv> ; # actual source is a CSV file.
  dcterms:license <http://creativecommons.org/licenses/by/4.0/> .

kaisa:wf2_dataset2
  a kaisa:Dataset, sd:Dataset ;
  dcterms:title "CRIS Publication Dataset" ;
  dcterms:description "National list of publication that are part of the official CRIS collection."@en;
  dcterms:publisher "Ministry of Culture and Education" ;
  dcterms:source <http://cris.fi/data_dump.csv> ; # actual source is a CSV file.
  dcterms:license <http://creativecommons.org/licenses/by/4.0/> .

kaisa:wf2_dataset3
  a kaisa:Dataset, sd:Dataset ;
  dcterms:title "Selected VIRTA Publication Data in RDF" ;
  dcterms:description "Dataset includes titles and external identifiers for every publication and research fields, see mapping steps for details"@en;
  dcterms:license <http://creativecommons.org/licenses/by/4.0/> . # license should be the same as original data

kaisa:activity2
  a prov:Activity , kaisa:WorkflowExecution ;
  prov:startedAtTime  "2016-11-17T13:02:10+02:00"^^xsd:dateTime ;
  prov:endedAtTime "2016-11-17T13:40:47+02:00"^^xsd:dateTime ;
  prov:qualifiedAssociation [
    a prov:Assocation ;
    prov:agent kaisa:ETL ;
    prov:hadPlan kaisa:wf2 ;
  ] ;
  prov:used kaisa:wf2_dataset1 ;
  prov:used kaisa:wf2_dataset2 ;
  prov:generated kaisa:wf2_dataset3 .
"""

def activity_get(modifiedSince = None):
    return prefix + static_activity

def activity_post():
    return 'Method Not Allowed!'

def workflow_get(modifiedSince = None):
    return prefix + static_workflow

def workflow_post():
    return 'Method Not Allowed!'
