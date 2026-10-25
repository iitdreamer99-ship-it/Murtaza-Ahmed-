# MRTZIX — Python-powered website

A responsive, premium black-and-silver personal brand website built with Flask, HTML, CSS and a little JavaScript. Your uploaded logo is included at `static/mrtzix-logo.png`.

## Run locally

1. Install Python 3.10 or newer.
2. Open a terminal in this project folder.
3. Create and activate a virtual environment (optional but recommended):
   - Windows: `py -m venv .venv` then `.venv\Scripts\activate`
   - macOS/Linux: `python3 -m venv .venv` then `source .venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run: `python app.py`
6. Open `http://127.0.0.1:5000` in your browser.

## Before publishing

- The contact form is a demo only. It does not send or store messages. Connect a real form service or backend email provider before using it with customers.
- Replace the demo copy with your actual services, links and contact details.
- Use production settings when hosting publicly; do not run Flask's debug server on the public internet.
- Keep domain/hosting costs in mind. Free hosting availability and terms can change.

## Deploy with Render (one possible option)

1. Create a GitHub repository and upload the project files.
2. Sign in to Render and create a new **Web Service** connected to that repository.
3. Build command: `pip install -r requirements.txt`
4. Start command: `gunicorn app:app`
5. Add `gunicorn` to `requirements.txt` before deploying (for example, `Flask>=3.0,<4.0` and `gunicorn>=22,<24`).
6. Deploy and use the provided public URL. Add a custom domain only if you want one and understand its renewal cost.

For a quick static preview, you can also adapt the HTML/CSS to static hosting such as GitHub Pages, but Flask/Python routes will not run on GitHub Pages.
