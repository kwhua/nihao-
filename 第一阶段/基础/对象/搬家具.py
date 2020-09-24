class Furniture():
    def __init__(self, type, area):
        self.type = type
        self.area = area

    def __str__(self):
        return f"家具的类型是{self.type},它的占地面积是{self.area}平米."


class House_item(Furniture):
    def __init__(self, adress_, area, residue_area):
        self.adress = adress_
        self.area = area
        self.residue_area = residue_area

    def out_put(self):
        print("房子正在添加{}...")
        print("添加成功")
        print(f"房子在{self.adress},占地面积{self.area}平米,剩余面积为{self.residue_area}平米.")

    def __str__(self):
        return self.out_put()


sofa = Furniture('sofa', 8)
print(sofa)
house = House_item("南沙金州", 40, 40)
print(house)

print("-" * 50)
class Furniture:
    def __init__(self, type, area):
        self.type = type
        self.area = area

    def __str__(self):
        return f'家具的类型是{self.type},占地面积{self.area}平米.'


class House_item:
    def __init__(self, adress, area ):
        self.adress = adress
        self.area1 = area


    def add_furniture(self,furniture):
        furniture = list()

        remaining_area = self.area1-self.area

        return f"房子正在添加{self.type}...\n添加成功\n房子在{self.adress},占地面积{self.area}平米,剩余面积为{self.area1-self.area}平米."

    def __str__(self):

        return
