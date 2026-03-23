# OSI Logo Setup Instructions

## Quick Setup

1. **Save the OSI logo image** you just shared as `logo.png` in the OSIWeb folder:
   - Right-click the logo image in the chat
   - Choose "Save Image As..."
   - Navigate to: `/Users/jklahr/Cursor Priojects/OSIWeb/`
   - Name it: `logo.png`
   - Click Save

2. **Refresh your browser** - The logo will now appear in the navigation bar!

## Alternative: Use SVG (Recommended for scalability)

If you have the logo in SVG format:
1. Save it as `logo.svg` instead of `logo.png`
2. Update line 16 in `index.html`:
   - Change: `<img src="logo.png" ...`
   - To: `<img src="logo.svg" ...`

## Logo Styling

The logo is currently set to:
- Height: 50px
- Auto width (maintains aspect ratio)
- Subtle hover animation (scales 5% on hover)

To adjust the size, edit `styles.css` line 49:
```css
.logo-image {
    height: 50px;  /* Change this value */
    width: auto;
}
```

## Troubleshooting

**Logo not showing?**
- Check the filename matches exactly: `logo.png`
- Verify it's in the correct folder: `/Users/jklahr/Cursor Priojects/OSIWeb/`
- Hard refresh your browser: `Cmd + Shift + R`

**Logo too big/small?**
- Adjust the height value in `styles.css` (line 49)
- Try: 40px (smaller), 60px (larger), or 70px (even larger)

---

That's it! Your OSI logo is now integrated. ✨

