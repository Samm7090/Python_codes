class Stock:
    stock_product_name=""
    stock_product_price=0
    stock_product_quantity=0
    text_heading="productid,productname,productprice,productquantity"
    text_content=""


    def addStock(self):
        f=open("addstock.txt","w")
        self.input_data=""
        self.operation_completed=False
        while(self.operation_completed==False):
            try:
                n = int(input("How many product you want to add "))
                self.operation_completed=True
            except ValueError as e:
                self.input_data=self.input_data+str(e)+"\n"
                print("You have entered incorrect integer value ")
        f.write(self.input_data)
        f.close()
        for i in range(n):
            self.stock_product_name=input("Enter product name you want to add: ")
            self.stock_product_price=int(input("Enter the price of product: "))
            self.stock_product_quantity=int(input("Enter the quantity of stock: "))
            if(self.stock_product_name not in self.text_content):
                self.line_date=str(i+1)+","+self.stock_product_name+","+str(self.stock_product_price)+","+str(self.stock_product_quantity)
                if(i<n-1):
                    self.text_content=self.text_content+self.line_date+"\n"
                else:
                    self.text_content=self.text_content+self.line_date

        self.data=self.text_heading+"\n"+self.text_content
        f=open("stock1.txt","w")
        f.write(self.data)
        f.close()

    def veiwStock(self):
        '''f=open("stock.txt","r")
        data=f.read()
        f.close()

        file_data_lines=data.split("\n")
        text_heading=file_data_lines[0].split(",")
        print(text_heading[0],text_heading[1],text_heading[2],text_heading[3])
        for i in range(1,len(file_data_lines)):
            line_data = file_data_lines[i]
            product_data = line_data.split(',')
            print(int(product_data[0]), '\t' , product_data[1] , '\t' , product_data[2])'''
        self.f = open("stock1.txt", "r")
        self.data = self.f.read()
        self.f.close()

        self.file_data_lines = self.data.split("\n")
        self.text_heading = self.file_data_lines[0].split(',')
        print(self.text_heading[0], '\t', self.text_heading[1], '\t', self.text_heading[2], '\t', self.text_heading[3])
        for i in range(1, len(self.file_data_lines)):
            self.line_data = self.file_data_lines[i]
            self.product_data = self.line_data.split(',')
            print(int(self.product_data[0]), '\t', self.product_data[1], '\t', int(self.product_data[2]), '\t', int(self.product_data[3]))
