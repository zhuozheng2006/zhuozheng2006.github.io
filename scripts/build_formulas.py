#!/usr/bin/env python3
"""Build font-independent, accessible formula artwork (requires LaTeX and dvisvgm)."""
import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FORMULAS = {
    'gauss-bonnet': r'\int_M K\,\mathrm{d}A=2\pi\chi(M)',
    'euler-product': r'\zeta(s)=\prod_p\frac{1}{1-p^{-s}}',
    'stokes': r'\int_{\partial\Omega}\omega=\int_{\Omega}\mathrm{d}\omega',
}

def main():
    output = ROOT / 'assets/formulas'
    output.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as directory:
        work = Path(directory)
        for name, formula in FORMULAS.items():
            (work / f'{name}.tex').write_text(
                r'\documentclass[12pt,border=1pt]{standalone}' '\n'
                r'\usepackage{amsmath,amssymb}' '\n'
                r'\begin{document}' '\n'
                r'$\displaystyle ' + formula + r'$' '\n'
                r'\end{document}' '\n'
            )
            subprocess.run(['latex', '-interaction=nonstopmode', '-halt-on-error', f'{name}.tex'], cwd=work, check=True, stdout=subprocess.DEVNULL)
            subprocess.run(['dvisvgm', '--no-fonts', '--exact', '--bbox=papersize', f'{name}.dvi', '-o', str(output / f'{name}.svg')], cwd=work, check=True)
            path = output / f'{name}.svg'
            svg = path.read_text().replace("<g id='page1'>", "<g id='page1' fill='#1d1b18'>")
            path.write_text(svg)
            width = float(re.search(r"width='([\d.]+)pt'", svg).group(1))
            print(f'{name}: CSS width {width / 12:.4f}em')

if __name__ == '__main__':
    main()
