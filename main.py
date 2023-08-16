import pandas as pd
from fpdf import FPDF




pdf=FPDF(orientation="p",format="A4",unit="mm")
pdf.set_auto_page_break(auto=False,margin=0)
df=pd.read_csv("topics.csv")

#print(df)
page=0
for index,row in df.iterrows():

    
    
    for i in range(row["Pages"]):
        pdf.add_page()
        pdf.set_font(family="Times",style="B",size=12)
        pdf.set_text_color(100,100,100)
        pdf.cell(w=0,h=12,txt=row["Topic"],align="L",ln=1)
        pdf.line(10,21,200,21)
        for i in range(31,295,10):
            pdf.line(10,i,200,i)
        pdf.ln(265)
        page+=1
        pdf.cell(w=0,h=12,txt=f"{page}",align="R")


pdf.output("output.pdf")