
# 🏠 house-price-webapp

This is a sleek, filterable property listing platform built with **Flask**. It displays a curated list of houses in Salem, India, complete with details like interior style, room count, and dynamic price calculation.

---

## 🔧 Features

- 📷 Visual house listings with images and descriptions
- 🧠 Smart price calculator based on:
  - Square footage
  - Number of rooms
  - Quality of construction
- 🔍 Filter by:
  - Location
  - Number of Rooms (e.g., 2 BHK, 3 BHK)
  - Quality (Good, Very Good, Excellent)
- ↕️ Sort options:
  - Low to High Price
  - High to Low Price
- 📞 Contact page for inquiries

---

## 🛠️ Tech Stack

- **Backend**: Python + Flask
- **Templating**: Jinja2 (`render_template`)
- **Frontend**: HTML/CSS (with static image URLs from Unsplash)
- **Hosting**: Flask Development Server (`debug=True`)

---

## 🧠 How Pricing Works

Each house price is calculated using the formula:

Price = Area * Base Price per Sqft * Quality Multiplier + Room Count * Room Multiplier


- `Base Price per Sqft`: ₹2500
- `Room Multiplier`: ₹50,000
- `Quality Multipliers`:
  - Excellent: `1.3`
  - Very Good: `1.2`
  - Good: `1.1`
  - Average: `1.0`

---

## 🚀 Getting Started

### 🔹 Prerequisites

- Python 3.x
- Flask

### 🔹 Installation

```bash
git clone https://github.com/yourusername/real-estate-flask-app.git
cd real-estate-flask-app
pip install flask
🔹 Run the App
bash
Copy
Edit
python app.py
Visit: http://127.0.0.1:5000/

📁 Project Structure

real-estate-flask-app/
│
├── app.py                # Main Flask application
├── templates/
│   ├── index.html        # Homepage showing listings
│   └── contact.html      # Contact page
└── static/               # (Optional) For custom styles or assets
✨ Screenshots 





🧑‍💻 Author
Built with ❤️ by Deepak PS

📬 Contact
Feel free to reach out via LinkedIn or drop an issue if you find a bug!

📜 License
This project is open-source and available under the MIT License.



---


