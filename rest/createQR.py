import qrcode

class QRCODE:
    def __init__(self,ctx):
        self.ctx = ctx

    @classmethod
    def createqr_code(self, ctx):
        img = qrcode.make(ctx)
        img.save('qrcode.png')
        return img


#if __name__ == '__main__':
#    ig = QRCODE.createqr_code('Isaac')
    