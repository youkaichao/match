class personalInfo:
    def __init__(self, line):
        # line = []
        self.Info = []
        for x in range(4):
            self.Info.append(line.pop(0))
        """
        Info[0] : name
        Info[1] : sex
        Info[2] : telephone number
        Info[3] : wechat account
        """
        if self.Info[1] == "1":
            self.Info[1] = "男"
        else:
            self.Info[1] = "女"
    def __str__(self):
        return "姓名：" + self.Info[0] + " " + "性别：" + self.Info[1] + " " + "电话：" + self.Info[2] + " " + "微信：" + self.Info[3]
    __repr__ = __str__