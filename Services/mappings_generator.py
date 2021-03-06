

class Mappings_generator:
	def __init__(self, file_path, mappings_path, project_name, process_name):
		self.file_path = '"' + file_path + '"'
		self.mappings_path = mappings_path
		self.project_name = project_name
		self.process_name = process_name
		
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
@prefix data: <https://data.cogito.iot.linkeddata.es/resources#> .

map:map_cost_000 rml:logicalSource map:source_001 ;
	rdf:type rr:TriplesMap ;
	rdfs:label "cost" ;
	rr:predicateObjectMap map:pom_009, map:pom_010, map:pom_011 ;
	rr:subjectMap map:s_001 .

map:map_cost_task_000 rml:logicalSource map:source_002 ;
	rdf:type rr:TriplesMap ;
	rdfs:label "cost_task" ;
	rr:predicateObjectMap map:pom_012 ;
	rr:subjectMap map:s_002 .

map:map_process_000 rml:logicalSource map:source_000 ;
	rdf:type rr:TriplesMap ;
	rdfs:label "process" ;
	rr:predicateObjectMap map:pom_000, map:pom_001, map:pom_002, map:pom_003, map:pom_004, map:pom_005, map:pom_006, map:pom_007, map:pom_008 ;
	rr:subjectMap map:s_000 .

map:map_resource_000 rml:logicalSource map:source_005 ;
	rdf:type rr:TriplesMap ;
	rdfs:label "resource" ;
	rr:predicateObjectMap map:pom_027, map:pom_028, map:pom_029, map:pom_030, map:pom_031 ;
	rr:subjectMap map:s_005 .

map:map_task_000 rml:logicalSource map:source_004 ;
	rdf:type rr:TriplesMap ;
	rdfs:label "task" ;
	rr:predicateObjectMap map:pom_016, map:pom_017, map:pom_018, map:pom_019, map:pom_020, map:pom_021, map:pom_022, map:pom_023, map:pom_024, map:pom_025, map:pom_026 ;
	rr:subjectMap map:s_004 .

map:map_unitOfCurrency_000 rml:logicalSource map:source_003 ;
	rdf:type rr:TriplesMap ;
	rdfs:label "unitOfCurrency" ;
	rr:predicateObjectMap map:pom_013, map:pom_014, map:pom_015 ;
	rr:subjectMap map:s_003 .

map:om_000 rdf:type rr:ObjectMap ;
	rr:constant "https://cogito.iot.linkeddata.es/def/process#Process" ;
	rr:termType rr:IRI .

map:om_001 rml:reference "GUID" ;
	rdf:type rr:ObjectMap ;
	rr:termType rr:Literal .

map:om_002 rml:reference "Title" ;
	rdf:type rr:ObjectMap ;
	rr:datatype xsd:string ;
	rr:termType rr:Literal .

map:om_003 rml:reference "CreationDate" ;
	rdf:type rr:ObjectMap ;
	rr:datatype xsd:dateTime ;
	rr:termType rr:Literal .

map:om_004 rdf:type rr:ObjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources#Cost_""" + self.project_name + """_{Title}" ;
	rr:termType rr:Literal .

map:om_005 rml:reference "StartDate" ;
	rdf:type rr:ObjectMap ;
	rr:datatype xsd:dateTime ;
	rr:termType rr:Literal .

map:om_006 rml:reference "FinishDate" ;
	rdf:type rr:ObjectMap ;
	rr:datatype xsd:dateTime ;
	rr:termType rr:Literal .

map:om_007 rdf:type rr:ObjectMap ;
	rr:parentTriplesMap map:map_task_000 .

map:om_008 rdf:type rr:ObjectMap ;
	rr:parentTriplesMap map:map_resource_000 .

map:om_009 rdf:type rr:ObjectMap ;
	rr:constant "https://cogito.iot.linkeddata.es/def/process#Cost" ;
	rr:termType rr:IRI .

map:om_010 rml:reference "CurrencyDigits" ;
	rdf:type rr:ObjectMap ;
	rr:datatype xsd:float ;
	rr:termType rr:Literal .

