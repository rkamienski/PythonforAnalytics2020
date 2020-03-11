def hello():
	return "Hello!"
    
class salad():
    def __init__(self):
        self.path = ''
        self.items = []
        self.numbers = []
    def write(self, path, salad, n_items):
        self.path = path
        print(self.path)
        assert len(salad) == len(n_items), "The lists must be equal length."
        os.makedirs(self.path, exist_ok=True)
        for k in range(len(salad)):
            print(salad[k],n_items[k])
            for j in range(n_items[k]):
                file_name = salad[k] + '_' + str('{:0>2}'.format(j)) + '.salad'
                f = open(os.path.join(self.path, file_name), "w+")
                f.close()
        return
    def read(self, path):
        flist = glob.glob(os.path.join(path,'*.salad'))
        a = []
        for file in flist:
            pattern = r"(\w+)(\d\d).salad"
            a.append(re.findall(pattern, file))
        return a

path = 'mysalad'
salad_items = ['lettuce', 'tomato']
salad_numbers = [2,3]
mysalad = salad()
mysalad.write(path, salad_items, salad_numbers)
flist = mysalad.read(path)
print(flist)
   