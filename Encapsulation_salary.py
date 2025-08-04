class employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary

    def get_salary(self):
        return self.__salary
    
    def set_salary(self,amount):
        if amount > 0:
            self.__salary += amount


