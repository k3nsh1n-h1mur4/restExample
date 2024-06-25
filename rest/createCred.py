from reportlab.pdfgen import canvas
from pathlib import Path

# c = name of the pdf file
# create pdf file
# add cred image to pdf object
# get data from db worker, auhtper, regh
# make qrcode
# get data of each child
# put data to pdf file

path = Path.cwd()
qrimg = path.joinpath('qrcode.png')

path1 = Path.cwd()
path_static = path1.joinpath('static')
img_cred = path_static.joinpath('cred.png')



class CREATECRED:
    def __init__(self, c):
        self.c = c    

    @classmethod
    def create_credFile(cls, c):
        c.drawImage(img_cred, x=10, y=10, width=200, height=200)
        