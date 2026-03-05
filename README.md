# file_type_changer
This Python engine handles local file conversions securely. It bridges formats like DOCX, MD, and PDF using pypandoc and ReportLab. Featuring a pathlib-driven I/O, it defaults to Downloads but allows custom paths and filenames. It’s a clean, modular solution for text scraping and rendering without third-party websites.

#  Universal File Converter

A Python-based tool to switch between document formats locally. No more uploading private files to random websites—this script handles **text extraction**, **format rendering**, and **PDF generation** directly on your machine.

###  What's New
* **Smart Paths:** Defaults to your system **Downloads** folder automatically.
* **Custom Naming:** You can choose a new name for your file during the conversion process.
* **Format Flexibility:** Supports `.docx`, `.md`, `.html`, `.pdf`, and `.txt`.

###  Setup & Usage
1. **Install Pandoc:** This script uses the Pandoc engine. Download it from [pandoc.org](https://pandoc.org/installing.html).
2. **Install Libraries:**
   ```bash
   pip install -r requirements.txt

++++++++++++++++++++++++++++++++++++++++=====================================
________________
Run the Engine: |
________________|
1.In bash go to directory 
2.Enter "python filename.py"

_________________________
Technical Flow           |
_________________________|

Input: Provide the source file path.

Target: Choose your output format.

Destination: Use the default Downloads folder or paste a custom directory.

Naming: Keep the original name or provide a fresh one.
