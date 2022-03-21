import os
from flask import Flask, json, send_file, request, make_response, jsonify, after_this_request
from Services.main_service import Service

app = Flask(__name__)
@app.route("/schedule", methods=['POST'])
def controller_post():
    """
    KGG Data Handler for POST requests
    """
    service = Service(request)#(request,kgg_endpoint)
    service.post() # return graph uri to query sparql endpoint
    return jsonify(service.response_dict)

@app.route("/", methods=['POST'])
def controller_post_return_ttl():
    """
    KGG Data Handler for POST requests that want as response a TTL file
    """
    service = Service(request)
    service.post_return_file()
    @after_this_request
    def remove_file(response):
        try:
            os.remove(service.ttl_path)
        except Exception as error:
            app.logger.error("Error removing downloaded file handle", error)
        return response

    return send_file(service.ttl_path, as_attachment=True)




if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)