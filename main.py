#!/usr/bin/env python
#
# Quellen:
# https://www.youtube.com/watch?v=jMu5olgIuOE (Florian Dalwigk)
# fpdf2 info: https://pypi.org/project/fpdf2/
#
import secrets
import time
from fpdf import FPDF, HTMLMixin

class HTML2PDF(FPDF, HTMLMixin):
    pass

html = HTML2PDF()
html.add_page()
# Core Fonts: courier, times, helvetica
html.set_font('helvetica', size=12)

# alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
# alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,+-!?'
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789%§$.,_-\/?!()={[#]}'
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
    html.output("pwKarte.pdf")

write_pdf()
