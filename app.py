from flask import Flask, request, jsonify, send_file
import os
import uuid
from functions import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify('pong'), 200

@app.route('/search_video', methods=['POST'])
def search_video_route():
    search = request.form.get("search")
    if not search:
        return jsonify({'error': 'Search term is required'}), 400

    try:
        video_list = search_video(search)
        return jsonify(video_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download_video', methods=['POST'])
def download_video_route():
    url = request.form.get("url")
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    try:
        download_video_highest_resolution(url)
        cleaned_filename = download_video_highest_resolution(url)

        filepath = f"./video/{cleaned_filename}.mp4"
        return send_file(
            filepath,
            mimetype='video/mp4',
            as_attachment=True,
            download_name=f'{cleaned_filename}.mp4'
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download_audio_m4a', methods=['POST'])
def download_audio_m4a_route():
    url = request.form.get("url")
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    try:
        tag = determinate_best_audio_stream(url)
        download_audio_m4a(url, tag)
        cleaned_filename = download_audio_m4a(url, tag)

        filepath = f"./audio/m4a/{cleaned_filename}.m4a"
        return send_file(
            filepath,
            mimetype='audio/m4a',
            as_attachment=True,
            download_name=f'{cleaned_filename}.m4a'
        )
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download_audio_mp3', methods=['POST'])
def download_audio_mp3_route():
    url = request.form.get("url")
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    try:
        tag = determinate_best_audio_stream(url)
        download_audio_m4a(url, tag)
        convert_m4a_to_mp3(url)
        cleaned_filename = download_audio_m4a(url, tag)

        filepath = f"./audio/{cleaned_filename}.mp3"
        return send_file(
            filepath,
            mimetype='audio/mp3',
            as_attachment=True,
            download_name=f'{cleaned_filename}.mp3'
        )
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5500", debug=True)