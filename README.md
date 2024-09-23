# Web-portal-for-disease-identification


---


## Project Overview

This project is a web-based application that helps users detect diseases in livestock by inputting symptoms. The system uses an AI model that processes the symptom data and provides a prediction of the disease.

The frontend of the application is built using **HTML**, **CSS**, and **JavaScript**, and the development was done using **Visual Studio Code**. The backend is powered by a **Flask API**, which integrates an ai model created using **TensorFlow** in Python.

## Features (Current)

- **Symptoms Input**: Users can input symptoms of livestock, and the AI model predicts the disease based on the symptoms provided.
- **AI-based Disease Prediction (Symptoms)**: The AI model processes the symptoms data and provides a prediction of the likely disease.

## Features (Upcoming)

- **Image Upload and Prediction**: Users will be able to upload images of livestock, and the AI model will predict diseases based on the images.
- **Medication Recommendation**: Based on the predicted disease, the system will provide suggested medications.
- **Enhanced Disease Coverage**: Train the model to cover more diseases.
- **Mobile Responsiveness**: Improve the UI to make the website mobile-friendly.
- **User Authentication**: Add login functionality for secure access.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **AI Model**: TensorFlow (Python)
- **Development Environment**: Visual Studio Code, Python IDLE

## AI Model

The AI model was developed using **TensorFlow** to detect diseases based on the symptoms provided by the user. It uses advanced natural language processing techniques to make accurate predictions from the text input.

## Flask API

The backend is designed using **Flask**, which serves as the API that connects the frontend to the AI model. It processes the symptom data input, feeds it to the AI model, and returns the result back to the user.

## How to Run the Project

1. **Clone the Repository**:
   ```
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. **Install Dependencies**:
   Install the required Python libraries:
   ```
   pip install -r requirements.txt
   ```

3. **Run the Flask Server**:
   Start the Flask server by running the following command:
   ```
   python app.py
   ```

4. **Access the Application**:
   Open a web browser and go to:
   ```
   http://localhost:5000
   ```

## Folder Structure

```
- static/
  - css/
  - js/
  - images/
- templates/
  - index.html
- model/
  - disease_detection_model.h5
- app.py
- requirements.txt
- README.md
```

## Future Enhancements

- **Medication Recommendation**: Integrate recommendations for medications based on predicted diseases.
- **Additional Diseases**: Expand the model’s ability to predict a wider range of diseases.
- **Mobile Support**: Implement responsive design for mobile devices.
- **Authentication**: Add user authentication for a personalized experience.

## Contributing

Feel free to contribute by submitting a pull request or reporting issues.

## License

This project is licensed under the MIT License.

---
