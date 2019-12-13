#!/usr/bin/env python
# coding: utf-8

# In[7]:


from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.platypus import Image


# In[8]:


import csv


# In[9]:


data_file='temp-adjusted.csv'
data_extract=[]
i=0


# In[12]:


def read_data(data_file):
    my_reader = csv.reader(open('temp-adjusted.csv', "rt"))
    for row in my_reader:
        for check in range(0,len(row)):
            data_extract.append(row[check])
        


# In[15]:


read_data(data_file)


# In[16]:


def create_reg_pdf(data_extract):
    
    #all variables carrying absolute values are
    #values converted to their PDF point values from
    #corresponding centimetre values
    #for reference : 
    #http://www.unitconversion.org/typography/centimeters-to-points-computer-conversion.html
    
    #horizontal centre
    h_centre=297.635
    
    #left margin corrected
    l_begin=70.866141732
    
    #right margin corrected
    r_end=524.403858268
    
    #name of the pdf
    pdf_name=data_extract[4]+'_'+data_extract[0]+'.pdf'
    
    #create the canvas object
    c=canvas.Canvas(pdf_name, pagesize=A4)
    
    #header text
    c.setFont('Helvetica',26,leading=None)
    c.drawCentredString(h_centre,780,data_extract[0])
    
    #university name text
    c.setFont('Helvetica',22,leading=None)
    c.setFillColorRGB(0.4,0.4,0.4)
    c.drawCentredString(h_centre,755,data_extract[1])
    
    #form type text
    c.setFont('Helvetica',20,leading=None)
    c.setFillColorRGB(0,0,0)
    c.drawCentredString(h_centre,730,data_extract[2])
    c.line(l_begin,720,r_end,720)
    
    #"Institution Details"
    c.setFont('Helvetica',15,leading=None)
    c.drawString(l_begin,680,data_extract[3])
    
    #name of university
    c.setFont('Helvetica',13,leading=None)
    c.drawString(l_begin,660,"Name of University:")
    c.setFont('Helvetica',10,leading=None)
    c.drawString(l_begin,649,data_extract[4])
    
    #address of university
    c.setFont('Helvetica',13,leading=None)
    c.drawString(l_begin,630,"Address of University:")
    styleSheet = getSampleStyleSheet()
    style = styleSheet['BodyText']
    P=Paragraph(data_extract[5], style)
    #available width for flowable 
    aW = (2*h_centre)-(2*l_begin)-len("Address:")
    #available height for flowable
    aH = 605
    w, h = P.wrap(aW, aH)
    if w<=aW and h<=aH:
        P.drawOn(c,l_begin,aH)
        aH= aH-h
        
    
    #contact number of university
    c.setFont('Helvetica',13,leading=None)
    c.drawString(l_begin,589,"Contact number:")
    c.setFont('Helvetica',10,leading=None)
    c.drawString(l_begin,578,data_extract[6])
    
    #email ID of university
    c.setFont('Helvetica',13,leading=None)
    c.drawString(l_begin,563,"E-mail ID:")
    c.setFont('Helvetica',10,leading=None)
    c.drawString(l_begin,552,data_extract[7])
    
    
    #name of the faculty in charge
    c.setFont('Helvetica',13,leading=None)
    c.drawString(l_begin,537,"Faculty in-charge:")
    c.setFont('Helvetica',10,leading=None)
    c.drawString(l_begin,526,data_extract[8])
    
    
    #Contact number of the faculty in charge
    c.setFont('Helvetica',13,leading=None)
    c.drawString(l_begin,511,"Contact number of Faculty in-charge:")
    c.setFont('Helvetica',10,leading=None)
    c.drawString(l_begin,500,data_extract[9])
        
    #Email ID of the faculty in charge
    c.setFont('Helvetica',13,leading=None)
    c.drawString(l_begin,485,"E-mail ID of Faculty in-charge:")
    c.setFont('Helvetica',10,leading=None)
    c.drawString(l_begin,474,data_extract[10])
    
    
    #Team Details
    c.setFont('Helvetica',15,leading=None)
    c.drawString(l_begin,434,data_extract[11])
        
    #Speaker-1 details
    #Name of Speaker-1
    c.setFont('Helvetica',13,leading=None)
    c.drawString(l_begin,414,"Speaker-1 name:")
    c.setFont('Helvetica',10,leading=None)
    c.drawString(l_begin,403,data_extract[12])
    
    
    #Contact number of Speaker-1
    c.setFont('Helvetica',13,leading=None)
    c.drawString(l_begin,388,"Speaker-1 E-mail ID:")
    c.setFont('Helvetica',10,leading=None)
    c.drawString(l_begin,377,data_extract[13])
    
    
    #Email ID of Speaker-1
    c.setFont('Helvetica',13,leading=None)
    c.drawString(l_begin,362,"Speaker-1 contact number:")
    c.setFont('Helvetica',10,leading=None)
    c.drawString(l_begin,351,data_extract[14])
    
    #Speaker-1 Image
    speaker_1_img='sample_passport_size.jpg'
    c.drawImage(speaker_1_img,r_end-100,353,width=70,height=70)
    
    #Speaker-2 details
    #Name of Speaker-2
    c.setFont('Helvetica',13,leading=None)
    c.drawString(l_begin,311,"Speaker-2 name:")
    c.setFont('Helvetica',10,leading=None)
    c.drawString(l_begin,300,data_extract[15])
    
    
    #Contact number of Speaker-2
    c.setFont('Helvetica',13,leading=None)
    c.drawString(l_begin,285,"Speaker-2 E-mail ID:")
    c.setFont('Helvetica',10,leading=None)
    c.drawString(l_begin,274,data_extract[16])
    
    
    #Email ID of Speaker-2
    c.setFont('Helvetica',13,leading=None)
    c.drawString(l_begin,259,"Speaker-2 contact number:")
    c.setFont('Helvetica',10,leading=None)
    c.drawString(l_begin,248,data_extract[17])
    
    #Speaker-2 Image
    speaker_2_img='sample_passport_size.jpg'
    c.drawImage(speaker_2_img,r_end-100,250,width=70,height=70)
    
    #Researcher details
    #Name of Researcher
    c.setFont('Helvetica',13,leading=None)
    c.drawString(l_begin,208,"Researcher name:")
    c.setFont('Helvetica',10,leading=None)
    c.drawString(l_begin,197,data_extract[18])
    
    
    #Contact number of Researcher
    c.setFont('Helvetica',13,leading=None)
    c.drawString(l_begin,182,"Researcher E-mail ID:")
    c.setFont('Helvetica',10,leading=None)
    c.drawString(l_begin,171,data_extract[16])
    
    
    #Email ID of Researcher
    c.setFont('Helvetica',13,leading=None)
    c.drawString(l_begin,156,"Speaker-2 contact number:")
    c.setFont('Helvetica',10,leading=None)
    c.drawString(l_begin,145,data_extract[17])
    
    #Researcher Image
    researcher_img='sample_passport_size.jpg'
    c.drawImage(researcher_img,r_end-100,147,width=70,height=70)
    
    #Page-1 End line
    c.line(l_begin,50,r_end,50)
    c.setFont('Helvetica',8,leading=None)
    c.drawString(r_end-70,35,"Please Turn Over")
    
    #End of Page-1
    c.showPage()
    
    
    #Start Page-2
    #Payment Details
    c.setFont('Helvetica',15,leading=None)
    c.drawString(l_begin,780,"Payment Details")
        
    #Online Payment Details
    c.setFont('Helvetica',13,leading=None)
    c.drawString(l_begin,740,"Online Payment:    Yes / No")
    c.setFont('Helvetica',10,leading=None)
    c.drawString(l_begin,720,"If Yes, Mode of Payment:    NEFT / UPI")
    c.setFont('Helvetica',13,leading=None)
    
    #Demand Draft
    c.drawString(l_begin,700,"Demand Draft:    Yes / No")
    c.setFont('Helvetica',10,leading=None)
    c.drawString(l_begin,680,"If Yes, Name of the Bank:")
    c.drawString(l_begin,665,"Demand Draft number:")
    
    
    #Declaration header
    c.setFont('Helvetica',13,leading=None)
    c.drawCentredString(h_centre,620,"Declaration")
    
    
    #Declaration Text
    c.setFont('Helvetica',10,leading=None)
    styleSheet = getSampleStyleSheet()
    style = styleSheet['BodyText']
    Q=Paragraph("We hereby declare that the institution and its team members will abide by all the rules of the competition set by the organizers and as notified to us from time to time throughout the period of the competition. We also declare and confirm that all the information provided by the organizers in the registration form is true and accurate to the best of our knowledge. In case of non compliance or violation of any rules or regulations on our part, the organizing body shall reserve the right to cancel our registration/ candidature.", style)
    #available width for flowable 
    aW = (2*h_centre)-(2*l_begin)
    #available height for flowable
    aH = 540
    w, h = Q.wrap(aW, aH)
    if w<=aW and h<=aH:
        Q.drawOn(c,l_begin,aH)
        aH= aH-h
    
    #Team member signatures
    #Speaker-1
    c.setDash([1.5,1,1.5,1],0)
    c.line(l_begin,450,l_begin+50,450)
    c.setFont('Helvetica',10,leading=None)
    c.drawString(l_begin,435,"Speaker-1")
    c.drawString(l_begin,420,"Name and signature")
    
    #Speaker-2
    c.line((((2*h_centre)-(2*l_begin))/2),450,(((2*h_centre)-(2*l_begin))/2)+50,450)
    c.setFont('Helvetica',10,leading=None)
    c.drawString((((2*h_centre)-(2*l_begin))/2),435,"Speaker-2")
    c.drawString((((2*h_centre)-(2*l_begin))/2),420,"Name and signature")
    
    #Researcher
    c.line(r_end-150,450,r_end-100,450)
    c.setFont('Helvetica',10,leading=None)
    c.drawString(r_end-150,435,"Researcher")
    c.drawString(r_end-150,420,"Name and signature")
    
    
    
    #Page-2 End line
    c.setDash([1,0,1,0],0)
    c.line(l_begin,50,r_end,50)
    #c.setFont('Helvetica',8,leading=None)
    #c.drawString(r_end-70,35,"Please Turn Over")
    
    
    c.showPage()
    
    print('writing')
    c.save()


# In[17]:


create_reg_pdf(data_extract)


# In[ ]:





# In[ ]:




