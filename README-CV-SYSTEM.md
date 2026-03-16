# Data-Driven CV System

This system maintains your CV in a single source of truth (YAML) and generates multiple output formats.

## 📁 Files

- **`cv-data.yaml`** - Your CV data (single source of truth)
- **`generate_html.py`** - Python script to generate ATS-friendly HTML
- **`cv-output.html`** - Generated HTML (can be printed to PDF)
- **`cv.tex`** - Your existing LaTeX CV (can be updated to read from YAML)

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install pyyaml
```

### 2. Edit Your CV Data

Edit `cv-data.yaml` with your information. This is the ONLY file you need to maintain!

### 3. Generate HTML Resume

```bash
python generate_html.py
```

This creates `cv-output.html`

### 4. Convert to PDF

Open `cv-output.html` in your browser and:
- Press `Ctrl+P` (Windows/Linux) or `Cmd+P` (Mac)
- Select "Save as PDF"
- Set margins to "Minimum" or "None"
- Enable "Background graphics"
- Save as `cv-ats-friendly.pdf`

## 📋 Workflow

```
┌─────────────────┐
│  cv-data.yaml   │  ← Edit this (single source of truth)
└────────┬────────┘
         │
         ├─────────────────┐
         │                 │
         ▼                 ▼
┌─────────────────┐  ┌──────────────┐
│ generate_html.py│  │  cv.tex      │
└────────┬────────┘  └──────┬───────┘
         │                  │
         ▼                  ▼
┌─────────────────┐  ┌──────────────┐
│ cv-output.html  │  │  cv.pdf      │
└────────┬────────┘  └──────────────┘
         │             (beautiful)
         ▼
┌─────────────────┐
│ cv-ats.pdf      │
└─────────────────┘
  (ATS-friendly)
```

## ✅ Benefits

1. **Single Source of Truth** - Edit CV data in one place
2. **Version Control** - Track changes with git
3. **Multiple Formats** - Generate ATS-friendly and beautiful versions
4. **Easy Maintenance** - No more syncing between different files
5. **Automation Ready** - Can be integrated into CI/CD

## 🎯 When to Use Which Version

- **`cv-ats.pdf`** (from HTML) - Use for online job applications (ATS systems)
- **`cv.pdf`** (from LaTeX) - Use for direct emails, networking, recruiters

## 📝 Customization

### Adding New Sections

Edit `cv-data.yaml` and add your section:

```yaml
awards:
  - name: "Best Developer Award"
    year: "2023"
    organization: "Company X"
```

Then update `generate_html.py` to render it.

### Styling the HTML

Edit the `<style>` section in `generate_html.py` to customize:
- Fonts (keep Arial, Calibri, or Garamond for ATS)
- Colors
- Spacing
- Layout

## 🔍 Testing ATS Compatibility

1. Generate your HTML and convert to PDF
2. Test with free tools:
   - [Resume Worded](https://resumeworded.com/resume-scanner)
   - [Targeted Resume](https://resumeworded.com/targeted-resume)
   - [AI Resume Judge](https://ayehigh.com/resume-judge)

3. Plain text test:
   - Open the PDF
   - Copy all text (Ctrl+A, Ctrl+C)
   - Paste into a plain text editor
   - Verify all information is readable and in correct order

## 🤖 GitHub Actions Integration

The repository includes a GitHub Actions workflow that automatically:
1. Generates the ATS-friendly HTML and converts it to PDF
2. Builds the LaTeX PDF version
3. Uploads both versions to your blog/website

### Workflow Files

- `.github/workflows/build.yml` - Main workflow that builds both versions

### What Gets Generated

- `cv.pdf` - Beautiful LaTeX version (for networking, direct emails)
- `cv-ats-friendly.pdf` - ATS-friendly version (for job applications)
- `cv-output.html` - HTML source (for preview)

### Accessing Your CVs

After the workflow runs:
- **Artifacts**: Download from GitHub Actions artifacts
- **Website**: Both PDFs are pushed to your blog at:
  - `https://yourblog.com/assets/cv.pdf` (LaTeX)
  - `https://yourblog.com/assets/cv-ats-friendly.pdf` (ATS)

## 🛠️ Advanced: Update LaTeX to Read YAML

You can update your LaTeX template to read from `cv-data.yaml` using:
- Python with Jinja2 templates
- LuaLaTeX with YAML parsing
- A simple Python script to generate `.tex` files

This keeps both versions in sync automatically!

## 📊 Comparison: Before vs After

### Before (LaTeX only)
- ❌ Not ATS-friendly
- ❌ Hard to maintain multiple versions
- ❌ Manual sync between formats
- ✅ Beautiful output

### After (Data-driven)
- ✅ ATS-friendly version available
- ✅ Easy to maintain (single YAML file)
- ✅ Automatic generation
- ✅ Beautiful LaTeX version still available
- ✅ Version controlled
- ✅ Automation ready

## 🤝 Contributing

Feel free to improve the generator script:
- Add more output formats (Markdown, JSON Resume, etc.)
- Improve HTML styling
- Add LaTeX generator from YAML
- Add validation for YAML data

## 📚 Resources

- [Tech Interview Handbook - Resume Guide](https://www.techinterviewhandbook.org/resume/)
- [ATS Resume Checklist](https://resumeworded.com/resume-scanner)
- [JSON Resume](https://jsonresume.org/) - Similar concept with JSON
