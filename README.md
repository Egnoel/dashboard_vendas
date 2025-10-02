# Sales Dashboard (dashboard_vendas)

A sales dashboard built with Python and Streamlit for visualizing sales data, metrics, and trends.

---

## 🚀 Demo

You can access the live version of the dashboard here:  
[dashboardvendas‑egnoel.streamlit.app](https://dashboardvendas‑egnoel.streamlit.app)

---

## 🧰 Features

- Data ingestion and preprocessing (CSV or structured datasets)  
- Interactive visualizations (charts, metrics, trends)  
- Filterable views by time periods, products, regions, etc.  
- Modular design with separate modules (e.g. `dataset.py`, `graficos.py`, `utils.py`)  
- Easily extensible to add new metrics, charts or data sources

---

## 📂 Repository Structure

```
dashboard_vendas/
├── pages/               ← (optional) supplementary Streamlit pages  
├── dados/                ← sample data / dataset files  
├── app.py                ← entry point of the Streamlit app  
├── dataset.py            ← data loading / preprocessing logic  
├── graficos.py           ← chart and plotting logic  
├── utils.py              ← utility/helper functions  
├── requirements.txt      ← Python dependencies  
└── .gitignore  
```

---

## ⚙️ Requirements & Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Egnoel/dashboard_vendas.git
   cd dashboard_vendas
   ```

2. (Optional) Create a Python virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On macOS / Linux
   # or
   venv\Scripts\activate      # On Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:

   ```bash
   streamlit run app.py
   ```

5. Open your browser at `http://localhost:8501` (by default).

---

## 🧩 How to Use / Extend

- Add or update datasets in the `dados/` folder.
- In `dataset.py`, implement or adjust data loading, cleaning, transformations.
- In `graficos.py`, define your charts or visualizations.
- In `utils.py`, place reusable helper functions (date handling, aggregations, formatting).
- Use Streamlit’s UI widgets in `app.py` to allow interactivity.

---

## ✅ Contributing

Contributions are welcome! Please open an issue or submit a pull request. 🎉

---

## 📝 License

MIT License  
© 2025 Egnoel

---

## 👤 Author

**Egnoel** — creator of this dashboard project ([GitHub Profile](https://github.com/Egnoel))

---
