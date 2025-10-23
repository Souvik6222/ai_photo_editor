#!/usr/bin/env python3
"""
Generate all feature pages for Pixverse ai Tools
Run this script to create all remaining HTML pages
"""

pages = [
    {
        'filename': 'enhancement.html',
        'title': 'Photo Enhancement',
        'icon': '✨',
        'subtitle': 'Enhance image quality with AI-powered tools',
        'api_endpoint': 'https://api.picsart.io/tools/1.0/enhance',
        'loading_text': '✨ Enhancing your image with AI...',
        'success_text': '✅ Image enhanced successfully!',
        'form_params': """
                formData.append('image', file);
                formData.append('enhance_type', 'ultra'); // or 'upscale'
                formData.append('format', 'PNG');"""
    },
    {
        'filename': 'effects.html',
        'title': 'Image Effects',
        'icon': '🎭',
        'subtitle': 'Apply stunning visual effects to your images',
        'api_endpoint': 'https://api.picsart.io/tools/1.0/effects',
        'loading_text': '🎭 Applying effects...',
        'success_text': '✅ Effects applied successfully!',
        'form_params': """
                formData.append('image', file);
                formData.append('effect_name', 'blur'); // Change effect type
                formData.append('format', 'PNG');"""
    },
    {
        'filename': 'editing.html',
        'title': 'Image Editing',
        'icon': '✂️',
        'subtitle': 'Professional image editing tools',
        'api_endpoint': 'https://api.picsart.io/tools/1.0/edit',
        'loading_text': '✂️ Editing your image...',
        'success_text': '✅ Image edited successfully!',
        'form_params': """
                formData.append('image', file);
                formData.append('format', 'PNG');"""
    },
    {
        'filename': 'content.html',
        'title': 'Content Generation',
        'icon': '🎨',
        'subtitle': 'AI-powered content generation',
        'api_endpoint': 'https://api.picsart.io/tools/1.0/generate',
        'loading_text': '🎨 Generating content...',
        'success_text': '✅ Content generated successfully!',
        'form_params': """
                formData.append('image', file);
                formData.append('format', 'PNG');"""
    },
    {
        'filename': 'conversion.html',
        'title': 'Format Conversion',
        'icon': '🔄',
        'subtitle': 'Convert images between different formats',
        'api_endpoint': 'https://api.picsart.io/tools/1.0/convert',
        'loading_text': '🔄 Converting format...',
        'success_text': '✅ Format converted successfully!',
        'form_params': """
                formData.append('image', file);
                formData.append('format', 'PNG'); // Change to desired format"""
    },
    {
        'filename': 'surfacemap.html',
        'title': 'Surfacemap',
        'icon': '🗺️',
        'subtitle': 'Create surface maps from images',
        'api_endpoint': 'https://api.picsart.io/tools/1.0/surfacemap',
        'loading_text': '🗺️ Creating surface map...',
        'success_text': '✅ Surface map created successfully!',
        'form_params': """
                formData.append('image', file);
                formData.append('format', 'PNG');"""
    },
    {
        'filename': 'watermark.html',
        'title': 'Watermark',
        'icon': '💧',
        'subtitle': 'Add or remove watermarks',
        'api_endpoint': 'https://api.picsart.io/tools/1.0/watermark',
        'loading_text': '💧 Processing watermark...',
        'success_text': '✅ Watermark processed successfully!',
        'form_params': """
                formData.append('image', file);
                formData.append('format', 'PNG');"""
    },
    {
        'filename': 'classification.html',
        'title': 'Image Classification',
        'icon': '🏷️',
        'subtitle': 'Classify and tag images with AI',
        'api_endpoint': 'https://api.picsart.io/tools/1.0/classify',
        'loading_text': '🏷️ Classifying image...',
        'success_text': '✅ Image classified successfully!',
        'form_params': """
                formData.append('image', file);"""
    },
    {
        'filename': 'utilities.html',
        'title': 'Utilities',
        'icon': '🛠️',
        'subtitle': 'Additional utility tools',
        'api_endpoint': 'https://api.picsart.io/tools/1.0/utilities',
        'loading_text': '🛠️ Processing...',
        'success_text': '✅ Processing completed successfully!',
        'form_params': """
                formData.append('image', file);
                formData.append('format', 'PNG');"""
    }
]

