import tkinter as tk
from tkinter import filedialog
import cv2
import pytesseract
from os import listdir
from os.path import isfile, join
import numpy
global z
z=''
def GUI():
    def UploadAction():
        global dirname
        dirname=filedialog.askdirectory(parent=window,initialdir="/",title='Please select a directory')
        global z
        z=''
        z+='folderpath'
        print(z)
    def fileupload():
        global filename
        filename = filedialog.askopenfilename()
        global z
        z=''
        z+='filepath'
    def detect():
        if z=="folderpath":
            mypath=dirname
            onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
            images = numpy.empty(len(onlyfiles), dtype=object)
            for n in range(0, len(onlyfiles)):
                images[n] = cv2.imread( join(mypath,onlyfiles[n]) )

    # Load the image

        # Convert to grayscale
                gray = cv2.cvtColor(images[n], cv2.COLOR_BGR2GRAY)

                # Apply bilateral filter to remove noise
                blur = cv2.bilateralFilter(gray, 11, 17, 17)

                # Detect edges with Canny edge detection
                edges = cv2.Canny(blur, 30, 200)

                # Find contours in the edged image
                contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

                # Sort contours by area and get the largest contour
                contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

                # Loop over the contours to find the license plate
                plate = None
                for contour in contours:
                    # Approximate the contour as a polygon
                    peri = cv2.arcLength(contour, True)
                    approx = cv2.approxPolyDP(contour, 0.02 * peri, True)

                    # If the polygon has four vertices, it is likely a license plate
                    if len(approx) == 4:
                        plate = approx
                        break

                # Extract the plate area from the image
                x, y, w, h = cv2.boundingRect(plate)
                plate_img = gray[y:y+h, x:x+w]

                # Apply thresholding to enhance the plate characters
                thresh = cv2.threshold(plate_img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

                # Perform OCR to extract the characters from the plate
                text = pytesseract.image_to_string(thresh, config='--psm 11')
                textbox1.insert('end',f"Detected {n+1}-car's plate number: {text}")
            
        elif z=='filepath':
            img = cv2.imread(filename)

# Convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Apply bilateral filter to remove noise
            blur = cv2.bilateralFilter(gray, 11, 17, 17)

            # Detect edges with Canny edge detection
            edges = cv2.Canny(blur, 30, 200)

            # Find contours in the edged image
            contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            # Sort contours by area and get the largest contour
            contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

            # Loop over the contours to find the license plate
            plate = None
            for contour in contours:
                # Approximate the contour as a polygon
                peri = cv2.arcLength(contour, True)
                approx = cv2.approxPolyDP(contour, 0.02 * peri, True)

                # If the polygon has four vertices, it is likely a license plate
                if len(approx) == 4:
                    plate = approx
                    break

            # Extract the plate area from the image
            x, y, w, h = cv2.boundingRect(plate)
            plate_img = gray[y:y+h, x:x+w]

            # Apply thresholding to enhance the plate characters
            thresh = cv2.threshold(plate_img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

            # Perform OCR to extract the characters from the plate
            text = pytesseract.image_to_string(thresh, config='--psm 11')
            textbox1.insert('end',f"car's plate number: {text}")
        else:
            textbox1.insert('end',"Choose File/ Folder path first")
            
    window=tk.Tk()
    window.title("Number plate Detection Applicatio")
    window.geometry('400x550')
    window.configure(bg="#0F0F0F")
    label1=tk.Label(window,text='Number Plate Detection',bg="#0F0F0F",fg='#de3163',font=("Comic Sans MS", 25))
    label1.grid(row=0,column=0,columnspan=2,padx=12,pady=7)

    label2=tk.Label(window,text='Choose Folder :',bg="#0F0F0F",fg='#7fffd4',font=("Arial", 16))
    label2.grid(row=1,column=0,sticky='NW',pady=30,padx=10)
    button2=tk.Button(window,text="Folder",font=('Helvetica', 13),bg='#4997d0',fg="black",command=UploadAction)
    button2.grid(row=1,column=1,sticky='NW',pady=30,padx=10)

    label3=tk.Label(window,text="OR",bg="#0F0F0F",fg='#e30022',font=("Arial", 16))
    label3.grid(column=0,row=2,columnspan=2)

    label4=tk.Label(window,text='Choose File/Picture :',bg="#0F0F0F",fg='#7fffd4',font=("Arial", 16))
    label4.grid(row=3,column=0,sticky='NW',pady=30,padx=10)
    button4=tk.Button(window,text="File",font=('Helvetica', 13),bg='#4997d0',fg="black",command=fileupload)
    button4.grid(row=3,column=1,sticky='NW',pady=30,padx=10)

    button4=tk.Button(window,text="Detect",font=('Helvetica',15),bg='#a4c639',fg="black",command=detect)
    button4.grid(row=4,column=0,columnspan=2,padx=10)

    textbox1=tk.Text(height=12,width=40,bg="#0F0F0F",fg='white')
    textbox1.grid(row=5,column=0,columnspan=2,pady=20)
    window.mainloop()

GUI()