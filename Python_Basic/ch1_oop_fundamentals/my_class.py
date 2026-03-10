class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def run(self):
        print(self.name, "正在运动")

    def eat(self):
        pass


class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "名字是：%s, 占地面积是：%s" % (self.name, self.area)


class House:
    def __init__(self, house_type, area, item):
        self.house_type = house_type
        self.area = area
        self.items = [i for i in item]

    def add_item(self, item: HouseItem):
        print("添加物品：%s" % item.name)
        if item.area > self.area:
            print("空间不足")
            return
        self.area -= item.area
        self.items.append(item.name)


if __name__ == '__main__':
    my_str = '0123456789'
    print(my_str[::-1])
