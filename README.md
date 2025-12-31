# 🎯 AI Resolution Planner 2026

A beautiful, modern web application that uses AI to predict personalized New Year resolutions based on your health and lifestyle data.

## ✨ Features

- **Modern UI/UX**: Stunning glassmorphism design with smooth animations
- **AI-Powered Predictions**: Machine learning model that analyzes your health data
- **Interactive Forms**: Range sliders and real-time value updates
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Production Ready**: Optimized for deployment on Render

## 🚀 Live Demo

Deployed on Render: [Your App URL]

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **ML Model**: Scikit-learn
- **Deployment**: Render

## 📋 Prerequisites

- Python 3.11+
- pip
- Git

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/Mihir-techie/2026_new_year_resolution.git
cd 2026_new_year_resolution
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Ensure your model file is in the `model/` directory:
```
model/
  └── resolution_2026_model.pkl
```

5. Run the application:
```bash
python app.py
```

The app will be available at `http://localhost:5000`

## 🌐 Deployment on Render

### Option 1: Using render.yaml (Recommended)

1. Push your code to GitHub
2. Go to [Render Dashboard](https://dashboard.render.com)
3. Click "New +" → "Blueprint"
4. Connect your GitHub repository
5. Render will automatically detect `render.yaml` and deploy

### Option 2: Manual Deployment

1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name**: 2026-resolution-planner
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. Click "Create Web Service"

### Environment Variables

No environment variables are required for basic deployment.

## 📁 Project Structure

```
2026_new_year_resolution/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── render.yaml           # Render deployment config
├── templates/
│   ├── index.html        # Main form page
│   └── result.html       # Results page
├── static/
│   ├── css/
│   │   └── style.css     # Styling and animations
│   └── js/
│       └── main.js       # Interactive features
└── model/
    └── resolution_2026_model.pkl  # ML model
```

## 🎨 Features in Detail

### Frontend
- **Glassmorphism Design**: Modern frosted glass effect
- **Gradient Animations**: Smooth color transitions
- **Interactive Sliders**: Real-time value updates
- **Loading States**: Visual feedback during processing
- **Responsive Layout**: Mobile-first design approach

### Backend
- **Error Handling**: Graceful error management
- **Health Check Endpoint**: `/health` for monitoring
- **Production Configuration**: Optimized for deployment

## 🔒 Security Notes

- The app runs in production mode (debug=False) when deployed
- Input validation is handled by Flask forms
- Model file should be kept secure and not committed if sensitive

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 👤 Author

**Mihir-techie**
- GitHub: [@Mihir-techie](https://github.com/Mihir-techie)

## 🙏 Acknowledgments

- Flask community for the amazing framework
- Render for hosting platform
- All contributors and users

---

Made with ❤️ for a better 2026!

