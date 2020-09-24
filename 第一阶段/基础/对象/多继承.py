class Father:
    def __init__(self, eyelid, nose):
        self.eyelid = eyelid
        super().__init__(nose)

    def make_money(self):
        print("遗传父亲的赚钱方式!")
        super().make_money()


class Mother:
    def __init__(self, nose):
        self.nose = nose

    def make_money(self):
        print("遗传母亲的赚钱方式!")


class Child(Father, Mother):
    pass


ls = Child("单眼皮","高鼻梁")
print(ls.eyelid)
print(ls.nose)
ls.make_money()
print(Child.mro())