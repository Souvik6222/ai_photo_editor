# Pixverse AI Photo Editor

AI-powered image editing tools with a beautiful modern interface.

## 📁 Project Structure

```
ai_photo_editor/
├── index.html              # Entry point (redirects to pages/home.html)
├── css/                    # Stylesheets
│   └── shared-styles.css   # Common styles for all pages
├── js/                     # JavaScript files
│   └── shared-scripts.js   # Shared utility functions
├── pages/                  # HTML pages
│   ├── home.html          # Landing page
│   ├── remove-bg.html     # Background removal tool
│   ├── enhancement.html   # Photo enhancement
│   ├── effects.html       # Image effects
│   ├── editing.html       # Image editing
│   ├── content.html       # Content generation
│   ├── classification.html # Image classification
│   ├── conversion.html    # Format conversion
│   ├── surfacemap.html    # Surface mapping
│   ├── utilities.html     # Utility tools
│   ├── watermark.html     # Watermark tool
│   └── nav-template.html  # Navigation template
├── scripts/               # Python and build scripts
│   └── generate-pages.py  # Page generation script
└── docs/                  # Documentation
    ├── README.md          # Main documentation
    ├── ENHANCEMENT_GUIDE.md # Enhancement guide
    └── TEST_NOW.txt       # Testing instructions
```

## 🚀 Getting Started

1. Open `index.html` in your browser or navigate directly to `pages/home.html`
2. Choose a tool from the sidebar navigation
3. Upload an image and apply the desired effect

## 🛠️ Features

- **Remove Background** - AI-powered background removal
- **Photo Enhancement** - Upscale and enhance image quality
- **Effects** - Apply various visual effects
- **Editing** - Professional image editing tools
- **Content Generation** - AI-powered content creation
- **Format Conversion** - Convert between image formats
- **Watermark** - Add watermarks to images
- **And more...**

## 📝 Development

To generate new pages, run:
```bash
python scripts/generate-pages.py
```

## 🎨 Customization

- Modify `css/shared-styles.css` to change the global styling
- Edit `js/shared-scripts.js` to add shared functionality
- Update individual pages in the `pages/` directory

## 📄 License

This project uses the Picsart API. Make sure to replace API keys with your own.
