<h1>🧠 Facial Expression Recognition</h1>

<p>
<strong>Facial Expression Recognition</strong> is a project that uses a
<strong>trained Convolutional Neural Network (CNN)</strong> to identify human emotions from
grayscale face images.
It supports multiple emotion classes such as <strong>happy, sad, angry, surprised</strong>,
and more — and is deployed as an API using <strong>FastAPI</strong> for easy integration.
</p>

<h2> Project Overview</h2>
<p>
Facial Expression Recognition Model can classify facial expressions
from images using deep learning techniques.
It is trained on image data and can recognize common human emotions.
The model is wrapped inside a <strong>FastAPI</strong> backend so you can query it via HTTP
requests in real time.
</p>

<h2>📁 Repository Structure</h2>
<pre>
facial-expression-recognition/
├── Images/                  # Example images or screenshots
├── code/                    # Training and utility code
├── model/                   # Trained model data
├── template/                # Web or UI templates
├── .gitattributes
├── README.md
├── class_weights.json       # Class weights for model
├── config.pkl               # Configuration or other model info
├── main.py                  # FastAPI backend
├── requirements.txt         # Python dependencies
</pre>

<h2> Features</h2>
<ul>
  <li>Detects major facial emotions from images</li>
  <li>Uses a trained CNN model</li>
  <li>Easily deployable using <strong>FastAPI</strong></li>
</ul>

<h2> Tech Stack</h2>
<ul>
  <li>Python</li>
  <li>TensorFlow / Keras (CNN)</li>
  <li>Convolutional Neural Network</li>
  <li>FastAPI (Backend API)</li>
  <li>HTML / Frontend templates (if included)</li>
  <li>Jupyter Notebook / Python Scripts (for training)</li>
</ul>

<h2> How It Works</h2>
<ol>
  <li><strong>Input image</strong> — A face image is passed to the model.</li>
  <li><strong>Preprocessing</strong> — The image is prepared and normalized.</li>
  <li><strong>CNN Model</strong> — A trained CNN model predicts the emotion category.</li>
  <li><strong>Output</strong> — The API returns the predicted emotion label.</li>
</ol>

<h2>📦 Installation &amp; Setup</h2>

<h3>1. Clone the Repository</h3>
<pre>
git clone https://github.com/AzeemAIDev/facial-expression-recognition.git
cd facial-expression-recognition
</pre>

<h3>2. Install Dependencies</h3>
<pre>
pip install -r requirements.txt
</pre>

<h3>3. Run the FastAPI Server</h3>
<pre>
uvicorn main:app --reload
</pre>

<h3>4. Test the API</h3>
<p>Visit:</p>
<pre>
http://localhost:8000/docs
</pre>
<pre>
Right click on index.html select open with live server
</pre>
<p>
This opens the Swagger UI where you can try the API endpoints.
</p>

<h2> Testing &amp; Usage</h2>
<p>
You can send a face image to the API and receive a predicted emotion as JSON output.
Use tools like <strong>Postman</strong> or the <strong>Swagger UI</strong> to test.
</p>
<p>Example endpoint:</p>
<pre>
POST /predict
</pre>

<h2> Notes</h2>
<ul>
    <li>The model may not work perfectly with very noisy images.</li>
</ul>

<h2> Author</h2>
<p>
<strong>Azeem</strong><br>
ML Engineer &amp; AI Learner<br>
<a href="https://github.com/AzeemAIDev" target="_blank">
https://github.com/AzeemAIDev
</a>
</p>
