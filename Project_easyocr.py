import easyocr as ocr
from easyocr import Reader
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import numpy as np
import re
import pandas as pd
import mysql.connector


with st.sidebar:
    selected = option_menu(
        menu_title='Business Card Data Extraction',
        options=['Home','Upload','Edit','Delete'],
        icons=['house','box-arrow-in-up','database','trash3-fill'],
        menu_icon="cast", default_index=0, orientation="verical",
        styles={'nav-link':{'font-size':'20px','margin':'-2px','font-color':'#342D7E'},
                'nav-link-selected':{'font-color':'white','background':'#342D7E'}}
    )
    st.write('VideoLink : ''https://youtu.be/BYPAhxubLYA')
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-color: #F8F6F0;
background-size :cover;
}
[data-testid="stSidebar"]{
background-position :center;
background-color: #F8F6F0;
}
[data-testid="stHeader"]{
background-color: #342D7E;
background-position :center;

}
# [data-baseweb="tab"]{
# background-color: #7E354D;
# }

</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
if selected == 'Home':
    st.title('BizCardX: Extracting Business Card Data with OCR')
    st.subheader('OCR')
    st.write('Optical Character Recognition (OCR) is the process that converts an image of text into a machine-readable text format. For example, if you scan a form or a receipt, your computer saves the scan as an image file. You cannot use a text editor to edit, search, or count the words in the image file. However, you can use OCR to convert the image into a text document with its contents stored as text data')
    st.write('')
    st.subheader('Importance Of OCR')
    st.write('Most business workflows involve receiving information from print media. Paper forms, invoices, scanned legal documents, and printed contracts are all part of business processes. These large volumes of paperwork take a lot of time and space to store and manage. Though paperless document management is the way to go, scanning the document into an image creates challenges. The process requires manual intervention and can be tedious and slow.'
            'Moreover, digitizing this document content creates image files with the text hidden within it. Text in images cannot be processed by word processing software in the same way as text documents. OCR technology solves the problem by converting text images into text data that can be analyzed by other business software. You can then use the data to conduct analytics, streamline operations, automate processes, and improve productivity.')
    st.subheader('Technologies Used in this Project')
    st.markdown('OCR,streamlit GUI, SQL,Data Extraction')
    st.subheader('Project overview')
    st.write('BizCardX: Extracting Business Card Data with OCR allows users to upload an image of a business card and extract relevant information from it using easyOCR. The extracted information which includes the company name, card holder name, designation, mobile number, email address, website URL, area, city, state, and pin code. The extracted information should then be displayed in the application graphical user interface (GUI)the application should allow users to save the extracted information into a database.')
    st.write('')
if selected == 'Upload':
    st.title('Easy OCR - Extract Text from Images')
    st.markdown('##Using Streamlit UI Application and EasyOCR')
    image = st.file_uploader(label="Upload an Image",type=["png", "jpeg", "jpg"])

    def load_an_image():
        reader = ocr.Reader(['en'])
        return reader
    reader = load_an_image()

    if image is not None:
        input_image = Image.open(image)
        st.image(input_image)
        with st.spinner('Wait for it...'):
            results = reader.readtext(np.array(input_image))
            details={
                    'Name':[],
                    'Position' :[],
                    'Website' :[],
                    'Mobile' :[],
                    'Email' :[],
                    'Address':[],
                    'District' :[],
                    'State':[],
                    'Pincode':[],
                    'Company_Name':[]
                    }
            for index,result in enumerate(results):
                if '@' in result[1] and '.com' in result[1]:
                    details['Email'].append(result[1])
                elif '-' in result[1]:
                    details['Mobile'].append(result[1])
                elif 'www' in result[1].lower() or 'www.' in result[1].lower():
                    details['Website'].append(result[1])
                elif index == 0:
                    details['Name'].append(result[1])
                elif index == 1:
                    details['Position'].append(result[1])
                elif re.findall("[a-zA-Z]{9} +[0-9]", result[1]):
                    details["Pincode"].append(result[1][10:])
                elif len(result[1])>=6 and result[1].isdigit():
                    details["Pincode"].append(result[1])
                state_extraction = re.findall("[a-zA-Z]{9} +[0-9]", result[1]) 
                state_extraction_1 = re.findall("^[0-9].+, ([a-zA-Z]+);", result[1])
                if state_extraction:
                    details["State"].append(result[1][:9])
                elif state_extraction_1:
                    details["State"].append(result[1].split()[-1])
                if len(details["State"]) == 2:
                    details["State"].pop(0)
                elif index == len(results) -1:
                    details["Company_Name"].append(result[1])
                address = re.findall("(^| )ABC-[0-9]+", result[1]) 
                address_1=re.findall(".+St, ([a-zA-Z]+).+", result[1]) 
                address_2 =re.findall('^[E].*',result[1])
                address_3 =re.findall("[0-9].+St.,", result[1]) 
                address_4 = re.findall('[0-9]+([a-zA-Z]+)St.,', result[1])
                if address:
                    details["Address"].append(address[0])
                elif address_1:
                    details["Address"].append(address_1[0])
                elif address_2:
                    details["Address"].append(address_2[0])
                elif address_3:
                    details["Address"].append(address_3[0])
                elif address_4:
                    details["Address"].append(address_4[0])
                re_1 = re.findall('.+St , ([a-zA-Z]+).+', result[1])
                re_2 = re.findall('.+St,, ([a-zA-Z]+).+', result[1])
                re_3 = re.findall('^[E].*',result[1])
                re_4 = re.findall('.+St., ([a-zA-Z]+).+', result[1])
                if re_1:
                    details["District"].append(re_1[0])
                elif re_1:
                    details["District"].append(re_2[0])
                elif re_3:
                    details["District"].append(re_3[0])
                elif re_4:
                    details["District"].append(re_4[0])
        rows = []
        for i in range(len(details['Name'])):
            row = {
                'Name': details['Name'][i] if details['Name'][i] else None,
                'Position': details['Position'][i] if details['Position'][i] else None,
                'Website': details['Website'][i] if details['Website'][i] else None,
                'Mobile': details['Mobile'][i] if details['Mobile'][i] else None,
                'Email': details['Email'][i] if details['Email'][i] else None,
                'Address': details['Address'][i] if details['Address'][i] else None,
                'District': details['District'][i] if details['District'][i] else None,
                'State': details['State'][i] if details['State'][i] else None,
                'Pincode': details['Pincode'][i] if details['Pincode'][i] else None,
                'Company_Name': details['Company_Name'][i] if details['Company_Name'][i] else None
            }
            rows.append(row)
        st.write(pd.DataFrame(rows).transpose())

        my_sql_connection = mysql.connector.connect(host ='localhost',user='root',password='1234')
        mycursor = my_sql_connection.cursor()
        mycursor.execute('use imagereader;')
        if st.button('Upload Data'):
            for data in rows:
                sql_insert = f'INSERT INTO imagedata(Name,Position,Website,Mobile,Email,Address,District,State,Pincode,Company_Name) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(sql_insert,tuple(data.values()))
                my_sql_connection.commit()
            st.success('Done Successfully!!!')

