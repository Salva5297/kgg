import os
class Helio_controller:
    def __init__(self, mappings_path, output_path, graph_namespace):
        self.mappings_path = mappings_path
        self.output_path = output_path
        self.graph_namespace = graph_namespace

    
    def execute_helio(self):
        """
        Execute Helio to create the rdf graph
        """
        # Execute Helio

        #print('java -jar helio.jar --mappings=Repositories/mappings'+ self.mappings_path + ' --config=config.json --write=Repositories/rdf_generated' + self.output_path + '/' + self.graph_namespace + '.ttl --close --clean')

        os.system('java -jar helio.jar --mappings=Repositories/mappings'+ self.mappings_path + ' --config=config.json --write=Repositories/rdf_generated' + self.output_path + '/' + self.graph_namespace + '.ttl --close --clean')
