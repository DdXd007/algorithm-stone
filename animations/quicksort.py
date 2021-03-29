from manimlib import *
sys.path.insert(0, './')
sys.path.insert(0, './src')
from algo_stack import *
from algo_vector import *
from algo_scene import *

class QuickSort(AlgoScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.partition_time = 0

    def scale(self, s):
        self.camera.frame.set_width(self.camera.frame.get_width()/s)
        self.camera.frame.set_height(self.camera.frame.get_height()/s)
    
    def add_span(self, arr, low, high):
        l = arr.submobjects[low].get_bounding_box_point(DOWN)
        h = arr.submobjects[high].get_bounding_box_point(DOWN)
        local color = self.rand_color()
        span = Line(l, h, color=color)
        delta = DOWN*self.partition_time*0.3
        span.shift(delta)
        span_left = Line(l, l+delta, color=color)
        span_right = Line(h, h+delta, color=color)
        self.play(ShowCreation(span), ShowCreation(span_left), ShowCreation(span_right))

    def partition(self, arr, low, high):
        self.partition_time += 1
        # 增加一条横线
        self.add_span(arr, low, high)
        anchor = arr.get(high)
        # 高亮锚点
        arr.submobjects[high].set_color(BLUE)

        i = low - 1
        for j in range(low, high):
            if arr.get(j) <= anchor:
                i += 1
                self.show_message("交换%d %d"%(i, j))
                arr.swap(i, j)
                self.wait()
        self.show_message("交换%d %d"%(i+1, high))
        arr.swap(i+1, high)
        self.wait()
        return i+1

    def quick_sort(self, arr, low, high):
        if low >= high:
            return
        p = self.partition(arr, low, high)
        self.quick_sort(arr, low, p-1)
        self.quick_sort(arr, p+1, high)

    def construct(self):
        self.scale(1)
        self.init_message("快速排序")
        self.datas = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]

        arr = AlgoVector(self, self.datas)
        arr.to_edge(edge=UP)
        for i in range(arr.size()):
            arr.set_sub(i, str(i))

        self.play(ShowCreation(arr))
        self.quick_sort(arr, 0, arr.size()-1)
        self.show_message("完成快速排序，谢谢观看！")
        self.finish()
