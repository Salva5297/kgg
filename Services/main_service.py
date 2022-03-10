import os
from flask import request, make_response, jsonify

from Services.tmp_file_service import Tmp_service
from Services.schedule_service import Schedule_service

class Service:
    def __init__(self, request_data):
        self.uploaded_file = request_data.files['file']
        self.type = None
        self.graph_namespace = ''
        self.response_dict = {}

    def post(self):
        """
        KGG Data Handler for POST requests
        """
        # self.type = self.request.args.get('type')
        if self.uploaded_file.filename != '':
            self.graph_namespace = self.uploaded_file.filename.split('.')[0] # Get the filename without the extension to create the graph namespace
            file_data = self.uploaded_file.read()
            tmp_service = Tmp_service(file_data)
            tmp_service.create_tmp_file() # create temporal file
            # Execute execute corresponding kgg, in this case we only have one kgg that is schedule
            schedule_service = Schedule_service(tmp_service.tmp_name, self.graph_namespace)
            schedule_service.execute_conversion()
            
            self.response_dict['graph_uri'] = schedule_service.graph_uri
            os.remove(tmp_service.tmp_name) # remove temporal file
        else:
            self.response_dict['Error'] = 'No filename'