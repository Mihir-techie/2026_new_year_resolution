from flask import Flask, render_template, request, jsonify
import joblib
import os

app = Flask(__name__)

# Load model (cross-platform path)
model_path = os.path.join("model", "new_year_resolution_model.pkl")
encoder_path = os.path.join("model", "resolution_encoder.pkl")

try:
    model = joblib.load(model_path)
    encoder = joblib.load(encoder_path)
except FileNotFoundError as e:
    print(f"Warning: Model file not found: {e}")
    model = None
    encoder = None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if model is None or encoder is None:
        return render_template(
            "result.html",
            resolution="Error: Model files not found. Please ensure model files are in the model directory."
        )
    
    try:
        # User inputs
        sleep_duration = float(request.form["sleep"])
        quality = int(request.form["sleep_quality"])
        activity = int(request.form["activity"])
        stress = int(request.form["stress"])
        steps = int(request.form["steps"])
        bmi = int(request.form["bmi"])

        # Defaults (realistic)
        heart_rate = 75
        bp_sys = 120
        bp_dia = 80

        # EXACT ORDER USED IN TRAINING
        user_input = [[
            sleep_duration,
            quality,
            activity,
            stress,
            heart_rate,
            steps,
            bp_sys,
            bp_dia,
            bmi
        ]]

        prediction = model.predict(user_input)
        result = encoder.inverse_transform(prediction)[0]

        return render_template("result.html", resolution=result)

    except Exception as e:
        return render_template("result.html", resolution=f"Error processing your data: {str(e)}")

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
