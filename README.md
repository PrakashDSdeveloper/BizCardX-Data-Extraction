# BizCardX: Extracting Business Card Data with OCR
What is OCR (Optical Character Recognition)?

Optical Character Recognition (OCR) is the process that converts an image of text into a machine-readable text format. For example, if you scan a form or a receipt, your computer saves the scan as an image file. You cannot use a text editor to edit, search, or count the words in the image file. However, you can use OCR to convert the image into a text document with its contents stored as text data.

Why is OCR important?

Most business workflows involve receiving information from print media. Paper forms, invoices, scanned legal documents, and printed contracts are all part of business processes. These large volumes of paperwork take a lot of time and space to store and manage. Though paperless document management is the way to go, scanning the document into an image creates challenges. The process requires manual intervention and can be tedious and slow.

Moreover, digitizing this document content creates image files with the text hidden within it. Text in images cannot be processed by word processing software in the same way as text documents. OCR technology solves the problem by converting text images into text data that can be analyzed by other business software. You can then use the data to conduct analytics, streamline operations, automate processes, and improve productivity.

How does OCR work?

The OCR engine or OCR software works by using the following steps:

Image acquisition
A scanner reads documents and converts them to binary data. The OCR software analyzes the scanned image and classifies the light areas as background and the dark areas as text.

Preprocessing
The OCR software first cleans the image and removes errors to prepare it for reading. These are some of its cleaning techniques:

Deskewing or tilting the scanned document slightly to fix alignment issues during the scan.
Despeckling or removing any digital image spots or smoothing the edges of text images.
Cleaning up boxes and lines in the image.
Script recognition for multi-language OCR technology
Text recognition
The two main types of OCR algorithms or software processes that an OCR software uses for text recognition are called pattern matching and feature extraction.

Pattern matching
Pattern matching works by isolating a character image, called a glyph, and comparing it with a similarly stored glyph. Pattern recognition works only if the stored glyph has a similar font and scale to the input glyph. This method works well with scanned images of documents that have been typed in a known font.

Feature extraction
Feature extraction breaks down or decomposes the glyphs into features such as lines, closed loops, line direction, and line intersections. It then uses these features to find the best match or the nearest neighbor among its various stored glyphs.

Postprocessing
After analysis, the system converts the extracted text data into a computerized file. Some OCR systems can create annotated PDF files that include both the before and after versions of the scanned document.

**OverView:**

BizCardX: Extracting Business Card Data with OCR allows users to upload an image of a business card and extract relevant information from it using easyOCR. The extracted information which includes the company name, card holder name, designation, mobile number, email address, website URL, area, city, state, and pin code. The extracted information should then be displayed in the application graphical user interface (GUI)the application should allow users to save the extracted information into a database.

**Flow**

1.Install the required packages: You will need to install Python, Streamlit,easyOCR, and a database management system like SQLite or MySQL.

2.Streamlit Application contains UPLOAD,EDIT,DELETE

3.In upload option we can upload an Bussiness card after clicking the upload button we can see data frame

4.In edit option we can edit the details of Bussiness card and upload the details accordingly.

5.In Delete option we can delete the uploaded details 



**Technologies used in this Project :**
OCR,streamlit GUI,pandas, SQL,Data Extraction

**Personal Details:**

Name: Prakash T N

Domain : Data Science

Video link : https://www.linkedin.com/feed/update/urn:li:activity:7101819488781697024?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7101819488781697024%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29&originTrackingId=SRmU%2BKWuR4KswoostXJOFQ%3D%3D&lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_recent_activity_content_view%3BtNfh%2B6xUQKq1x%2BojdLkrsw%3D%3D

