class Basket:
    bskt_product_name=""
    bskt_product_quantity=0
    total_bill=0
    text_heading="productname, productquantity"
    text_content=""

    def addBasket(self):
        n = int(input("Enter how many product you want: "))
        for i in range(n):
            self.bskt_product_name=input("Enter the product name you want to buy: ")
            self.bskt_product_quantity=int(input("Enter the quantity of product: "))
            if(self.bskt_product_name not in self.text_content):
                self.line_data=self.bskt_product_name+"\t"+str(self.bskt_product_quantity)
                if(i<n-1):
                    self.text_content=self.text_content+self.line_data+"\n"
                else:
                    self.text_content = self.text_content + self.line_data

        self.data = self.text_heading + "\n" + self.text_content
        f=open("Basket.txt","w")
        f.write(self.data)
        f.close()
    def veiwBasket(self):
        f=open("Basket.txt","r")
        self.data=f.read()
        f.close()

        self.file_data_lines=self.data.split("\n")
        self.text_heading=self.file_data_lines[0].split(",")
        print(len(self.text_heading))
        print(self.text_heading[0],"\t",self.text_heading[1])
        print(len(self.file_data_lines))
        for i in range(1,len(self.file_data_lines)):
            self.line_data=self.file_data_lines[i]
            self.product_data=self.line_data.split(",")
            print(self.product_data[0],"\t",int(self.product_data[1]))

    def calculateBill(self):
        f = open("stock.txt", "r")
        self.data = f.read()
        f.close()

        self.file_data_lines=self.data.split("\n")
        self.total_bill=0
        for i in range(1,len(self.file_data_lines)):
            self.line_data=self.file_data_lines[i]
            self.product_data=self.line_data.split(",")
            self.total_bill=self.total_bill+(int(self.bskt_product_quantity)*int(self.product_data[2]))
        print("Total bill is ",self.total_bill)