map:om_011 rdf:type rr:ObjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources#UnitOfCurrency_""" + self.project_name + """_{Title}" ;
	rr:termType rr:Literal .

map:om_012 rdf:type rr:ObjectMap ;
	rr:constant "https://cogito.iot.linkeddata.es/def/process#Cost" ;
	rr:termType rr:IRI .

map:om_013 rdf:type rr:ObjectMap ;
	rr:constant "https://cogito.iot.linkeddata.es/def/process#UnitOfCurrency" ;
	rr:termType rr:IRI .

map:om_014 rml:reference "CurrencyCode" ;
	rdf:type rr:ObjectMap ;
	rr:termType rr:Literal .

map:om_015 rml:reference "CurrencySymbol" ;
	rdf:type rr:ObjectMap ;
	rr:termType rr:Literal .

map:om_016 rdf:type rr:ObjectMap ;
	rr:constant "https://cogito.iot.linkeddata.es/def/process#Task" ;
	rr:termType rr:IRI .

map:om_017 rml:reference "ID" ;
	rdf:type rr:ObjectMap ;
	rr:termType rr:Literal .

map:om_018 rml:reference "UID" ;
	rdf:type rr:ObjectMap ;
	rr:termType rr:Literal .

map:om_019 rml:reference "Name" ;
	rdf:type rr:ObjectMap ;
	rr:datatype xsd:string ;
	rr:termType rr:Literal .

map:om_020 rml:reference "CreateDate" ;
	rdf:type rr:ObjectMap ;
	rr:datatype xsd:dateTime ;
	rr:termType rr:Literal .

map:om_021 rml:reference "Start" ;
	rdf:type rr:ObjectMap ;
	rr:datatype xsd:dateTime ;
	rr:termType rr:Literal .

map:om_022 rml:reference "Finish" ;
	rdf:type rr:ObjectMap ;
	rr:datatype xsd:dateTime ;
	rr:termType rr:Literal .

map:om_023 rml:reference "Priority" ;
	rdf:type rr:ObjectMap ;
	rr:datatype xsd:integer ;
	rr:termType rr:Literal .

map:om_024 rml:reference "RemainingWork" ;
	rdf:type rr:ObjectMap ;
	rr:datatype xsd:string ;
	rr:termType rr:Literal .

map:om_025 rml:reference "ActualWork" ;
	rdf:type rr:ObjectMap ;
	rr:datatype xsd:string ;
	rr:termType rr:Literal .

map:om_026 rdf:type rr:ObjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources#Task_Cost_""" + self.project_name + """_""" + self.process_name + """_{ID}" ;
	rr:termType rr:Literal .

map:om_027 rdf:type rr:ObjectMap ;
	rr:constant "https://cogito.iot.linkeddata.es/def/resource#ResourceType" ;
	rr:termType rr:IRI .

map:om_028 rml:reference "ID" ;
	rdf:type rr:ObjectMap ;
	rr:termType rr:Literal .

map:om_029 rml:reference "UID" ;
	rdf:type rr:ObjectMap ;
	rr:termType rr:Literal .

map:om_030 rml:reference "CreationDate" ;
	rdf:type rr:ObjectMap ;
	rr:datatype xsd:dateTime ;
	rr:termType rr:Literal .

map:om_031 rdf:type rr:ObjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources#Resource_Type_{Type}" ;
	rr:termType rr:Literal .

map:pm_000 rdf:type rr:PredicateMap ;
	rr:constant rdf:type .

map:pm_001 rdf:type rr:PredicateMap ;
	rr:constant process:processID .

map:pm_002 rdf:type rr:PredicateMap ;
	rr:constant process:hasName .

map:pm_003 rdf:type rr:PredicateMap ;
	rr:constant process:hasCreationDate .

map:pm_004 rdf:type rr:PredicateMap ;
	rr:constant process:hasCost .

map:pm_005 rdf:type rr:PredicateMap ;
	rr:constant process:hasStartDate .

map:pm_006 rdf:type rr:PredicateMap ;
	rr:constant process:hasEndDate .

map:pm_007 rdf:type rr:PredicateMap ;
	rr:constant process:hasTask .

