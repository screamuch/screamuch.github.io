# Personal Website - Peter Chudinov

A minimal, clean personal website built with HTML and CSS.

## What You Need to Customize

### 1. Update Links in `index.html`

Search for these placeholders and replace with your actual links:

- `your.email@example.com` - Your email address
- `https://scholar.google.com/your-profile` - Your Google Scholar profile
- `https://github.com/yourusername` - Your GitHub username
- `https://linkedin.com/in/yourprofile` - Your LinkedIn profile

### 2. Add Project Images

Place your project images in the `images/` folder with these filenames:
- `robocam.jpg` (or .png)
- `neural-interface.jpg` (or .png)
- `single-cell.jpg` (or .png)
- `music-ai.jpg` (or .png)

If you use .png instead of .jpg, update the image src in `index.html`.

### 3. Update Project Links

For each project, replace the `#` placeholders with actual URLs:
- Paper links
- Code repositories (GitHub)
- Demo videos
- Project websites

### 4. Fine-tune Content

- Adjust project descriptions if needed
- Add/remove publications from the list
- Update bio text if you want to change the wording

## How to View Locally

Just open `index.html` in your web browser. Double-click the file or:

```bash
open index.html  # macOS
```

## How to Deploy

### Option 1: GitHub Pages
1. Create a new repository on GitHub
2. Push these files to the repository
3. Go to Settings > Pages
4. Select main branch as source
5. Your site will be at `https://yourusername.github.io/repo-name`

### Option 2: Custom Domain (you have one!)
1. Upload files to your web host
2. Point your domain to the hosting
3. Done!

### Option 3: Netlify (easiest)
1. Drag and drop this folder to netlify.com/drop
2. Connect your custom domain in Netlify settings

## File Structure

```
personal-website/
├── index.html       # Main HTML file
├── style.css        # Styling
├── images/          # Project images go here
│   ├── robocam.jpg
│   ├── neural-interface.jpg
│   ├── single-cell.jpg
│   └── music-ai.jpg
└── README.md        # This file
```

## Notes

- The design is minimal and clean (inspired by akarshkumar.com)
- Mobile-responsive
- No JavaScript needed
- Light gray background (#ededed) with single-column layout
- All styling can be adjusted in `style.css`
