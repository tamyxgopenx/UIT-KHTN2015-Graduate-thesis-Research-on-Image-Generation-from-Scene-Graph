#!flask/bin/python
from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import json
import os
import sys
from scripts.run_model import main

class argumentBuilder:
    checkpoint = 'sg2im-models/vg128.pt'
    id = ''
    scene_graphs_json = ''
    output_dir = 'outputs'
    draw_scene_graphs = 0
    device = 'cpu'

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/generate', methods=['POST'])
def generate():
    error = None
    print("Hello")
    if request.method == 'POST':
        print("It is POST")
        print(request.content_type)
        scene_graph = request.json
        print(scene_graph)
        print(scene_graph['objects'])
        print(scene_graph['relationships'])
        args = argumentBuilder()
        args.scene_graphs_json = scene_graph
        args.id = str(scene_graph['visitor_id'])
        model_build = main(args)
        if (model_build == True):
            print('Built')
        else:
            print('Fail')
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return jsonify(success=True), 201

@app.route('/get_image', methods=['GET'])
def get_image():

    return "Hello"


if __name__ == '__main__':
    app.run(debug=True)