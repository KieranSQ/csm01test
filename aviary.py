class Aviary:
    def __init__(self):
        self.data = []
        
    def add(self, x):
        self.data.append(x)
        
    def addtwice(self, x):
        self.add(x)
        self.add(x)

    def count(self):
        return(len(self.data))

    def get_dict(self):
        common_name_dict = {}
        for owl in self.data:
            if owl.common_name in common_name_dict.keys(): #default is .keys()
                common_name_dict[owl.common_name]   += 1 
            
            else:
                common_name_dict[owl.common_name] = 1
            
            
        return common_name_dict


    def describe(self):
        for owl in self.data:
            print( owl.get_info()) #return only returns once
        