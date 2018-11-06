class Student(object):
    """docstring for Student"""

    def __init__(self, name, score):
        self.__name = name  # __name表示name是私有变量
        self.__score = score

    def print_score(self):
        print('%s : %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
    # 外部获取__name和__score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score
    # 外部修改私有数据__name __score

    def set_score(self, score):
        self.__score = score

    def set_name(self, name):
        self.__name = name


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
