from flask import Flask, render_template, request, jsonify
import sys
import traceback
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

try:
    import joblib
    from sklearn.feature_extraction.text import TfidfVectorizer
except ImportError as e:
    app.logger.error(f"Error: {e}")
    app.logger.error("Please install the required libraries using:")
    app.logger.error("pip install scikit-learn joblib")
    sys.exit(1)

try:
    # Load the saved model and vectorizer
    model = joblib.load('disease_classifier_model.pkl')
    vectorizer = joblib.load('tfidf_vectorizer.pkl')
except FileNotFoundError as e:
    app.logger.error(f"Error: {e}")
    app.logger.error("Make sure 'disease_classifier_model.pkl' and 'tfidf_vectorizer.pkl' are in the same directory as this script.")
    sys.exit(1)

@app.route('/')
def home():
    try:
        return render_template('index.html')
    except Exception as e:
        app.logger.error(f"Error rendering template: {e}")
        app.logger.error(traceback.format_exc())
        return f"An error occurred: {str(e)}", 500

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.form
        description = data.get('symptoms')
        crop_livestock_type = data.get('type')

        # Transform the input description using the loaded vectorizer
        description_vectorized = vectorizer.transform([description])
        
        # Predict using the loaded model
        prediction = model.predict(description_vectorized)[0]
        
        return jsonify({
            'prediction': prediction,
            'type': crop_livestock_type
        })
    except Exception as e:
        app.logger.error(f"An error occurred: {e}")
        app.logger.error(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
