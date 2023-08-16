import pandas as pd
from fpdf import FPDF


pdf=FPDF(orientation="p",format="A4",unit="mm")
df=pd.read_csv("topics.csv")

#print(df)

for index,row in df.iterrows():
    
    for pages in range(row["Pages"]):
        pdf.add_page()
        pdf.set_font(family="Times",style="B",size=12)
        pdf.set_text_color(100,100,100)
        pdf.cell(w=0,h=12,txt=row["Topic"],align="L",ln=1)
        pdf.line(10,21,200,21)

pdf.output("output.pdf")