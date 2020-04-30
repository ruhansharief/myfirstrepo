from fpdf import FPDF
pdf=FPDF()
pdf.add_page()

#The Font you are using must be available in your system
pdf.set_font("Arial",size=20)
pdf.cell(60,30,txt="Hello",align="C")
#for new line use pdf.ln
pdf.ln()

#for changing text color R G B
pdf.set_text_color(255,0,0)

#for border just add border in the cell
pdf.cell(60,40,txt="Hello",align="C",border=1)

#for adding image
pdf.image("C:\\Users\\Tanmay\\Desktop\\py.png",x=None,y=None,w=50,h=50,type='',link="")

pdf.output('demo.pdf')


#to know more about it
dir(pdf)
