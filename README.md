# Cloud Computing Mini Project: Publish a Streamlit App Online

## What this project does
This is a one-file Streamlit text checker. It flags common spam-like phrases using simple rules, then shows:
- Three lines explaining IaaS, PaaS, and SaaS
- Why Streamlit Community Cloud is a PaaS example
- A three-row table of free-offer examples from AWS, Microsoft Azure, and Google Cloud

> The text checker is an educational rule-based demo, not a production spam filter or a trained ML model.

## Run locally
1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
4. Start the app:
   ```bash
   streamlit run app.py
   ```
5. Open the local URL shown in the terminal, usually `http://localhost:8501`.

## Publish it on GitHub
1. Create a new public GitHub repository, e.g. `cloud-streamlit-mini-project`.
2. Upload `app.py`, `requirements.txt`, and `README.md` to the repository root.
3. Make sure `app.py` is at the top level of the repository.

## Publish it on Streamlit Community Cloud
1. Visit https://share.streamlit.io/ and sign in with GitHub.
2. Select **Create app** (or **Deploy an app**).
3. Choose your repository, branch (usually `main`), and main file path `app.py`.
4. Click **Deploy** and wait for the build to finish.
5. Open the generated public app URL and test it.
6. Submit both the GitHub repository link and the deployed Streamlit app link if your teacher asks for them.

## Free-tier note
Cloud provider free offers change often and can vary by region, account, and eligibility. The app links to official AWS, Azure, and Google Cloud free pages; verify current terms before use.