# Navigation menu HTML
nav_menu = '''<aside class="sidebar" id="sidebar">
        <div class="sidebar-header">
            <h2>🎨 Pixverse ai</h2>
            <p>Programmable Image Tools</p>
        </div>
        <nav class="sidebar-menu">
            <a href="home.html" class="menu-item">
                <span class="menu-item-icon">🏠</span>
                <span class="menu-item-text">Home</span>
            </a>
            
            <div class="menu-divider"></div>
            <div class="menu-section-title">Image Tools</div>
            
            <a href="remove-bg.html" class="menu-item">
                <span class="menu-item-icon">🖼️</span>
                <span class="menu-item-text">Remove Background</span>
            </a>
            
            <a href="enhancement.html" class="menu-item">
                <span class="menu-item-icon">✨</span>
                <span class="menu-item-text">Photo Enhancement</span>
            </a>
            
            <a href="effects.html" class="menu-item">
                <span class="menu-item-icon">🎭</span>
                <span class="menu-item-text">Effects</span>
            </a>
            
            <a href="editing.html" class="menu-item">
                <span class="menu-item-icon">✂️</span>
                <span class="menu-item-text">Editing</span>
            </a>
            
            <a href="content.html" class="menu-item">
                <span class="menu-item-icon">🎨</span>
                <span class="menu-item-text">Content Generation</span>
            </a>
            
            <a href="conversion.html" class="menu-item">
                <span class="menu-item-icon">🔄</span>
                <span class="menu-item-text">Conversion</span>
            </a>
            
            <a href="surfacemap.html" class="menu-item">
                <span class="menu-item-icon">🗺️</span>
                <span class="menu-item-text">Surfacemap</span>
            </a>
            
            <a href="watermark.html" class="menu-item">
                <span class="menu-item-icon">💧</span>
                <span class="menu-item-text">Watermark</span>
            </a>
            
            <a href="classification.html" class="menu-item">
                <span class="menu-item-icon">🏷️</span>
                <span class="menu-item-text">Classification</span>
            </a>
            
            <a href="utilities.html" class="menu-item">
                <span class="menu-item-icon">🛠️</span>
                <span class="menu-item-text">Utilities</span>
            </a>
            
            <div class="menu-divider"></div>
            
            <!-- Sidebar Advertisement -->
            <div style="text-align: center; padding: 20px 10px;">
                <script type="text/javascript">
                    atOptions = {
                        'key' : '6239817a5426bca1b12532f991ab457e',
                        'format' : 'iframe',
                        'height' : 50,
                        'width' : 320,
                        'params' : {}
                    };
                </script>
                <script type="text/javascript" src="//www.highperformanceformat.com/6239817a5426bca1b12532f991ab457e/invoke.js"></script>
            </div>
        </nav>
    </aside>'''

def generate_page(page_info):
    # Update nav menu to mark current page as active
    nav = nav_menu.replace(f'href="{page_info["filename"]}" class="menu-item"', 
                           f'href="{page_info["filename"]}" class="menu-item active"')
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{page_info["title"]} - Pixverse ai</title>
    <link rel="stylesheet" href="shared-styles.css">
