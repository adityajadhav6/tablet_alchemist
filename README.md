
# 💊 Tablet Alchemist

A Flask-based web application that recommends tablets based on user-input health conditions. It provides detailed information for each medicine and a clean, interactive UI.

---

## 🗂️ Project Structure

```
.
├── README.md                 # Project documentation  
├── main.py                   # Application entry point  
├── requirements.txt          # Python dependencies  
├── src/                      # Source code  
│   ├── alchemist.py          # Core logic for recommendations and tablet details  
│   ├── routes.py             # Flask routes  
│   ├── utils.py              # Utility functions  
│   └── data/  
│       └── drug_database.json # Medicine database  
├── templates/                # HTML templates  
│   ├── index.html            # Homepage  
│   ├── details.html          # Tablet details page  
│   └── search_results.html   # Search results page  
├── static/                   # Static files (CSS, images)  
│   └── styles.css            # Custom styles  
└── tests/  
    └── test_alchemist.py     # Test cases for core logic  
```
---
Live Demo: https://tablet-alchemist-adityajadhav6-adityajadhav6s-projects.vercel.app
---
---

## 🚀 Installation

### ✅ Prerequisites

* Python 3.8 or higher
* `pip` (Python package manager)

### 🛠️ Steps

```bash
# 1. Clone the repository
git clone https://github.com/your-username/tablet-alchemist.git
cd tablet-alchemist

# 2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the application
python3 main.py
```

Open your browser and go to:
👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 💡 Usage

* **Homepage**: Enter a health condition to get tablet recommendations.
* **Search Results**: Displays tablets matching the condition.
* **Tablet Details**: Click a tablet to view age suitability, image, and more.

---

## 🧪 Testing

To run unit tests:

```bash
python -m unittest discover tests
```

---

## 📦 Data

The application uses `drug_database.json` for medicine details. Each entry contains:

* Tablet Name
* Image Path
* Age Suitability
* Additional Info (optional)

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a new branch (`feature/your-feature`)
3. Commit your changes
4. Push and open a pull request

---
## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](./LICENSE) file.

