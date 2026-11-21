# Personal Portfolio — Flask

A responsive dark-theme portfolio built with Python, Flask, Jinja templates, and CSS.

## Personalize it first

Open `app.py` and update `PROFILE` with your real name, email, GitHub URL, LinkedIn URL, and introduction. Update `SKILLS` and replace the sample `PROJECTS` with work you have actually completed. Do not publish placeholder links.

## Run on Windows

Install Python 3.10+ and Git. In Command Prompt or PowerShell, open this folder and run:

```powershell
py -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python app.py
```

Visit http://127.0.0.1:5000.

## Upload to GitHub

1. Create a new repository at https://github.com/new named `my-portfolio`.
2. Keep it empty (do not add a README, license, or .gitignore there).
3. Open a terminal in this project folder and run:

```bash
git init
git add .
git commit -m "Build my Flask portfolio"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/my-portfolio.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your actual GitHub username. If Git asks you to sign in, complete the GitHub browser authentication prompt.

## Deploy the live Flask website with Render

GitHub stores your code; Render runs the Flask server and gives you a public website URL.

1. Sign in to https://render.com using your GitHub account.
2. Select **New** → **Web Service** and connect the `my-portfolio` repository.
3. Choose the Python runtime.
4. Build command: `pip install -r requirements.txt`
5. Start command: `gunicorn app:app`
6. Select a plan and click **Deploy**.
7. When deployment succeeds, Render displays a public URL such as `https://your-service-name.onrender.com`.

Render plan availability and free-tier limits can change. Check the current plan details before deploying.

## Important

- GitHub Pages does not run Flask/Python server applications. Use a Python host such as Render for this Flask project.
- The included project descriptions are starter examples. Only claim experience and projects you can explain and demonstrate.
- Never commit passwords, AWS access keys, secret keys, or other credentials.