if selected == 'Edit':
    my_sql_connection = mysql.connector.connect(host ='localhost',user='root',password='1234')
    mycursor = my_sql_connection.cursor()
    mycursor.execute('use imagereader;')
    st.markdown("### Modify the Database")
    mycursor.execute("SELECT * FROM imagedata")
    data = mycursor.fetchall()
    columns = ['Name','Position','Website','Mobile','Email','Address','District','State','Pincode','Company_Name']
    data_frame = pd.DataFrame(data, columns=columns)
    st.write(data_frame)

    mycursor.execute('Select Name from imagedata')
    names = mycursor.fetchall()
    selection = {}
    for name in names:
        selection[name[0]] = name[0]
    selected_detail = st.selectbox("Select a Name to update",selection)
    st.markdown('###update your card detail')
    mycursor.execute('Select Name,Position,Website,Mobile,Email,Address,District,State,Pincode,Company_Name from imagedata where Name =%s',(selected_detail,))
    result = mycursor.fetchone()

    name = st.text_input('Name',result[0])
    position=st.text_input('Position',result[1])
    website =st.text_input('Website',result[2])
    mobile=st.text_input('Mobile',result[3])
    email=st.text_input('Email',result[4])
    address=st.text_input('Address',result[5])
    district=st.text_input('District',result[6])
    state=st.text_input('State',result[7])
    pincode=st.text_input('Pincode',result[8])
    company_name=st.text_input('Company_Name',result[9])
    
    try:
        if st.button("Modify Data"):
            my_sql_connection = mysql.connector.connect(host ='localhost',user='root',password='1234')
            mycursor = my_sql_connection.cursor()
            mycursor.execute('use imagereader;')
            mycursor.execute("UPDATE imagedata SET Name=%s,Position=%s, Website=%s, Mobile=%s, Email=%s,Address = %s,District=%s, State=%s, Pincode=%s, Company_Name=%s WHERE Name=%s",(name,position, website, mobile, email,address, district, state, pincode, company_name,selected_detail))
            my_sql_connection.commit()
            st.success("Data modified successfully!")
        if st.button('View updated Database'):
            st.markdown("### Modified Database")
            st.write(pd.DataFrame(data_frame))
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

if selected == 'Delete':
    my_sql_connection = mysql.connector.connect(host ='localhost',user='root',password='1234')
    mycursor = my_sql_connection.cursor()
    mycursor.execute('use imagereader;')
    mycursor.execute('SELECT Name from imagedata')
    names = mycursor.fetchall()
    selection = {}
    for name in names:
        selection[name[0]] = name[0]
    selected_detail = st.selectbox("Select a Name to delete",selection)
    st.write(f"### You have selected :green[**{selected_detail}'s**] card")
    try:
        if st.button("Delete Data"):
            my_sql_connection = mysql.connector.connect(host ='localhost',user='root',password='1234')
            mycursor = my_sql_connection.cursor()
            mycursor.execute('use imagereader;')
            mycursor.execute(f"DELETE from imagedata WHERE Name ='{selected_detail}'")
            my_sql_connection.commit()
            st.success("Data modified successfully!")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
    if st.button('View updated Database'):
        mycursor.execute('SELECT * from imagedata')
        df= mycursor.fetchall()
        st.markdown("### Modified Database")
        st.write(pd.DataFrame(df))