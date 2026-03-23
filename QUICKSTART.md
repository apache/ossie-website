# OSI Website - Quick Start Guide 🚀

Get the OSI website running in seconds!

## Step 1: View the Website

Simply open the HTML file in your browser:

```bash
open /Users/jklahr/Cursor\ Priojects/OSIWeb/index.html
```

Or just double-click `index.html` in Finder!

## Step 2: Make It Live

### Option 1: GitHub Pages (Recommended)
1. Create a repo on GitHub
2. Push these files
3. Go to Settings → Pages
4. Select main branch
5. Your site will be live at `https://yourusername.github.io/OSI`

### Option 2: Netlify (Drag & Drop)
1. Go to [netlify.com](https://netlify.com)
2. Drag the OSIWeb folder onto their deploy zone
3. Done! Instant live URL

### Option 3: Vercel
```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
cd OSIWeb
vercel
```

## Step 3: Add Your Logo

When you have the logo ready:

1. Save it as `logo.png` in the OSIWeb folder
2. Edit `index.html` line 15-17, replace:
```html
<div class="nav-brand">
    <span class="logo-text">OSI</span>
    <span class="logo-subtitle">Open Semantic Interchange</span>
</div>
```

With:
```html
<div class="nav-brand">
    <img src="logo.png" alt="OSI Logo" style="height: 60px;">
</div>
```

## Step 4: Add Member Logos

To replace text with actual company logos:

1. Create a `logos` folder
2. Add company logo images (e.g., `aws.png`, `google.png`)
3. Edit the `.member-card` sections in `index.html`
4. Replace text with: `<img src="logos/aws.png" alt="AWS">`

## Customization Quick Reference

### Change Colors
Edit `styles.css` lines 11-15:
```css
--primary-blue: #29B5E8;
--dark-blue: #043464;
```

### Update Content
All content is in `index.html` - just search for the section and edit!

### Add Sections
Copy any `<section>` block and modify the content.

---

**That's it!** You now have a professional OSI website ready to go. 🎉

