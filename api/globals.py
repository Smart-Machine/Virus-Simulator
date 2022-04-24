class Dataset:
    
    dataset = []

    def __init__(self, value={}):
        self.dataset.append(value)


    def add(self, **data):
        d = self.dataset[-1]
        if data['timestamp'] == d['timestamp']:
            d['cases'] = data['cases']
            return
        self.dataset.append({**data})


    def get(self):
        return self.dataset
    

dataset = Dataset({
    'cases' : 0,
    'timestamp': 0
})






