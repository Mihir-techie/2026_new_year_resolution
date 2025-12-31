from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd
import os

app = Flask(__name__)

# Load trained model
model_path = os.path.join("model", "resolution_2026_model.pkl")
try:
    with open(model_path, "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    print(f"Warning: Model file not found at {model_path}")
    model = None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return render_template(
            "result.html",
            resolution="Error: Model not found. Please ensure the model file is in the model directory."
        )
    
    try:
        # Collect form data
        data = {
            "Gender": request.form["gender"],
            "Age": int(request.form["age"]),
            "Sleep Duration": float(request.form["sleep"]),
            "Quality of Sleep": int(request.form["sleep_quality"]),
            "Physical Activity Level": int(request.form["activity"]),
            "Stress Level": int(request.form["stress"]),
            "Daily Steps": int(request.form["steps"]),
            "BMI_Encoded": float(request.form["bmi"])
        }

        # Convert to DataFrame
        df = pd.DataFrame([data])

        # Encode categorical variables
        df = pd.get_dummies(df)

        # Align columns with training model
        model_features = model.feature_names_in_
        df = df.reindex(columns=model_features, fill_value=0)

        # Predict
        prediction = model.predict(df)[0]

        return render_template(
            "result.html",
            resolution=prediction
        )
    except Exception as e:
        return render_template(
            "result.html",
            resolution=f"Error processing your data: {str(e)}"
        )

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
