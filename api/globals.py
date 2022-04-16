class Dataset:
    
    dataset = []
    
    def __init__(self, value={}):
        pass
    
    def __getitem__(self, key):
        for data in self.dataset:
            if key in data.keys():
                return data[key]
        self.__setitem__(key, None)
    
    def __setitem__(self, key, value):
        # TODO: delete duplicates
        self.dataset.append({key : value})
    
    def get(self):
        list = []
        final_list = []
        for i in range(len(self.dataset)):
            try: 
                list.append(self.dataset[i] | self.dataset[i+1])
                i += 1
            except:
                pass
        print(list)
        k = 2;
        for i in range(len(list)):
            dict = {}
            while (list[i]['timestamp'] == k) :
                dict = list.pop(0)
            final_list.append(dict) 
            k += 1
        return final_list 


dataset = Dataset({})






