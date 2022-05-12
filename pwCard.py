#!/usr/bin/env python
# pwCard V 2022-02-12
#
# Quelle: https://www.youtube.com/watch?v=jMu5olgIuOE (Florian Dalwigk)
#
# benötigt library fpdf2: pip install fpdf2
# fpdf2 info: https://pypi.org/project/fpdf2/
#
# Konsolenaufruf z.B.: python pwCard.py 1
#
import secrets
import sys
import time
from fpdf import FPDF, HTMLMixin

class HTML2PDF(FPDF, HTMLMixin):
    pass

html = HTML2PDF()
html.add_page()
# Core Fonts: courier, times, helvetica
html.set_font('helvetica', size=12)
pdfName = 'pwKarte.pdf'
alphabet = ''

try:
    intArg = int(sys.argv[1])

    if intArg == 1:
        # mit Sonderzeichen (1 = krass | 2 oder höher = normal)
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789%§$.,_+-\/?!()={[#]}'
    else:
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,+-!?'
except:
    # default (Buchstaben und Zahlen)
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

head = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU', 'VWX', 'YZ1', '...']


def random_string():
    return secrets.choice(alphabet) + secrets.choice(alphabet) + secrets.choice(alphabet)

def generate_password_card():
    pc = []
    for row in range(10):
        row = []
        for col in range(10):
            row.append(random_string())
        pc.append(row)
    return pc

def start_pc_table(pc):
    table = ''
    pclen = len(pc)
    for row in range(pclen):
        for col in range(pclen):
            table += pc[row][col]
        if row != pclen - 1:
            table += '\n'
    # print(table)
    return table

def write_pdf():
    timestr = time.strftime("%Y-%m-%d %H:%M:%S")
    table = start_pc_table(generate_password_card())

    pc = []
    for line in table.splitlines():
        # line = line.strip()
        pc.append([line[0 + i:3 + i] for i in range(0, len(line), 3)])
    # print(pc)

    pclen = len(pc)
    width = int(100 / (float(len(head)) + 1.0))

    html_table = '<p><font size="8">Generiert: ' + timestr + '</font></p>\n'
    html_table += '<h2>PASSWORTKARTE</h2>\n<table border="1"><thead>\n<tr>\n'
    html_table += '<th width="' + str(width) + '%"> Reihe </th>\n'
    for th in head:
        html_table += '<th width="' + str(width) + '%">' + th + '</th>\n'
    html_table += '</tr>\n</thead><tbody>'
    i = 1
    for row in range(pclen):
        if i % 2:
            html_table += '<tr bgcolor="#FFFFFF">'
        else:
            html_table += '<tr bgcolor="#DCDCDC">'
        html_table += '<td><b><font color="#123">' + str(i) + '</td></font></b>\n'
        i += 1
        for col in range(pclen):
            html_table += '<td><font color="#123">' + pc[row][col] + '</td></font>\n'
        html_table += '</tr>'
    html_table += '</tbody></table>'
    # print(html_table)
    html.write_html(html_table)
    html.output(pdfName)

write_pdf()
print(f'{pdfName} mit "{alphabet}" erstellt :-)')
