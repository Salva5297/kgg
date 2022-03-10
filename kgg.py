from flask import Flask, json, send_file, request, make_response, jsonify
from Services.main_service import Service

app = Flask(__name__)
@app.route("/", methods=['POST'])
def controller_post():
    """
    KGG Data Handler for POST requests
    """
    service = Service(request)#(request,kgg_endpoint)
    service.post() # return graph uri to query sparql endpoint
    return jsonify(service.response_dict)



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)