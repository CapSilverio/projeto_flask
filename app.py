from flask import Flask, request, render_template
import base64
import json
from datetime import datetime
import os

app = Flask(__name__)

# Garante que as pastas para salvar dados existam
os.makedirs("images", exist_ok=True)
os.makedirs("locations", exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_data', methods=['POST'])
def upload_data():
    data = request.json
    location = data.get('location')
    image_data = data.get('image')  # base64-encoded image

    # Timestamp para nomes únicos
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Salvar imagem em PNG
    if image_data:
        image_path = f"images/captured_image_{timestamp}.png"
        with open(image_path, "wb") as f:
            f.write(base64.b64decode(image_data.split(",")[1]))

    # Salvar localização em JSON
    if location:
        location_path = f"locations/location_data_{timestamp}.json"
        with open(location_path, "w") as f:
            json.dump(location, f)

    return 'Dados recebidos com sucesso', 200

if __name__ == '__main__':
    app.run(debug=True)
