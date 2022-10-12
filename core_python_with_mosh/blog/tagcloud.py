class TagCloud:

    def __init__(self):
        self.tags = {}

    def add(self, param):
        """
        param_lower = str(param).lower()
        if param_lower in self.tags.keys():
            self.tags[param_lower] += 1
        else:
            self.tags[param_lower] = 1
        """
      #  self.tags[param.lower()] = self.tags.get(param.lower(), 0) + 1
        self[param] = self[param] + 1
        print(f"Tag Cloud add({param.lower()}) : {str(self)}")

    def remove(self, param):
        """
        param_lower = str(param).lower()
        if param_lower in self.tags.keys():
            self.tags[param_lower] -= 1
        """
#        self.tags[param.lower()] = self.tags.get(param.lower(), 0) - 1
        self[param] = self[param] - 1
        print(f"Tag Cloud remove({param.lower()}) : {str(self)}")

    def is_empty(self):
        return len(self.tags) == 0

    def __str__(self):
        if self.is_empty():
            return f"\nEmpty Tag Cloud"
        tag_cloud_str = ""
        for k, v in self.tags.items():
            tag_cloud_str += "#"+k+": "+str(v)+" "
        return tag_cloud_str

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
            return iter(self.tags)

    def clear(self):
        self.tags.clear()
