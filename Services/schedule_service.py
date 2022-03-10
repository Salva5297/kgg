from Services.mappings_generator import Mappings_generator
from Controllers.helio_controller import Helio_controller
from Controllers.triplestore_controller import Triple_Store_Controller

class Schedule_service:
    def __init__(self, tmp_name, graph_namespace):
        self.tmp_file_path = tmp_name
        self.mappings_path = '/schedule_mappings'
        self.output_path = '/schedule_rdf'
        self.graph_namespace = graph_namespace


    def execute_conversion(self):
        """
        Execute the schedule kgg conversion to RDF
        """
        # Execute mappings generator
        mapping_generator = Mappings_generator(self.tmp_file_path, self.mappings_path)
        mapping_generator.generate_mappings()
        print('ended mapping generation')

        # Execute Helio
        helio_controller = Helio_controller(self.mappings_path, self.output_path, self.graph_namespace)
        helio_controller.execute_helio()

        # Send graph to triple store
        triplestore_controller = Triple_Store_Controller(self.output_path, self.graph_namespace)
        triplestore_controller.send_graph()