# SupportFlow Optimizer – CRM Workflow Dashboard

This is a Streamlit-based dashboard app that simulates CRM-style partner support workflows.

### Features
- Filter tickets by Department, Status, and Priority
- Live table view with real-time filtering
- Bar chart showing ticket status distribution
- Download filtered results as CSV

### Stack Used
- Python
- Streamlit
- Pandas

### Screenshot
![Dashboard](screenshot.png)

### Run Locally
Follow these steps to run the project on your local machine:

#### 1. Clone the Repository

```bash
git clone https://github.com/gracy1305/supportflow-optimizer.git
cd supportflow-optimizer
```

#### 2. (Optional) Create a Virtual Environment
```bash
python -m venv venv
```

Activate it:

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

#### 3. Install Dependencies
```bash
pip install streamlit pandas
```

#### 4. Run the App
```bash
streamlit run supportflow.py
```
Visit the URL shown in your terminal, usually http://localhost:8501

Project Structure
```bash
supportflow_project/
│
├── supportflow.py         # Main Streamlit app
├── README.md              # Project overview and instructions
└── screenshot.png         # Dashboard UI screenshot
 ```

### Deployment (Optional)
This app is deployed on Streamlit Cloud with the following:
- GitHub repository: gracy1305/supportflow-optimizer
- Main file: supportflow.py
- Custom subdomain: https://supportflow.streamlit.app

Gracy Patel
MS in Computer Science | DePaul University
GitHub: gracy1305
