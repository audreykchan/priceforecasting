<h1 align="center">Price Modeling and Forecasting Dashboard</h1>

<p align="center">
  <i>An interactive Streamlit app to explore pricing strategies using transaction data.</i><br>
  Built to help product teams, pricing analysts, and B2B businesses understand how price affects demand and revenue.
</p>

---

## <strong>Live Demo</strong>

<p>
Try the dashboard live on <a href="https://audreykchan-priceforecasting-price-tool-xmtp6p.streamlit.app/" target="_blank"><strong>Streamlit Cloud</strong></a> 
</p>

---

##  <strong>Use Cases</strong>

<ul>
  <li><b>B2B Product Teams</b>: Identify optimal pricing strategies using historical sales data</li>
  <li><b>Retail & POS Startups</b>: Explore category-level demand sensitivity and revenue modeling</li>
  <li><b>Data Analysts</b>: Visualize real-world demand curves and calculate elasticity</li>
  <li><b>Founders & Operators</b>: Forecast revenue outcomes from price experiments</li>
</ul>

---

## <strong>What It Does</strong>

- Visualizes real & modeled demand curves from POS data  
- Estimates price elasticity using regression and economics  
- Filters by product category to isolate patterns  
- Automatically identifies optimal pricing zones  
- Exports graphs and filtered datasets  

---

##  <strong>Project Structure</strong>

```bash
├── price_tool.py          # Main Streamlit app
├── pos_transactions.csv   # Sample transaction data
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
