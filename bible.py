#!/usr/bin/env python3
import time,numpy as np,json,hashlib
from reportlab.pdfgen import canvas
# Seed the random number generator
def seed():
    return int(hashlib.sha256(str(time.time()).encode()).hexdigest(), 16) % 10**8
np.random.seed(seed())
# Generate a random identifier
def id_generator(size=3, chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
    s = ''
    for i in range(size):
        for d in range(0,5):
            s += chars[seed()%len(chars)]
        if i < size-1:
            s += '-'
    return s
identifier = id_generator()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
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
pdf = canvas.Canvas(f"bible-{identifier}.pdf")

# Create pages
# title page

pdf.setFont("Courier", 24)
pdf.drawString(5, 5, "AutoCypherBible")
pdf.drawCentredString(300, 450, "Cypher Bible")
pdf.setFont("Courier", 12)
pdf.grid([25,575],[25,825])
pdf.drawCentredString(300, 400, f'Alphabet: {alphabet}')
pdf.drawCentredString(300, 350, f'Obscurity: {str(obscurity)}')
pdf.showPage()
for i in range(0,len(alphabet)):
    pdf.grid([25,575],[25,825])
    pdf.setFont("Courier", 24)
    pdf.drawString(5, 5, "AutoCypherBible")
    # Draw the letter top center middle
    pdf.setFont("Courier", 32)
    pdf.drawCentredString(300, 750, alphabet[i])
    pdf.setFont("Courier", 12)
    # draw a grid of numbers
    width = obscurity//10
    height = obscurity//width
    xlist = [*range(50,50+width*50,50)]
    ylist = [*range(50,50+height*50,50)]
    # make it 10x10
    xlist.append(50+width*50)
    ylist.append(50+height*50)
    # offset the grid
    for j in range(0,len(ylist)):
        ylist[j] += 180
    for j in range(0,height):
        for k in range(0,width):
            pdf.drawString(60+k*50, 700-j*50, str(crypt[alphabet[i]][j*width+k]))
    pdf.grid(xlist,ylist)
    # Draw coordinates above the grid and to the left
    pdf.setFont("Courier", 12)
    pdf.drawString(70/2, 735, "x")
    for j in range(0,width):
        pdf.drawString(70+j*50, 735, str(j+1))
    for j in range(0,height):
        pdf.drawString(35, 700-j*50, str(j+1))
    pdf.showPage()
pdf.save()

print(f"Generated in {str(time.time()-start)} seconds")

print ("Generating a JSON file")
start = time.time()
with open(f"bible-{identifier}.json","w") as f:
    json.dump(crypt,f)
print(f"Generated in {str(time.time()-start)} seconds")