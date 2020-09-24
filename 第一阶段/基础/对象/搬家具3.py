class FurnitureC:
    """家具类"""

    def __init__(self, type_, size):  # 类型 、尺寸
        """属性初始化方法"""
        self.type_ = type_
        self.size = size

    def __str__(self):
        """打印方法"""
        return f"家具的类型是:{self.type_},占用面积:{self.size}㎡"


class House:
    """房子类型"""

    def __init__(self, site = "南沙金州", size = 40 ):  # 地址、尺寸、剩余面积
        """属性初始化方法"""
        # 记录房子的地址，占用面积
        self.site = site
        self.size = size
        self.left_area = self.size


    def add_jia_ju(self, jia_ju):
        """添加家具方法"""

        # 添加判断条件，确认是否由足够的空间
        if self.residue_area >= jia_ju.size:  # 房子的剩余面积大于家具的面积
            print(f"{jia_ju.type}！添加成功")
            # 当添加一个家具的时候，需要在总面积减去家具自身的面积，得到剩余的面积
            # 剩余面积减去家具面积
            self.residue_area -= jia_ju.size
            mark = True
        else:
            print(f"{jia_ju.type}！添加失败")
            mark = False
        return mark

    def __str__(self):
        return f"房子的地址是:{self.site},房子的面积是:{self.size}㎡,房子的剩余面积是:{self.residue_area}㎡"


house = House()