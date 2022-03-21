from Services.mappings_generator import Mappings_generator
from Controllers.helio_controller import Helio_controller
from Controllers.triplestore_controller import Triple_Store_Controller

import xml.etree.ElementTree as ET  

class Schedule_service:
    def __init__(self, tmp_name, graph_namespace, project_name):
        self.tmp_file_path = tmp_name
        self.mappings_path = '/schedule_mappings'
        self.output_path = 'Repositories/rdf_generated/schedule_rdf'
        self.graph_namespace = graph_namespace
        self.graph_uri = ""
        self.project_name = project_name
        self.ttl_path = ""
        self.process_name = ""


    def execute_conversion(self):
        """
        Execute the schedule kgg conversion to RDF
        """
        # Execute mappings generator
        mapping_generator = Mappings_generator(self.tmp_file_path, self.mappings_path, self.project_name)
        mapping_generator.generate_mappings()
        print('ended mapping generation')

        # Execute Helio
        helio_controller = Helio_controller(self.mappings_path, self.output_path, self.graph_namespace)
        helio_controller.execute_helio()

        # Send graph to triple store
        triplestore_controller = Triple_Store_Controller(self.output_path, self.graph_namespace)
        triplestore_controller.send_graph()
        self.graph_uri = triplestore_controller.graph_url + self.graph_namespace
    
    def execute_conversion_return_ttl(self):

        # Get process name to write it inside the mapping file
        self.get_process_name()

        # Execute mappings generator
        mapping_generator = Mappings_generator(self.tmp_file_path, self.mappings_path, self.project_name, self.process_name)
        mapping_generator.generate_mappings()
        print('ended mapping generation')

        # Execute Helio
        helio_controller = Helio_controller(self.mappings_path, self.output_path, self.graph_namespace)
        helio_controller.execute_helio()
        self.ttl_path =self.output_path + '/' + self.graph_namespace + '.ttl'


    def get_process_name(self):
        xml_doc = ET.parse(self.tmp_file_path)
        root = xml_doc.getroot()
        for element in root.findall("Project"):
            self.process_name = element.find('Title').text
