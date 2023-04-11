from fpdf import FPDF
import mysql.connector

connection=mysql.connector.connect(host='localhost',database='DASS',user='root',password='4267')    #MySQL connection
cursor=connection.cursor()

def pdf_report():
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font('Arial','B',16)
    pdf.cell(200,200,"Hello world")
    pdf.output('Report.pdf','F')
pdf_report()