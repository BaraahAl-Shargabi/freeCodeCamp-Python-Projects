class HashTable:
    def init(self):
        self.collection = {}  # القاموس الرئيسي

    def hash(self, key):
        return sum(ord(char) for char in key)

    def add(self, key, value):
        hashed_key = self.hash(key)
        if hashed_key not in self.collection:
            # لو هذا الـ hash جديد → نعمل dict داخلي
            self.collection[hashed_key] = {}
        # نخزن key-value داخل dict الداخلي
        self.collection[hashed_key][key] = value

    def remove(self, key):
        hashed_key = self.hash(key)
        if hashed_key in self.collection:
            inner_dict = self.collection[hashed_key]
            if key in inner_dict:
                del inner_dict[key]
            # لو انتهى dict الداخلي → نحذف الـ hash نفسه
            if not inner_dict:
                del self.collection[hashed_key]

    def lookup(self, key):
        hashed_key = self.hash(key)
        if hashed_key in self.collection:
            inner_dict = self.collection[hashed_key]
            if key in inner_dict:
                return inner_dict[key]
        return None