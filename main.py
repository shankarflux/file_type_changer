import os
import pypandoc
from PyPDF2 import PdfReader
from reportlab.pdfgen import canvas
from pathlib import Path

def get_output_path(input_path, output_format):

    custom_dir = input("\nEnter specific folder path (or press Enter for Downloads): ").strip('"')
    
    if not custom_dir:
        
        output_dir = Path.home() / "Downloads"
    else:
        output_dir = Path(custom_dir)
    
    # Create the folder if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)

    # -> Handle the Filename
    default_name = Path(input_path).stem
    custom_name = input(f"Enter new filename (Press Enter for '{default_name}'): ").strip()
    
    final_name = custom_name if custom_name else default_name
    
    # Return the full path: Folder + Name + Extension
    return output_dir / f"{final_name}.{output_format.lower()}"

def convert_file(input_path, output_format):
    output_path = get_output_path(input_path, output_format)

    # DOCX / MD / HTML → any format
    if input_path.lower().endswith((".docx", ".md", ".html")):
        pypandoc.convert_file(input_path, output_format, outputfile=str(output_path), extra_args=['--standalone'])
        print(f"\n✅ Converted successfully: {output_path}")
        return

    # PDF -> TXT
    if input_path.lower().endswith(".pdf") and output_format.lower() == "txt":
        reader = PdfReader(input_path)
        text = "".join([page.extract_text() for page in reader.pages if page.extract_text()])
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"\n✅ Extracted text to: {output_path}")
        return

    # TXT -> PDF
    if input_path.lower().endswith(".txt") and output_format.lower() == "pdf":
        c = canvas.Canvas(str(output_path))
        with open(input_path, "r", encoding="utf-8") as f:
            y = 800
            for line in f:
                c.drawString(50, y, line.strip())
                y -= 15
                if y < 50:
                    c.showPage()
                    y = 800
        c.save()
        print(f"\n✅ Converted successfully: {output_path}")
        return

    print(f"\n❌ Unsupported conversion: {input_path} → {output_format}")

if __name__ == "__main__":
    print("--- File Converter Tool ---")
    in_path = input("Enter source file path: ").strip('"')
    
    if not os.path.exists(in_path):
        print("Error: File not found!")
        exit(1)

    out_fmt = input("Enter target format (pdf/txt/md/html/docx): ").lower().strip()
    convert_file(in_path, out_fmt)