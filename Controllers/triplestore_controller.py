import subprocess
import sys

class Triple_Store_Controller:

    def __init__(self, output_path, graph_namespace):
        self.output_path = output_path
        self.graph_namespace = graph_namespace
        self.triple_store_url = "http://localhost:8890/"
        self.graph_url = "https://data.cogito.iot.linkeddata.es/schedule/"


    def send_graph(self):
        proc = subprocess.Popen(["curl", 
            "--digest", 
            "--verbose", 
            "--user", 
            "dba:mysecret", 
            "--url", 
            self.triple_store_url + "sparql-graph-crud-auth?graph-uri=" + self.graph_url + self.graph_namespace, 
            "-T", 
            self.output_path + '/' + self.graph_namespace + ".ttl"],
            shell=False, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE)

        (out, err) = proc.communicate()
        lastCode = str(err).split('HTTP/1.1 ')[-1].split(" ")[0]

        if lastCode == "200":
            print(["Updated Graph or Existing Graph", 200])
        elif lastCode == "201":
            print(["Created Graph", 201])
        elif lastCode == "401":
            print(["Error with Authorization", 401])
        else:
            print(["You did something wrong", 500])