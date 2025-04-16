from flask import Flask, request, jsonify
from functions import *

app = Flask(__name__)

@app.route('/download_audio', methods=['POST'])
def download_audio_m4a_route():
    url = request.form.get("url")
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    try:
        tag = determinate_best_audio_stream(url)
        download_audio_m4a(url, tag)
        convert_m4a_to_mp3(url)
        return jsonify({'message': 'Download started successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)