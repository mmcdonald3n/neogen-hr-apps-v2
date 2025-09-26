from fpdf import FPDF
from pathlib import Path
from .branding import BRAND
class PDF(FPDF):
    def header(self):
        try: self.image(BRAND.logo_path, 10, 8, 22)
        except Exception: pass
        self.set_font('Helvetica', 'B', 14); self.set_text_color(17,17,17)
        self.cell(0, 10, self.title, border=0, ln=1, align='R'); self.ln(2)
    def footer(self):
        self.set_y(-15); self.set_font('Helvetica', '', 9); self.set_text_color(102,112,133)
        self.cell(0, 10, f"Page {self.page_no()}", align='C')
def export_pdf(md_text: str, title: str, out_path: Path) -> Path:
    pdf = PDF(); pdf.set_title(title); pdf.set_auto_page_break(auto=True, margin=15); pdf.add_page()
    pdf.set_font('Helvetica', '', 11)
    for line in md_text.split('\n'):
        s = line.strip()
        if s.startswith('**') and s.endswith('**'):
            pdf.set_font('Helvetica', 'B', 12); pdf.multi_cell(0, 6, s.strip('*')); pdf.ln(1); pdf.set_font('Helvetica','',11)
        elif s.startswith('**'):
            text = s.replace('**',''); pdf.set_font('Helvetica', 'B', 12); pdf.multi_cell(0,6,text); pdf.ln(1); pdf.set_font('Helvetica','',11)
        elif s.startswith('- '):
            pdf.cell(5); pdf.multi_cell(0, 5.5, '• ' + s[2:])
        else:
            if s == "": pdf.ln(2)
            else: pdf.multi_cell(0, 5.5, s)
    out_path.parent.mkdir(parents=True, exist_ok=True); pdf.output(str(out_path)); return out_path