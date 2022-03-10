

class Mappings_generator:
    def __init__(self, file_path, mappings_path):
        self.file_path = '"' + file_path + '"'
        self.mappings_path = mappings_path


    def generate_mappings(self):
        """
        Generate the mappings file
        """
        # Generate the mappings file
        with open('Repositories/mappings' + self.mappings_path + '/map.rml.ttl', 'w') as map_file:
            map_file.write("""@prefix rr: <http://www.w3.org/ns/r2rml#> .
@prefix rml: <http://semweb.mmlab.be/ns/rml#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix ql: <http://semweb.mmlab.be/ns/ql#> .
@prefix map: <http://mapping.example.com/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix sd: <http://www.w3.org/ns/sparql-service-description#> .
@prefix time: <http://www.w3.org/2006/time#> .
@prefix process: <https://cogito.iot.linkeddata.es/def/process#> .
@prefix resource: <https://cogito.iot.linkeddata.es/def/resource#> .
@prefix const: <https://cogito.iot.linkeddata.es/def/construction#> .
@prefix geo: <http://www.w3.org/2003/01/geo/wgs84_pos#> .
@prefix s4city: <https://saref.etsi.org/saref4city#> .
@prefix saref: <https://saref.etsi.org/core#> .
@prefix data: <https://data.cogito.iot.linkeddata.es/resources/> .

map:jc_000 rr:child "TaskUID" ;
	rr:parent "UID" .

map:map_assignment_000 rml:logicalSource map:source_007 ;
	rdf:type rr:TriplesMap ;
	rdfs:label "assignment" ;
	rr:predicateObjectMap map:pom_033, map:pom_034, map:pom_035, map:pom_036, map:pom_037, map:pom_038, map:pom_039 ;
	rr:subjectMap map:s_007 .

map:map_cost_000 rml:logicalSource map:source_001 ;
	rdf:type rr:TriplesMap ;
	rdfs:label "cost" ;
	rr:predicateObjectMap map:pom_008, map:pom_009, map:pom_010 ;
	rr:subjectMap map:s_001 .

map:map_cost_assignment_000 rml:logicalSource map:source_003 ;
	rdf:type rr:TriplesMap ;
	rdfs:label "cost_assignment" ;
	rr:predicateObjectMap map:pom_013, map:pom_014 ;
	rr:subjectMap map:s_003 .

map:map_cost_task_000 rml:logicalSource map:source_002 ;
	rdf:type rr:TriplesMap ;
	rdfs:label "cost_task" ;
	rr:predicateObjectMap map:pom_011, map:pom_012 ;
	rr:subjectMap map:s_002 .

map:map_instant_end_assignment_000 rml:logicalSource map:source_016 ;
	rdf:type rr:TriplesMap ;
	rdfs:label "instant_end_assignment" ;
	rr:predicateObjectMap map:pom_059, map:pom_060 ;
	rr:subjectMap map:s_016 .

map:map_instant_end_project_000 rml:logicalSource map:source_010 ;
	rdf:type rr:TriplesMap ;
	rdfs:label "instant_end_project" ;
	rr:predicateObjectMap map:pom_045, map:pom_046 ;
	rr:subjectMap map:s_010 .

map:map_instant_end_task_000 rml:logicalSource map:source_013 ;
	rdf:type rr:TriplesMap ;
	rdfs:label "instant_end_task" ;
	rr:predicateObjectMap map:pom_052, map:pom_053 ;
	rr:subjectMap map:s_013 .

map:map_instant_start_assignment_000 rml:logicalSource map:source_015 ;
	rdf:type rr:TriplesMap ;
	rdfs:label "instant_start_assignment" ;
	rr:predicateObjectMap map:pom_057, map:pom_058 ;
	rr:subjectMap map:s_015 .

map:map_instant_start_project_000 rml:logicalSource map:source_009 ;
	rdf:type rr:TriplesMap ;
	rdfs:label "instant_start_project" ;
	rr:predicateObjectMap map:pom_043, map:pom_044 ;
	rr:subjectMap map:s_009 .

map:map_instant_start_task_000 rml:logicalSource map:source_012 ;
	rdf:type rr:TriplesMap ;
	rdfs:label "instant_start_task" ;
	rr:predicateObjectMap map:pom_050, map:pom_051 ;
	rr:subjectMap map:s_012 .

map:map_interval_assignment_000 rml:logicalSource map:source_014 ;
	rdf:type rr:TriplesMap ;
	rdfs:label "interval_assignment" ;
	rr:predicateObjectMap map:pom_054, map:pom_055, map:pom_056 ;
	rr:subjectMap map:s_014 .

map:map_interval_project_000 rml:logicalSource map:source_008 ;
	rdf:type rr:TriplesMap ;
	rdfs:label "interval_project" ;
	rr:predicateObjectMap map:pom_040, map:pom_041, map:pom_042 ;
	rr:subjectMap map:s_008 .

map:map_interval_task_000 rml:logicalSource map:source_011 ;
	rdf:type rr:TriplesMap ;
	rdfs:label "interval_task" ;
	rr:predicateObjectMap map:pom_047, map:pom_048, map:pom_049 ;
	rr:subjectMap map:s_011 .

map:map_project_000 rml:logicalSource map:source_000 ;
	rdf:type rr:TriplesMap ;
	rdfs:label "project" ;
	rr:predicateObjectMap map:pom_000, map:pom_001, map:pom_002, map:pom_003, map:pom_004, map:pom_005, map:pom_006, map:pom_007 ;
	rr:subjectMap map:s_000 .

map:map_resource_000 rml:logicalSource map:source_006 ;
	rdf:type rr:TriplesMap ;
	rdfs:label "resource" ;
	rr:predicateObjectMap map:pom_028, map:pom_029, map:pom_030, map:pom_031, map:pom_032 ;
	rr:subjectMap map:s_006 .

map:map_task_000 rml:logicalSource map:source_005 ;
	rdf:type rr:TriplesMap ;
	rdfs:label "task" ;
	rr:predicateObjectMap map:pom_018, map:pom_019, map:pom_020, map:pom_021, map:pom_022, map:pom_023, map:pom_024, map:pom_025, map:pom_026, map:pom_027 ;
	rr:subjectMap map:s_005 .

map:map_unitOfCurrency_000 rml:logicalSource map:source_004 ;
	rdf:type rr:TriplesMap ;
	rdfs:label "unitOfCurrency" ;
	rr:predicateObjectMap map:pom_015, map:pom_016, map:pom_017 ;
	rr:subjectMap map:s_004 .

map:om_000 rdf:type rr:ObjectMap ;
	rr:constant "https://cogito.iot.linkeddata.es/def/construction#Project" ;
	rr:termType rr:IRI .

map:om_001 rml:reference "GUID" ;
	rdf:type rr:ObjectMap ;
	rr:termType rr:Literal .

map:om_002 rml:reference "Name" ;
	rdf:type rr:ObjectMap ;
	rr:datatype xsd:string ;
	rr:termType rr:Literal .

map:om_003 rml:reference "CreationDate" ;
	rdf:type rr:ObjectMap ;
	rr:datatype xsd:dateTime ;
	rr:termType rr:Literal .

map:om_004 rdf:type rr:ObjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources/cost/{GUID}" ;
	rr:termType rr:Literal .

map:om_005 rdf:type rr:ObjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources/interval/{GUID}" ;
	rr:termType rr:Literal .

map:om_006 rdf:type rr:ObjectMap ;
	rr:parentTriplesMap map:map_task_000 .

map:om_007 rdf:type rr:ObjectMap ;
	rr:parentTriplesMap map:map_resource_000 .

map:om_008 rdf:type rr:ObjectMap ;
	rr:constant "https://cogito.iot.linkeddata.es/def/process#Cost" ;
	rr:termType rr:IRI .

map:om_009 rml:reference "CurrencyDigits" ;
	rdf:type rr:ObjectMap ;
	rr:datatype xsd:float ;
	rr:termType rr:Literal .

map:om_010 rdf:type rr:ObjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources/unitOfCurrency/{GUID}" ;
	rr:termType rr:Literal .

map:om_011 rdf:type rr:ObjectMap ;
	rr:constant "https://cogito.iot.linkeddata.es/def/process#Cost" ;
	rr:termType rr:IRI .

map:om_012 rml:reference "Cost" ;
	rdf:type rr:ObjectMap ;
	rr:datatype xsd:float ;
	rr:termType rr:Literal .

map:om_013 rdf:type rr:ObjectMap ;
	rr:constant "https://cogito.iot.linkeddata.es/def/process#Cost" ;
	rr:termType rr:IRI .

map:om_014 rml:reference "Cost" ;
	rdf:type rr:ObjectMap ;
	rr:datatype xsd:float ;
	rr:termType rr:Literal .

map:om_015 rdf:type rr:ObjectMap ;
	rr:constant "https://cogito.iot.linkeddata.es/def/process#UnitOfCurrency" ;
	rr:termType rr:IRI .

map:om_016 rml:reference "CurrencyCode" ;
	rdf:type rr:ObjectMap ;
	rr:termType rr:Literal .

map:om_017 rml:reference "CurrencySymbol" ;
	rdf:type rr:ObjectMap ;
	rr:termType rr:Literal .

map:om_018 rdf:type rr:ObjectMap ;
	rr:constant "https://cogito.iot.linkeddata.es/def/process#Task" ;
	rr:termType rr:IRI .

map:om_019 rml:reference "GUID" ;
	rdf:type rr:ObjectMap ;
	rr:termType rr:Literal .

map:om_020 rml:reference "UID" ;
	rdf:type rr:ObjectMap ;
	rr:termType rr:Literal .

map:om_021 rml:reference "Name" ;
	rdf:type rr:ObjectMap ;
	rr:datatype xsd:string ;
	rr:termType rr:Literal .

map:om_022 rml:reference "CreateDate" ;
	rdf:type rr:ObjectMap ;
	rr:datatype xsd:dateTime ;
	rr:termType rr:Literal .

map:om_023 rdf:type rr:ObjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources/interval/{GUID}" ;
	rr:termType rr:Literal .

map:om_024 rml:reference "Priority" ;
	rdf:type rr:ObjectMap ;
	rr:datatype xsd:integer ;
	rr:termType rr:Literal .

map:om_025 rml:reference "RemainingWork" ;
	rdf:type rr:ObjectMap ;
	rr:datatype xsd:string ;
	rr:termType rr:Literal .

map:om_026 rml:reference "ActualWork" ;
	rdf:type rr:ObjectMap ;
	rr:datatype xsd:string ;
	rr:termType rr:Literal .

map:om_027 rdf:type rr:ObjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources/cost/{GUID}" ;
	rr:termType rr:Literal .

map:om_028 rdf:type rr:ObjectMap ;
	rr:constant "https://cogito.iot.linkeddata.es/def/resource#Resource" ;
	rr:termType rr:IRI .

map:om_029 rml:reference "GUID" ;
	rdf:type rr:ObjectMap ;
	rr:termType rr:Literal .

map:om_030 rml:reference "UID" ;
	rdf:type rr:ObjectMap ;
	rr:termType rr:Literal .

map:om_031 rml:reference "CreationDate" ;
	rdf:type rr:ObjectMap ;
	rr:datatype xsd:dateTime ;
	rr:termType rr:Literal .

map:om_032 rdf:type rr:ObjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources/resourceType/{Type}" ;
	rr:termType rr:Literal .

map:om_033 rdf:type rr:ObjectMap ;
	rr:constant "https://cogito.iot.linkeddata.es/def/resource#Assignment" ;
	rr:termType rr:IRI .

map:om_034 rml:reference "GUID" ;
	rdf:type rr:ObjectMap ;
	rr:termType rr:Literal .

map:om_035 rml:reference "CreationDate" ;
	rdf:type rr:ObjectMap ;
	rr:datatype xsd:dateTime ;
	rr:termType rr:Literal .

map:om_036 rdf:type rr:ObjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources/interval/{GUID}" ;
	rr:termType rr:Literal .

map:om_037 rml:reference "ResourceUID" ;
	rdf:type rr:ObjectMap ;
	rr:termType rr:Literal .

map:om_038 rdf:type rr:ObjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources/cost/{GUID}" ;
	rr:termType rr:Literal .

map:om_039 rdf:type rr:ObjectMap ;
	rr:joinCondition map:jc_000 ;
	rr:parentTriplesMap map:map_task_000 .

map:om_040 rdf:type rr:ObjectMap ;
	rr:constant "http://www.w3.org/2006/time#Interval" ;
	rr:termType rr:IRI .

map:om_041 rdf:type rr:ObjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources/startInstant/{GUID}" ;
	rr:termType rr:Literal .

map:om_042 rdf:type rr:ObjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources/endInstant/{GUID}" ;
	rr:termType rr:Literal .

map:om_043 rdf:type rr:ObjectMap ;
	rr:constant "http://www.w3.org/2006/time#Instant" ;
	rr:termType rr:IRI .

map:om_044 rml:reference "StartDate" ;
	rdf:type rr:ObjectMap ;
	rr:datatype xsd:dateTime ;
	rr:termType rr:Literal .

map:om_045 rdf:type rr:ObjectMap ;
	rr:constant "http://www.w3.org/2006/time#Instant" ;
	rr:termType rr:IRI .

map:om_046 rml:reference "FinishDate" ;
	rdf:type rr:ObjectMap ;
	rr:datatype xsd:dateTime ;
	rr:termType rr:Literal .

map:om_047 rdf:type rr:ObjectMap ;
	rr:constant "http://www.w3.org/2006/time#Interval" ;
	rr:termType rr:IRI .

map:om_048 rdf:type rr:ObjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources/startInstant/{GUID}" ;
	rr:termType rr:Literal .

map:om_049 rdf:type rr:ObjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources/endInstant/{GUID}" ;
	rr:termType rr:Literal .

map:om_050 rdf:type rr:ObjectMap ;
	rr:constant "http://www.w3.org/2006/time#Instant" ;
	rr:termType rr:IRI .

map:om_051 rml:reference "Start" ;
	rdf:type rr:ObjectMap ;
	rr:datatype xsd:dateTime ;
	rr:termType rr:Literal .

map:om_052 rdf:type rr:ObjectMap ;
	rr:constant "http://www.w3.org/2006/time#Instant" ;
	rr:termType rr:IRI .

map:om_053 rml:reference "Finish" ;
	rdf:type rr:ObjectMap ;
	rr:datatype xsd:dateTime ;
	rr:termType rr:Literal .

map:om_054 rdf:type rr:ObjectMap ;
	rr:constant "http://www.w3.org/2006/time#Interval" ;
	rr:termType rr:IRI .

map:om_055 rdf:type rr:ObjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources/startInstant/{GUID}" ;
	rr:termType rr:Literal .

map:om_056 rdf:type rr:ObjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources/endInstant/{GUID}" ;
	rr:termType rr:Literal .

map:om_057 rdf:type rr:ObjectMap ;
	rr:constant "http://www.w3.org/2006/time#Instant" ;
	rr:termType rr:IRI .

map:om_058 rml:reference "Start" ;
	rdf:type rr:ObjectMap ;
	rr:datatype xsd:dateTime ;
	rr:termType rr:Literal .

map:om_059 rdf:type rr:ObjectMap ;
	rr:constant "http://www.w3.org/2006/time#Instant" ;
	rr:termType rr:IRI .

map:om_060 rml:reference "Finish" ;
	rdf:type rr:ObjectMap ;
	rr:datatype xsd:dateTime ;
	rr:termType rr:Literal .

map:pm_000 rdf:type rr:PredicateMap ;
	rr:constant rdf:type .

map:pm_001 rdf:type rr:PredicateMap ;
	rr:constant const:projectID .

map:pm_002 rdf:type rr:PredicateMap ;
	rr:constant const:hasName .

map:pm_003 rdf:type rr:PredicateMap ;
	rr:constant process:hasCreationDate .

map:pm_004 rdf:type rr:PredicateMap ;
	rr:constant process:hasCost .

map:pm_005 rdf:type rr:PredicateMap ;
	rr:constant process:isPlannedIn .

map:pm_006 rdf:type rr:PredicateMap ;
	rr:constant process:hasTask .

map:pm_007 rdf:type rr:PredicateMap ;
	rr:constant process:involvesResourceType .

map:pm_008 rdf:type rr:PredicateMap ;
	rr:constant rdf:type .

map:pm_009 rdf:type rr:PredicateMap ;
	rr:constant process:amount .

map:pm_010 rdf:type rr:PredicateMap ;
	rr:constant process:isMeasuredIn .

map:pm_011 rdf:type rr:PredicateMap ;
	rr:constant rdf:type .

map:pm_012 rdf:type rr:PredicateMap ;
	rr:constant process:amount .

map:pm_013 rdf:type rr:PredicateMap ;
	rr:constant rdf:type .

map:pm_014 rdf:type rr:PredicateMap ;
	rr:constant process:amount .

map:pm_015 rdf:type rr:PredicateMap ;
	rr:constant rdf:type .

map:pm_016 rdf:type rr:PredicateMap ;
	rr:constant process:currencyCode .

map:pm_017 rdf:type rr:PredicateMap ;
	rr:constant process:currencySymbol .

map:pm_018 rdf:type rr:PredicateMap ;
	rr:constant rdf:type .

map:pm_019 rdf:type rr:PredicateMap ;
	rr:constant process:taskId .

map:pm_020 rdf:type rr:PredicateMap ;
	rr:constant process:taskUid .

map:pm_021 rdf:type rr:PredicateMap ;
	rr:constant process:hasName .

map:pm_022 rdf:type rr:PredicateMap ;
	rr:constant process:hasCreationDate .

map:pm_023 rdf:type rr:PredicateMap ;
	rr:constant process:isPlannedIn .

map:pm_024 rdf:type rr:PredicateMap ;
	rr:constant process:hasPriority .

map:pm_025 rdf:type rr:PredicateMap ;
	rr:constant process:hasProgress .

map:pm_026 rdf:type rr:PredicateMap ;
	rr:constant process:hasStatus .

map:pm_027 rdf:type rr:PredicateMap ;
	rr:constant process:hasCost .

map:pm_028 rdf:type rr:PredicateMap ;
	rr:constant rdf:type .

map:pm_029 rdf:type rr:PredicateMap ;
	rr:constant resource:resourceId .

map:pm_030 rdf:type rr:PredicateMap ;
	rr:constant resource:resourceUid .

map:pm_031 rdf:type rr:PredicateMap ;
	rr:constant resource:hasCreationDate .

map:pm_032 rdf:type rr:PredicateMap ;
	rr:constant resource:hasResourceType .

map:pm_033 rdf:type rr:PredicateMap ;
	rr:constant rdf:type .

map:pm_034 rdf:type rr:PredicateMap ;
	rr:constant resource:assignmentId .

map:pm_035 rdf:type rr:PredicateMap ;
	rr:constant resource:hasCreationDate .

map:pm_036 rdf:type rr:PredicateMap ;
	rr:constant process:isPlannedIn .

map:pm_037 rdf:type rr:PredicateMap ;
	rr:constant resource:assignedResource .

map:pm_038 rdf:type rr:PredicateMap ;
	rr:constant process:hasCost .

map:pm_039 rdf:type rr:PredicateMap ;
	rr:constant resource:assignedTask .

map:pm_040 rdf:type rr:PredicateMap ;
	rr:constant rdf:type .

map:pm_041 rdf:type rr:PredicateMap ;
	rr:constant time:hasBeginning .

map:pm_042 rdf:type rr:PredicateMap ;
	rr:constant process:hasEnd .

map:pm_043 rdf:type rr:PredicateMap ;
	rr:constant rdf:type .

map:pm_044 rdf:type rr:PredicateMap ;
	rr:constant time:inXSDDateTimeStamp .

map:pm_045 rdf:type rr:PredicateMap ;
	rr:constant rdf:type .

map:pm_046 rdf:type rr:PredicateMap ;
	rr:constant process:inXSDDateTimeStamp .

map:pm_047 rdf:type rr:PredicateMap ;
	rr:constant rdf:type .

map:pm_048 rdf:type rr:PredicateMap ;
	rr:constant time:hasBeginning .

map:pm_049 rdf:type rr:PredicateMap ;
	rr:constant process:hasEnd .

map:pm_050 rdf:type rr:PredicateMap ;
	rr:constant rdf:type .

map:pm_051 rdf:type rr:PredicateMap ;
	rr:constant time:inXSDDateTimeStamp .

map:pm_052 rdf:type rr:PredicateMap ;
	rr:constant rdf:type .

map:pm_053 rdf:type rr:PredicateMap ;
	rr:constant process:inXSDDateTimeStamp .

map:pm_054 rdf:type rr:PredicateMap ;
	rr:constant rdf:type .

map:pm_055 rdf:type rr:PredicateMap ;
	rr:constant time:hasBeginning .

map:pm_056 rdf:type rr:PredicateMap ;
	rr:constant process:hasEnd .

map:pm_057 rdf:type rr:PredicateMap ;
	rr:constant rdf:type .

map:pm_058 rdf:type rr:PredicateMap ;
	rr:constant time:inXSDDateTimeStamp .

map:pm_059 rdf:type rr:PredicateMap ;
	rr:constant rdf:type .

map:pm_060 rdf:type rr:PredicateMap ;
	rr:constant process:inXSDDateTimeStamp .

map:pom_000 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_000 ;
	rr:predicateMap map:pm_000 .

map:pom_001 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_001 ;
	rr:predicateMap map:pm_001 .

map:pom_002 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_002 ;
	rr:predicateMap map:pm_002 .

map:pom_003 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_003 ;
	rr:predicateMap map:pm_003 .

map:pom_004 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_004 ;
	rr:predicateMap map:pm_004 .

map:pom_005 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_005 ;
	rr:predicateMap map:pm_005 .

map:pom_006 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_006 ;
	rr:predicateMap map:pm_006 .

map:pom_007 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_007 ;
	rr:predicateMap map:pm_007 .

map:pom_008 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_008 ;
	rr:predicateMap map:pm_008 .

map:pom_009 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_009 ;
	rr:predicateMap map:pm_009 .

map:pom_010 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_010 ;
	rr:predicateMap map:pm_010 .

map:pom_011 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_011 ;
	rr:predicateMap map:pm_011 .

map:pom_012 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_012 ;
	rr:predicateMap map:pm_012 .

map:pom_013 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_013 ;
	rr:predicateMap map:pm_013 .

map:pom_014 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_014 ;
	rr:predicateMap map:pm_014 .

map:pom_015 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_015 ;
	rr:predicateMap map:pm_015 .

map:pom_016 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_016 ;
	rr:predicateMap map:pm_016 .

map:pom_017 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_017 ;
	rr:predicateMap map:pm_017 .

map:pom_018 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_018 ;
	rr:predicateMap map:pm_018 .

map:pom_019 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_019 ;
	rr:predicateMap map:pm_019 .

map:pom_020 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_020 ;
	rr:predicateMap map:pm_020 .

map:pom_021 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_021 ;
	rr:predicateMap map:pm_021 .

map:pom_022 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_022 ;
	rr:predicateMap map:pm_022 .

map:pom_023 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_023 ;
	rr:predicateMap map:pm_023 .

map:pom_024 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_024 ;
	rr:predicateMap map:pm_024 .

map:pom_025 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_025 ;
	rr:predicateMap map:pm_025 .

map:pom_026 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_026 ;
	rr:predicateMap map:pm_026 .

map:pom_027 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_027 ;
	rr:predicateMap map:pm_027 .

map:pom_028 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_028 ;
	rr:predicateMap map:pm_028 .

map:pom_029 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_029 ;
	rr:predicateMap map:pm_029 .

map:pom_030 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_030 ;
	rr:predicateMap map:pm_030 .

map:pom_031 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_031 ;
	rr:predicateMap map:pm_031 .

map:pom_032 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_032 ;
	rr:predicateMap map:pm_032 .

map:pom_033 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_033 ;
	rr:predicateMap map:pm_033 .

map:pom_034 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_034 ;
	rr:predicateMap map:pm_034 .

map:pom_035 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_035 ;
	rr:predicateMap map:pm_035 .

map:pom_036 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_036 ;
	rr:predicateMap map:pm_036 .

map:pom_037 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_037 ;
	rr:predicateMap map:pm_037 .

map:pom_038 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_038 ;
	rr:predicateMap map:pm_038 .

map:pom_039 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_039 ;
	rr:predicateMap map:pm_039 .

map:pom_040 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_040 ;
	rr:predicateMap map:pm_040 .

map:pom_041 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_041 ;
	rr:predicateMap map:pm_041 .

map:pom_042 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_042 ;
	rr:predicateMap map:pm_042 .

map:pom_043 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_043 ;
	rr:predicateMap map:pm_043 .

map:pom_044 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_044 ;
	rr:predicateMap map:pm_044 .

map:pom_045 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_045 ;
	rr:predicateMap map:pm_045 .

map:pom_046 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_046 ;
	rr:predicateMap map:pm_046 .

map:pom_047 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_047 ;
	rr:predicateMap map:pm_047 .

map:pom_048 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_048 ;
	rr:predicateMap map:pm_048 .

map:pom_049 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_049 ;
	rr:predicateMap map:pm_049 .

map:pom_050 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_050 ;
	rr:predicateMap map:pm_050 .

map:pom_051 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_051 ;
	rr:predicateMap map:pm_051 .

map:pom_052 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_052 ;
	rr:predicateMap map:pm_052 .

map:pom_053 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_053 ;
	rr:predicateMap map:pm_053 .

map:pom_054 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_054 ;
	rr:predicateMap map:pm_054 .

map:pom_055 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_055 ;
	rr:predicateMap map:pm_055 .

map:pom_056 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_056 ;
	rr:predicateMap map:pm_056 .

map:pom_057 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_057 ;
	rr:predicateMap map:pm_057 .

map:pom_058 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_058 ;
	rr:predicateMap map:pm_058 .

map:pom_059 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_059 ;
	rr:predicateMap map:pm_059 .

map:pom_060 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_060 ;
	rr:predicateMap map:pm_060 .

map:rules_000 <http://rdfs.org/ns/void#exampleResource> map:map_assignment_000, map:map_cost_000, map:map_cost_assignment_000, map:map_cost_task_000, map:map_instant_end_assignment_000, map:map_instant_end_project_000, map:map_instant_end_task_000, map:map_instant_start_assignment_000, map:map_instant_start_project_000, map:map_instant_start_task_000, map:map_interval_assignment_000, map:map_interval_project_000, map:map_interval_task_000, map:map_project_000, map:map_resource_000, map:map_task_000, map:map_unitOfCurrency_000 ;
	rdf:type <http://rdfs.org/ns/void#Dataset> .

map:s_000 rdf:type rr:SubjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources/project/{GUID}" .

map:s_001 rdf:type rr:SubjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources/cost/{GUID}" .

map:s_002 rdf:type rr:SubjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources/cost/{GUID}" .

map:s_003 rdf:type rr:SubjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources/cost/{GUID}" .

map:s_004 rdf:type rr:SubjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources/unitOfCurrency/{GUID}" .

map:s_005 rdf:type rr:SubjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources/task/{GUID}" .

map:s_006 rdf:type rr:SubjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources/resource/{GUID}" .

map:s_007 rdf:type rr:SubjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources/assignment/{GUID}" .

map:s_008 rdf:type rr:SubjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources/interval/{GUID}" .

map:s_009 rdf:type rr:SubjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources/startInstant/{GUID}" .

map:s_010 rdf:type rr:SubjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources/endInstant/{GUID}" .

map:s_011 rdf:type rr:SubjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources/interval/{GUID}" .

map:s_012 rdf:type rr:SubjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources/startInstant/{GUID}" .

map:s_013 rdf:type rr:SubjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources/endInstant/{GUID}" .

map:s_014 rdf:type rr:SubjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources/interval/{GUID}" .

map:s_015 rdf:type rr:SubjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources/startInstant/{GUID}" .

map:s_016 rdf:type rr:SubjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources/endInstant/{GUID}" .

map:source_000 rml:iterator "Project" ;
	rml:referenceFormulation ql:XPath ;
	rml:source """ + self.file_path + """ ;
	rdf:type rml:LogicalSource .

map:source_001 rml:iterator "Project" ;
	rml:referenceFormulation ql:XPath ;
	rml:source """ + self.file_path + """ ;
	rdf:type rml:LogicalSource .

map:source_002 rml:iterator "Project/Tasks/Task[*]" ;
	rml:referenceFormulation ql:XPath ;
	rml:source """ + self.file_path + """ ;
	rdf:type rml:LogicalSource .

map:source_003 rml:iterator "Project/Assignments/Assignment[*]" ;
	rml:referenceFormulation ql:XPath ;
	rml:source """ + self.file_path + """ ;
	rdf:type rml:LogicalSource .

map:source_004 rml:iterator "Project" ;
	rml:referenceFormulation ql:XPath ;
	rml:source """ + self.file_path + """ ;
	rdf:type rml:LogicalSource .

map:source_005 rml:iterator "Project/Tasks/Task[*]" ;
	rml:referenceFormulation ql:XPath ;
	rml:source """ + self.file_path + """ ;
	rdf:type rml:LogicalSource .

map:source_006 rml:iterator "Project/Resources/Resource[*]" ;
	rml:referenceFormulation ql:XPath ;
	rml:source """ + self.file_path + """ ;
	rdf:type rml:LogicalSource .

map:source_007 rml:iterator "Project/Assignments/Assignment[*]" ;
	rml:referenceFormulation ql:XPath ;
	rml:source """ + self.file_path + """ ;
	rdf:type rml:LogicalSource .

map:source_008 rml:iterator "Project" ;
	rml:referenceFormulation ql:XPath ;
	rml:source """ + self.file_path + """ ;
	rdf:type rml:LogicalSource .

map:source_009 rml:iterator "Project" ;
	rml:referenceFormulation ql:XPath ;
	rml:source """ + self.file_path + """ ;
	rdf:type rml:LogicalSource .

map:source_010 rml:iterator "Project" ;
	rml:referenceFormulation ql:XPath ;
	rml:source """ + self.file_path + """ ;
	rdf:type rml:LogicalSource .

map:source_011 rml:iterator "Project/Tasks/Task[*]" ;
	rml:referenceFormulation ql:XPath ;
	rml:source """ + self.file_path + """ ;
	rdf:type rml:LogicalSource .

map:source_012 rml:iterator "Project/Tasks/Task[*]" ;
	rml:referenceFormulation ql:XPath ;
	rml:source """ + self.file_path + """ ;
	rdf:type rml:LogicalSource .

map:source_013 rml:iterator "Project/Tasks/Task[*]" ;
	rml:referenceFormulation ql:XPath ;
	rml:source """ + self.file_path + """ ;
	rdf:type rml:LogicalSource .

map:source_014 rml:iterator "Project/Assignments/Assignment[*]" ;
	rml:referenceFormulation ql:XPath ;
	rml:source """ + self.file_path + """ ;
	rdf:type rml:LogicalSource .

map:source_015 rml:iterator "Project/Assignments/Assignment[*]" ;
	rml:referenceFormulation ql:XPath ;
	rml:source """ + self.file_path + """ ;
	rdf:type rml:LogicalSource .

map:source_016 rml:iterator "Project/Assignments/Assignment[*]" ;
	rml:referenceFormulation ql:XPath ;
	rml:source """ + self.file_path + """ ;
	rdf:type rml:LogicalSource .
""")
        map_file.close()