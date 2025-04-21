<h1>Heart Disease Prediction Project</h1> 

<p>This project uses machine learning to predict the likelihood of heart disease in individuals based on medical data. The prediction model is deployed using a user-friendly Streamlit app, enabling users to input patient data and receive predictions instantly.</p>

<h3>1. What the Project Does</h3>
<p>This project predicts the likelihood of heart disease in individuals using machine learning models. Users can input patient data (e.g., age, cholesterol level, blood pressure) into a Streamlit app, which outputs a probability of heart disease based on the trained model. It’s designed to provide quick and accurate insights for medical decision-making.
</p>

<h3>2. Tools/Languages Used</h3>
<ol>
  <li>Programming Language: <code>Python</code></li>
  <li>Libraries:-
    <ul>
      <li><code>pandas</code>: For data manipulation and analysis.</li>
      <li><code>scikit-learn</code>: For building and training the machine learning model</li>
      <li><code>Streamlit</code>: For creating the interactive web app.</li>
    </ul>
  </li>
  <li>Environment Management: <code>Conda</code> for managing dependencies.</li>
  <li>Dataset: <code>heart-disease.csv</code> for training the model.</li>
</ol>
<ul>
<h2>Steps to Build and Run</h2>
<ol>  
  <li>
    Clone the Repository:-
    <ul>
      <li>Download the project from GitHub using: <strong>git clone https://github.com/YourUsername/Heart-Disease-Prediction.git</strong></li>
    </ul>
  </li>
<li>
  Navigate to the Project Directory:-
  <ul>
    <li>Open the terminal and move to the project folder: <code>cd Heart-Disease-Prediction </code></li>
  </ul>
</li>
<li>
  Set Up the Environment:-
  <ul>
    <li>Create and activate the Conda environment using the <code>environment.yaml</code> file:</li>
    <li><strong>conda env create -f environment.yaml</strong></li>
    <li><strong>conda activate your_environment_name</strong></li>
  </ul>
</li>
<li>
  Run the App:-
  <ul>
    <li>Launch the Streamlit app using: <strong>streamlit run app.py</strong></li>
    <li>This will open the app in your browser. Input patient details to receive predictions.</li>
  </ul>
</li>
</ol>
<h3>3. Challenges and Key Features</h3>
<ul>
  <li>
    Challenges:
    <ul>
      <li>- <strong>Feature Selection</strong>: Identifying the most relevant predictors from the dataset.</li>
      <li><strong>Deployment</strong>: Ensuring the Streamlit app works seamlessly across different platforms.</li>
    </ul>
  </li>
  <li>
    Key Features:
    <ul>
      <li>- Interactive and user-friendly Streamlit interface.</li>
      <li>Machine learning model trained on medical data for heart disease prediction.</li>
      <li>Easy environment setup using the <code>environment.yaml</code> file for reproducibility.</li>
    </ul>
  </li>
</ul>
