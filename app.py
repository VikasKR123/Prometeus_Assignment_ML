from flask import Flask, render_template, request
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import prometheus_client  # Import Prometheus client for metrics
# import mlflow
app = Flask(__name__)


# model_uri = "models:/toxic_comment_model/1" 
# model = mlflow.pyfunc.load_model(model_uri)

# Load model and vectorizer
model = joblib.load("toxic_comment_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")  

# Initialize Prometheus metrics
REQUEST_COUNT = prometheus_client.Counter('request_count', 'Total number of requests')
COMMENT_COUNT = prometheus_client.Counter('comment_count', 'Total number of comments submitted')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        comment = request.form['comment']
        
        # Increment comment count
        COMMENT_COUNT.inc()
        
        # Increment request count
        REQUEST_COUNT.inc()
        
        comment_tfidf = tfidf.transform([comment])
        prediction = model.predict(comment_tfidf).tolist()[0]
        categories = ["Toxic", "Severe Toxic", "Obscene", "Threat", "Insult", "Identity Hate"]
        result = {categories[i]: bool(prediction[i]) for i in range(len(categories))} 
        
        return render_template('result.html', comment=comment, result=result)

@app.route('/metrics')
def metrics():
    return prometheus_client.generate_latest()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