map:pm_008 rdf:type rr:PredicateMap ;
	rr:constant process:involvesResourceType .

map:pm_009 rdf:type rr:PredicateMap ;
	rr:constant rdf:type .

map:pm_010 rdf:type rr:PredicateMap ;
	rr:constant process:amount .

map:pm_011 rdf:type rr:PredicateMap ;
	rr:constant process:isMeasuredIn .

map:pm_012 rdf:type rr:PredicateMap ;
	rr:constant rdf:type .

map:pm_013 rdf:type rr:PredicateMap ;
	rr:constant rdf:type .

map:pm_014 rdf:type rr:PredicateMap ;
	rr:constant process:currencyCode .

map:pm_015 rdf:type rr:PredicateMap ;
	rr:constant process:currencySymbol .

map:pm_016 rdf:type rr:PredicateMap ;
	rr:constant rdf:type .

map:pm_017 rdf:type rr:PredicateMap ;
	rr:constant process:taskId .

map:pm_018 rdf:type rr:PredicateMap ;
	rr:constant process:taskUid .

map:pm_019 rdf:type rr:PredicateMap ;
	rr:constant process:hasName .

map:pm_020 rdf:type rr:PredicateMap ;
	rr:constant process:hasCreationDate .

map:pm_021 rdf:type rr:PredicateMap ;
	rr:constant process:hasStartDate .

map:pm_022 rdf:type rr:PredicateMap ;
	rr:constant process:hasEndDate .

map:pm_023 rdf:type rr:PredicateMap ;
	rr:constant process:hasPriority .

map:pm_024 rdf:type rr:PredicateMap ;
	rr:constant process:hasProgress .

map:pm_025 rdf:type rr:PredicateMap ;
	rr:constant process:hasStatus .

map:pm_026 rdf:type rr:PredicateMap ;
	rr:constant process:hasCost .

map:pm_027 rdf:type rr:PredicateMap ;
	rr:constant rdf:type .

map:pm_028 rdf:type rr:PredicateMap ;
	rr:constant resource:resourceTypeId .

map:pm_029 rdf:type rr:PredicateMap ;
	rr:constant resource:resourceTypeUid .

map:pm_030 rdf:type rr:PredicateMap ;
	rr:constant resource:hasCreationDate .

map:pm_031 rdf:type rr:PredicateMap ;
	rr:constant resource:hasResourceType .

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

map:rules_000 <http://rdfs.org/ns/void#exampleResource> map:map_cost_000, map:map_cost_task_000, map:map_process_000, map:map_resource_000, map:map_task_000, map:map_unitOfCurrency_000 ;
	rdf:type <http://rdfs.org/ns/void#Dataset> .

map:s_000 rdf:type rr:SubjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources#Process_""" + self.project_name + """_{Title}" .

map:s_001 rdf:type rr:SubjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources#Cost_""" + self.project_name + """_{Title}" .

map:s_002 rdf:type rr:SubjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources#Task_Cost_""" + self.project_name + """_""" + self.process_name + """_{ID}" .

map:s_003 rdf:type rr:SubjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources#unitOfCurrency/""" + self.project_name + """_{Title}" .

map:s_004 rdf:type rr:SubjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources#Task_""" + self.project_name + """_""" + self.process_name + """_{ID}" .

map:s_005 rdf:type rr:SubjectMap ;
	rr:template "https://data.cogito.iot.linkeddata.es/resources#Resource_Type_""" + self.project_name + """_""" + self.process_name + """_{ID}" .

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

map:source_003 rml:iterator "Project" ;
	rml:referenceFormulation ql:XPath ;
	rml:source """ + self.file_path + """ ;
	rdf:type rml:LogicalSource .

map:source_004 rml:iterator "Project/Tasks/Task[*]" ;
	rml:referenceFormulation ql:XPath ;
	rml:source """ + self.file_path + """ ;
	rdf:type rml:LogicalSource .

map:source_005 rml:iterator "Project/Resources/Resource[*]" ;
	rml:referenceFormulation ql:XPath ;
	rml:source """ + self.file_path + """ ;
	rdf:type rml:LogicalSource .
""")
		map_file.close()