</head>
<body>
    <div class="particles" id="particles"></div>
    <button class="menu-toggle" id="menuToggle">☰</button>
    
    <!-- Sidebar Navigation -->
    {nav}
    
    <!-- Main Content -->
    <main class="main-content">
        <div class="container">
            <div class="header">
                <h1>{page_info["icon"]} {page_info["title"]}</h1>
                <p class="subtitle">{page_info["subtitle"]}</p>
            </div>
            
            <!-- Top Banner Ad -->
            <div style="text-align: center; margin: 20px 0;">
                <script type="text/javascript">
                    atOptions = {{
                        'key' : '88a30d558b0ce128650a58dd786d60f2',
                        'format' : 'iframe',
                        'height' : 90,
                        'width' : 728,
                        'params' : {{}}
                    }};
                </script>
                <script type="text/javascript" src="//www.highperformanceformat.com/88a30d558b0ce128650a58dd786d60f2/invoke.js"></script>
            </div>
            
            <div class="upload-area" id="uploadArea">
                <div class="upload-icon">📤</div>
                <p>Click or drag & drop an image here</p>
                <p class="hint">Supports JPG, PNG, WEBP • Max 10MB</p>
            </div>
            
            <input type="file" id="fileInput" accept="image/*">
            
            <div class="loading" id="loading">
                <div class="spinner"></div>
                <p class="loading-text">{page_info["loading_text"]}</p>
            </div>
            
            <div class="error" id="error"></div>
            <div class="success" id="success"></div>
            
            <div class="preview-area" id="previewArea">
                <div class="preview-container">
                    <div class="preview-box">
                        <h3>📷 Original Image</h3>
                        <div class="image-wrapper">
                            <img id="originalImg" alt="Original">
                        </div>
                    </div>
                    <div class="preview-box">
                        <h3>🎨 Result</h3>
                        <div class="image-wrapper">
                            <span class="image-badge">✨ AI Processed</span>
                            <img id="resultImg" alt="Result">
                        </div>
                    </div>
                </div>
                
                <div class="stats" id="stats">
                    <div class="stat-item">
                        <span class="stat-value" id="fileSize">-</span>
                        <span>File Size</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-value" id="dimensions">-</span>
                        <span>Dimensions</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-value" id="processTime">-</span>
                        <span>Process Time</span>
                    </div>
                </div>
                
                <!-- Content Advertisement -->
                <div style="text-align: center; margin: 30px 0; padding: 20px; background: linear-gradient(145deg, #f8f9ff, #ffffff); border-radius: 15px;">
                    <script async="async" data-cfasync="false" src="//pl27910130.effectivegatecpm.com/bfad7f3288af73bf1c7d772d5671a0bd/invoke.js"></script>
                    <div id="container-bfad7f3288af73bf1c7d772d5671a0bd"></div>
                </div>
                
                <div class="buttons">
                    <button class="btn" id="downloadBtn">⬇️ Download Result</button>
                    <button class="btn" id="newImageBtn">🔄 Upload New Image</button>
                </div>
            </div>
        </div>
    </main>

    <script src="shared-scripts.js"></script>
    <script>
        // API Configuration
        const API_KEY = 'YOUR_API_KEY_HERE'; // TODO: Replace with your Pixverse ai key
        const API_ENDPOINT = '{page_info["api_endpoint"]}';

        // DOM Elements
        const uploadArea = document.getElementById('uploadArea');
        const fileInput = document.getElementById('fileInput');
        const loading = document.getElementById('loading');
        const previewArea = document.getElementById('previewArea');
        const originalImg = document.getElementById('originalImg');
        const resultImg = document.getElementById('resultImg');
        const downloadBtn = document.getElementById('downloadBtn');
        const newImageBtn = document.getElementById('newImageBtn');
        const stats = document.getElementById('stats');
        const fileSize = document.getElementById('fileSize');
        const dimensions = document.getElementById('dimensions');
        const processTime = document.getElementById('processTime');

        let resultUrl = '';
        let startTime = 0;

        // Upload Area Click
        uploadArea.addEventListener('click', () => {{
            fileInput.click();
        }});

        // Drag and Drop
        uploadArea.addEventListener('dragover', (e) => {{
            e.preventDefault();
            uploadArea.classList.add('dragover');
        }});

        uploadArea.addEventListener('dragleave', () => {{
            uploadArea.classList.remove('dragover');
        }});

        uploadArea.addEventListener('drop', (e) => {{
            e.preventDefault();
            uploadArea.classList.remove('dragover');
            const file = e.dataTransfer.files[0];
            if (file && file.type.startsWith('image/')) {{
                handleImage(file);
            }} else {{
                showError('Please drop a valid image file');
            }}
        }});

        // File Input Change
        fileInput.addEventListener('change', (e) => {{
            const file = e.target.files[0];
            if (file) handleImage(file);
        }});

        // Handle Image Processing
        async function handleImage(file) {{
            // Validate file size
            if (file.size > 10 * 1024 * 1024) {{
                showError('File size exceeds 10MB limit');
                return;
            }}

            startTime = Date.now();

            // Show original image
            const reader = new FileReader();
            reader.onload = (e) => {{
                originalImg.src = e.target.result;
                const img = new Image();
                img.onload = () => {{
                    dimensions.textContent = `${{img.width}}x${{img.height}}`;
                }};
                img.src = e.target.result;
            }};
            reader.readAsDataURL(file);

            fileSize.textContent = formatFileSize(file.size);

            // Show loading
            uploadArea.style.display = 'none';
            loading.style.display = 'block';
            previewArea.style.display = 'none';

            try {{
                // Check API key
                if (API_KEY === 'YOUR_API_KEY_HERE') {{
                    throw new Error('Please add your Pixverse ai key in the code');
                }}

                // Prepare form data
                const formData = new FormData();
{page_info["form_params"]}

                // API Request
                const response = await fetch(API_ENDPOINT, {{
                    method: 'POST',
                    headers: {{
                        'accept': 'application/json',
                        'X-Picsart-API-Key': API_KEY
                    }},
                    body: formData
                }});

                const data = await response.json();

                if (data.status === 'success' && data.data && data.data.url) {{
                    resultUrl = data.data.url;
                    resultImg.src = resultUrl;
                    
                    const endTime = Date.now();
                    const timeTaken = ((endTime - startTime) / 1000).toFixed(2);
                    processTime.textContent = `${{timeTaken}}s`;
                    
                    loading.style.display = 'none';
                    previewArea.style.display = 'block';
                    stats.style.display = 'block';
                    showSuccess('{page_info["success_text"]}');
                }} else {{
                    throw new Error(data.message || 'Processing failed');
                }}
            }} catch (err) {{
                loading.style.display = 'none';
                uploadArea.style.display = 'block';
                showError(err.message);
                console.error(err);
            }}
        }}

        // Download Result
        downloadBtn.addEventListener('click', async () => {{
            if (resultUrl) {{
                try {{
                    downloadBtn.disabled = true;
                    downloadBtn.textContent = '⏳ Downloading...';
                    
                    const response = await fetch(resultUrl);
                    const blob = await response.blob();
                    const url = window.URL.createObjectURL(blob);
                    const a = document.createElement('a');
                    a.href = url;
                    a.download = `result-${{Date.now()}}.png`;
                    document.body.appendChild(a);
                    a.click();
                    document.body.removeChild(a);
                    window.URL.revokeObjectURL(url);
                    
                    downloadBtn.textContent = '✅ Downloaded!';
                    setTimeout(() => {{
                        downloadBtn.disabled = false;
                        downloadBtn.textContent = '⬇️ Download Result';
                    }}, 2000);
                }} catch (err) {{
                    downloadBtn.disabled = false;
                    downloadBtn.textContent = '⬇️ Download Result';
                    showError('Failed to download image');
                }}
            }}
        }});

        // Upload New Image
        newImageBtn.addEventListener('click', () => {{
            previewArea.style.display = 'none';
            stats.style.display = 'none';
            uploadArea.style.display = 'block';
            fileInput.value = '';
            resultUrl = '';
        }});
    </script>
</body>
</html>'''
    
    return html

# Generate all pages
if __name__ == '__main__':
    for page in pages:
        html_content = generate_page(page)
        with open(page['filename'], 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"✅ Created {page['filename']}")
    
    print("\n🎉 All pages generated successfully!")
    print("\nNext steps:")
    print("1. Add your Pixverse ai key to each page")
    print("2. Test each feature")
    print("3. Customize API parameters as needed")
