# OSI Website

Official website for the Open Semantic Interchange (OSI) initiative.

## About OSI

The OSI initiative is a collaborative, open-source effort dedicated to standardizing and streamlining semantic model exchange and utilization across the diverse array of tools and platforms within the data analytics, AI, and BI ecosystem.

## Website Structure

- **Home Page**: Hero section with value proposition
- **About**: Overview of the OSI initiative and core features
- **Why OSI**: Problem statement and solution benefits
- **Members**: Contributing member organizations and companies
- **Specification**: Technical details, roadmap, and GitHub links
- **Get Involved**: Ways to contribute and participate

## Features

- Modern, responsive design
- Snowflake-inspired color scheme
- Smooth scrolling navigation
- Interactive animations
- Mobile-friendly layout
- Clean, professional aesthetic

## Technology Stack

- HTML5
- CSS3 (with CSS Variables)
- Vanilla JavaScript
- No external dependencies

## Local Development

Simply open `index.html` in your web browser. No build process or server required!

```bash
# On macOS
open index.html

# On Linux
xdg-open index.html

# On Windows
start index.html
```

## Deployment

This is a static website that can be deployed to any web hosting service:

- GitHub Pages
- Netlify
- Vercel
- AWS S3 + CloudFront
- Any traditional web server

## Customization

### Colors

Edit CSS variables in `styles.css`:

```css
:root {
    --primary-blue: #29B5E8;
    --dark-blue: #043464;
    --navy: #0E1C3D;
    /* ... more colors */
}
```

### Content

Edit `index.html` to update:
- Text content
- Section structure
- Links
- Member organizations

### Adding a Logo

Replace the text logo in the navbar section of `index.html` with an `<img>` tag:

```html
<div class="nav-brand">
    <img src="path/to/logo.png" alt="OSI Logo" class="logo-image">
</div>
```

Then add CSS for the logo:

```css
.logo-image {
    height: 50px;
    width: auto;
}
```

## Future Enhancements

- [ ] Add actual member company logos (with images)
- [ ] Interactive specification visualizer
- [ ] Blog/news section
- [ ] Documentation portal
- [ ] Community forum integration
- [ ] Real examples and use cases
- [ ] Video content section

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

- Code: Apache 2.0
- Documentation: Creative Commons Attribution (CC BY)

## Contact

For questions or suggestions, please open an issue on the [OSI GitHub repository](https://github.com/open-semantic-interchange/OSI).

---

Built with ❄️ for the OSI community

