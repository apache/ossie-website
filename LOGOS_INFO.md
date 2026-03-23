# Company Logos Implementation

## How It Works

The website now displays actual company logos using the **Clearbit Logo API**, which automatically fetches company logos based on their domain names.

### Features
- ✅ **Automatic logo fetching** - No need to manually download logos
- ✅ **Smart fallback** - If a logo fails to load, company name displays instead
- ✅ **Optimized display** - Logos are sized to fit nicely (max 120px wide, 60px tall)
- ✅ **Hover effects** - Logos scale up slightly and cards lift on hover

## Logo Sources

Using: `https://logo.clearbit.com/[company-domain]`

Examples:
- AWS: `aws.amazon.com`
- Google: `google.com`
- Snowflake: `snowflake.com`
- dbt Labs: `getdbt.com`

## Customization

### Change Logo Size

Edit `styles.css` around line 238:

```css
.member-card img {
    max-width: 120px;   /* Adjust width */
    max-height: 60px;   /* Adjust height */
}
```

### Use Local Logos Instead

If you want to use downloaded logo files:

1. Create a `logos` folder in OSIWeb
2. Add logo files (e.g., `aws.png`, `google.png`)
3. Update `index.html`, change:
   ```html
   <img src="https://logo.clearbit.com/aws.amazon.com" alt="AWS">
   ```
   To:
   ```html
   <img src="logos/aws.png" alt="AWS">
   ```

### Add More Members

Copy this template and adjust:

```html
<div class="member-card">
    <img src="https://logo.clearbit.com/company-domain.com" 
         alt="Company Name" 
         onerror="this.parentElement.innerHTML='<span>Company Name</span>'">
</div>
```

## Current Members (29 total)

1. AWS
2. Alation
3. Atlan
4. BlackRock
5. Blue Yonder
6. Collibra
7. Cube
8. DataHub
9. dbt Labs
10. Domo
11. Elementum AI
12. Firebolt
13. Google
14. Hex
15. Honeydew
16. Informatica
17. Instacart
18. JPMC
19. Mistral AI
20. Omni
21. Preset
22. RelationalAI
23. Salesforce
24. Select Star
25. Sigma
26. Snowflake
27. Starburst Data
28. Strategy
29. ThoughtSpot

## Troubleshooting

**Logo not loading?**
- Check if the domain is correct
- Try the company's main domain (e.g., `.com` vs `.io`)
- The fallback will show the company name instead

**Logo looks blurry?**
- Clearbit provides the best available logo
- Consider using a local high-res version for important logos

**Want uniform logo colors?**
- Add a CSS filter in `styles.css`:
  ```css
  .member-card img {
      filter: grayscale(100%);  /* Black & white */
  }
  .member-card:hover img {
      filter: grayscale(0%);    /* Color on hover */
  }
  ```

---

All logos automatically update and are cached by the browser! 🎨

