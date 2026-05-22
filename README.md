# 🎗️ BreastWise: ML-Powered Breast Cancer Detection

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=flat-square&logo=streamlit)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=flat-square&logo=scikit-learn)

> A machine learning web application that predicts whether a breast tumor is **Benign** or **Malignant** based on clinical tumor characteristics — built to make early detection more accessible.

---

## 🧠 About the Project

Breast cancer is one of the most common cancers worldwide. Early and accurate detection dramatically improves survival rates. **BreastWise** uses Logistic Regression trained on the well-established **Wisconsin Breast Cancer Dataset** to classify tumors based on 30 cellular features extracted from fine needle aspirate (FNA) images.

Users can input tumor measurements through a clean Streamlit interface and receive an instant prediction.

---

![App Screenshot](screenshot.png)

## ✨ Features

- 🔬 Predicts tumor type: **Benign** or **Malignant**
- 📊 Trained on the **Wisconsin Breast Cancer Dataset** (sklearn built-in)
- ⚖️ Input features pre-filled with dataset mean values for ease of use
- 🧪 Feature scaling using **StandardScaler** for accurate predictions
- 🖥️ Clean, interactive web UI powered by **Streamlit**

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Language | Python 3.8+ |
| ML Model | Logistic Regression (scikit-learn) |
| Preprocessing | StandardScaler |
| Dataset | Wisconsin Breast Cancer Dataset |
| Frontend | Streamlit |
| Numerics | NumPy |

---

## 📁 Project Structure

```
BreastWise/
│
├── app.py            # Streamlit UI — main entry point
├── model.py          # Model training and scaler logic
├── utils.py          # Input collection helper functions
└── requirements.txt  # Project dependencies
```

---

## ⚙️ How It Works

```
User Inputs 30 Tumor Features
            ↓
    StandardScaler (normalization)
            ↓
    Logistic Regression Model
            ↓
    Prediction: Benign / Malignant
```

1. The model loads the **Wisconsin Breast Cancer Dataset** directly via sklearn
2. Features are normalized using **StandardScaler**
3. A **Logistic Regression** classifier is trained on all 569 samples
4. User inputs are scaled and passed to the model for real-time prediction

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/BreastWise_ML_Powered_Cancer_Detection.git
cd BreastWise_ML_Powered_Cancer_Detection

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501`

---

## 🖥️ Usage

1. Launch the app with `streamlit run app.py`
2. You'll see 30 tumor feature input fields, pre-filled with average dataset values
3. Adjust the values based on clinical measurements
4. Click **"Predict"** to get the result — Benign or Malignant

---

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| Dataset | Wisconsin Breast Cancer (sklearn) |
| Samples | 569 |
| Features | 30 |
| Algorithm | Logistic Regression |
| Preprocessing | StandardScaler |

> 💡 Logistic Regression on this dataset typically achieves **~95%+ accuracy**. Run the model locally to see evaluation metrics.

---

## ⚠️ Disclaimer

> This tool is built for **educational purposes only**. It is **not a medical device** and should **not be used for actual clinical diagnosis**. Always consult a qualified medical professional for health-related decisions.

---

## 📦 Dependencies

```
streamlit
scikit-learn
numpy
```

---

## 🙋‍♂️ Author

**Malka Naaz**
- GitHub: [@Malka23](https://github.com/Malka23)
- LinkedIn: [LinkedIn](https://www.linkedin.com/in/malka-naaz-870338145)

---

📄 License
This project is licensed under the MIT License — see the LICENSE file for details.

---

⭐ **If you found this project helpful, please give it a star!**
