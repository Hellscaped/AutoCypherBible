#!/usr/bin/env python3
import time,numpy as np
from reportlab.pdfgen import canvas
# Seed the random number generator
np.random.seed(np.random.randint(0,1000))

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
obscurity = 100 # Code numbers per letter
print(f"Generating a {str(obscurity)} codes per {str(len(alphabet))} letter multibet cypher")
start = time.time()
offset = "1"
for i in range(1,len(str(len(alphabet)*obscurity))):
    offset += "0"
offset = int(offset)

multibet = ""
crypt = {}
for let in alphabet:
    multibet += let*obscurity

numbers = [*range(offset,offset+len(multibet))]
np.random.shuffle(numbers)
for let,num in zip(multibet,numbers):
    if let not in crypt:
        crypt[let] = [num]
    else:
        crypt[let].append(num)

print(f"Generated in {str(time.time()-start)} seconds")

print ("Generating a PDF file")
start = time.time()
# Create a PDF file.
pdf = canvas.Canvas(f"bible-{str(start)}.pdf")

# Create pages
# title page
pdf.setFont("Courier", 24)
pdf.drawCentredString(300, 750, "AutoCypherBible Generated Bible")
pdf.setFont("Courier", 12)
pdf.drawCentredString(300, 700, f'Alphabet: {alphabet}')
pdf.drawCentredString(300, 650, f'Obscurity: {str(obscurity)}')
pdf.showPage()
for i in range(0,len(alphabet)):
    pdf.setFont("Courier", 12)
    pdf.drawString(2,2, "AutoCypherBible")
    # Draw the letter top center middle
    pdf.drawCentredString(300, 750, alphabet[i])
    # draw a grid of numbers
    width = obscurity//10
    height = obscurity//width
    for j in range(0,height):
        for k in range(0,width):
            pdf.drawString(50+k*50, 700-j*50, str(crypt[alphabet[i]][j*width+k]))
    pdf.showPage()
pdf.save()