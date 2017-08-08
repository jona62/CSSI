class Box:
    def __init__(self, box_height, box_width, box_border):
        self.Height = box_Height
        self.Width = box_Width
        self.Border = box_Border

    def getWidth(self):
        return self.Width

    def getHeight(self):
        return self.Height

    def getBorder(self):
        return self.Border

    def Fillbox(width, height):
        box=



    def BorderBox(Width, Height, Border):
        tb_border = ("#" * (self.Width + self.Border *2))
        lr_border = (("# " * self.Border) + (" "* self.Width) + ("#"* self.Border))
        for i in range (self.Height + self.Border * 2 ):
            if i >= self.Border and i<= (self.Height + self.Border -1):
                print lr_border
            else:
                print tb_border
        BorderBox (1,2,3)


    
