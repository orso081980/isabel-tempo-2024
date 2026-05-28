# GitHub Pages Deployment Guide for Jira Track

## ✅ Code is Pushed to GitHub!

Your Jira Track application has been pushed to: **https://github.com/orso081980/isabel-tempo-2024**

## 🚀 Two Deployment Options:

### Option 1: Automatic Deployment with GitHub Actions (Recommended)

1. Go to your GitHub repository: https://github.com/orso081980/isabel-tempo-2024
2. Click on **Settings** → **Pages**
3. Under **Source**, select: **GitHub Actions**
4. Save the settings

The GitHub Actions workflow (`.github/workflows/deploy.yml`) will automatically:

- Build the app when you push changes to `jira-track/`
- Deploy to GitHub Pages

**Your site will be available at:** `https://orso081980.github.io/isabel-tempo-2024/jira-track/`

### Option 2: Manual Deployment with gh-pages

From the `jira-track` folder, run:

```bash
cd jira-track
npm run deploy
```

This will:

1. Build the production version
2. Deploy the `dist` folder to the `gh-pages` branch
3. Deploy to: `https://orso081980.github.io/isabel-tempo-2024/jira-track/`

**Note:** For this option, you need to:

1. Go to **Settings** → **Pages**
2. Under **Source**, select: **Deploy from a branch**
3. Select branch: **gh-pages** and folder: **/ (root)**

## 🔧 Configuration Details:

- **Base Path**: `/isabel-tempo-2024/jira-track/` (configured in `vite.config.js`)
- **Build Command**: `npm run build` (sets NODE_ENV=production)
- **Output Directory**: `jira-track/dist/`
- **Tailwind CSS**: v4.3.0 ✅ (properly configured with @tailwindcss/vite)

## 📝 Files Committed:

- ✅ All source files in `jira-track/`
- ✅ `.github/workflows/deploy.yml` (GitHub Actions workflow)
- ✅ `.gitignore` (excludes node_modules, dist, etc.)
- ✅ `package.json` with deploy script

**Note:** The `dist` folder is NOT committed (it's in .gitignore), which is correct. It will be built during deployment.

## 🛠️ Development:

To run locally:

```bash
cd jira-track
npm install
npm run dev
```

Visit: http://localhost:5173/

## ✨ Features:

- ✅ Vue.js 3 with Composition API
- ✅ Tailwind CSS v4 (properly working!)
- ✅ Vue Chart.js for professional charts
- ✅ SOLID principles & MVC architecture
- ✅ Separation of concerns (no logic in components)
- ✅ Custom colors: Purple (Isabel), Red (Finca), Cyan (Freetime)

---

**Ready to deploy!** Choose Option 1 (GitHub Actions) for automatic deployments, or Option 2 for manual control.
