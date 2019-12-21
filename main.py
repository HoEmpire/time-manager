'''
test case
11.22-13.22 魔域 3
23.10-1.20 打游戏 6
23.10-1.20. 打游戏 6
'''


class time_24h():
    def __init__(self, time):
        comma_index = time.find('.')
        self.hour = int(time[:comma_index])
        self.minute = int(time[comma_index + 1:len(time)])
        #print(self.hour)
        #print(self.minute)

    def __sub__(self, other):
        duration = 60 * (self.hour - other.hour) + (self.minute - other.minute)
        if duration < 0:
            duration += 24 * 60
        return duration


class event():
    def __init__(self, block_event_list):
        self.time = block_event_list[0]
        self.content = block_event_list[1]
        self.label = block_event_list[2]
        all_tpye = ['生活必须', '干活', '专业发展', '个人发展', '运动', '享受', '浪费']
        self.type = all_tpye[int(self.label)]
        self.cal_duration()

    def cal_duration(self):
        index_minus = self.time.find('-')
        self.time_start = time_24h(self.time[:index_minus])
        self.time_end = time_24h(self.time[index_minus + 1:len(self.time)])
        self.duration = self.time_end - self.time_start
        #print(self.duration)

    def report(self):
        print('*****记录成功*****')
        print('开始时间:{}时{}分'.format(self.time_start.hour,
                                   self.time_start.minute))
        print('结束时间:{}时{}分'.format(self.time_end.hour, self.time_end.minute))
        print('持续时间:{}分钟'.format(self.duration))
        print('内容:{}'.format(self.content))
        print('类型:{}'.format(self.type))


def input_new_event():
    onscreen = "输入事件(xx.xx-xx.xx 内容 分类):\n"
    onscreen += "1-生活必须\n"
    onscreen += "2-干活\n"
    onscreen += "3-专业发展\n"
    onscreen += "4-个人发展\n"
    onscreen += "5-运动\n"
    onscreen += "6-享受\n"
    onscreen += "7-浪费\n"

    str = input(onscreen)
    block_event_list = []

    if str.count(' ') != 2:
        print('小伙子输入的长度错误')
    else:
        space_index1 = str.find(' ')
        space_index2 = str.find(' ', space_index1 + 1)
        block_event_list.append(str[:space_index1])
        block_event_list.append(str[space_index1 + 1:space_index2])
        block_event_list.append(str[space_index2 + 1:])
        #print(block_event_list)
        if input_event_verify(block_event_list):
            new_event = event(block_event_list)
            new_event.report()
        else:
            print('小伙子输入格式错误')


def input_event_verify(block_event_list):
    is_input_right = True
    if (block_event_list[0].count('.') !=
            2) or (block_event_list[0].count('-') != 1) or (int(
                block_event_list[2]) < 1) or (int(block_event_list[2]) > 7):
        is_input_right = False
    return is_input_right


input_new_event()
