# Next Word Prediction Flask App

This project is a Flask web application that predicts the next word in a sentence using a TensorFlow-based LSTM model. The model is trained on a dataset of frequently asked questions (FAQs) and can generate text predictions based on user input.

## Features

- **Next Word Prediction**: Enter a sentence fragment, and the app predicts the next word using an LSTM neural network.
- **Pre-trained Model**: The application uses a pre-trained TensorFlow model and a tokenizer to generate predictions.
- **File Download**: Users can download a sample text file directly from the app.
- **Easy Deployment**: The app is built with Flask, making it easy to deploy and run on any platform.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. **Create a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask app:**
    ```bash
    python app.py
    ```

5. **Open your browser and visit:**
    ```
    http://127.0.0.1:5000/
    ```

## Usage

1. Open the web app in your browser.
2. Enter a sentence fragment in the input field.
3. Click "Predict" to see the next word predictions.
4. Download the sample text file by clicking the "Download Sample Text File" link.

## Model Details

- **Tokenizer**: The app uses a `Tokenizer` object saved in `tokenizer.pkl` to process and encode the input text.
- **LSTM Model**: The model is a sequential LSTM model trained on the FAQ dataset. The trained model is saved in `model.pkl`.

## Improvements

- **Larger Dataset**: To enhance prediction accuracy, consider training the model on a larger and more diverse dataset.
- **Extended Predictions**: The model currently generates a limited number of words; expanding this capability would make the predictions more coherent.

## Contributing

If you would like to contribute to this project, feel free to fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to [CampusX](https://learnwith.campusx.in/) for providing the FAQ dataset used to train the model.

