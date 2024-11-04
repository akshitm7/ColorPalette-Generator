from flask import Flask, render_template, request, jsonify
import random
import colorsys
# Initialize the Flask application
app = Flask(__name__)
# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')
# Route to generate color palettes based on the base color and scheme
@app.route('/generate_palette', methods=['POST'])
def generate_palette():
    data = request.json
    base_color = data['baseColor']
    color_scheme = data['colorScheme']
    palette = []
    if color_scheme == "monochromatic":
        palette = generate_monochromatic_palette(base_color)
    elif color_scheme == "analogous":
        palette = generate_analogous_palette(base_color)
    elif color_scheme == "complementary":
        palette = generate_complementary_palette(base_color)
    return jsonify(palette)
def hex_to_rgb(hex):
    hex = hex.lstrip('#')
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)
def generate_monochromatic_palette(base_color):
    palette = [base_color]
    r, g, b = hex_to_rgb(base_color)
    for i in range(1, 5):
        variation = '#{:02x}{:02x}{:02x}'.format(
            min(max(0, r + i * 30), 255),
            min(max(0, g + i * 30), 255),
            min(max(0, b + i * 30), 255)
        )
        palette.append(variation)
    return palette
def generate_analogous_palette(base_color):
    palette = [base_color]
    r, g, b = hex_to_rgb(base_color)
    h, l, s = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
    for i in range(1, 5):
        new_h = (h + (i * 30) / 360) % 1.0 
        new_rgb = colorsys.hls_to_rgb(new_h, l, s)
        palette.append(rgb_to_hex((int(new_rgb[0] * 255), int(new_rgb[1] * 255), int(new_rgb[2] * 255))))
    return palette
def generate_complementary_palette(base_color):
    r, g, b = hex_to_rgb(base_color)
    comp_color = '#{:02x}{:02x}{:02x}'.format(255 - r, 255 - g, 255 - b)
    return [base_color, comp_color]
if __name__ == '__main__':
    app.run(debug=True)
