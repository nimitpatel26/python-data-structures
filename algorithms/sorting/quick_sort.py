
class QuickSort:
    def __init__(self, a, comp):
        self.a = a
        self.comp = comp


    def sort(self):
        self.quick_sort(0, len(self.a) - 1)
        print(self.a)


    def quick_sort(self, start, end):
        if start >= end:
            return

        marker = start
        for i in range(start, end, 1):
            if self.comp(self.a[i], self.a[end]):
                self.a[i], self.a[marker] = self.a[marker], self.a[i]
                marker += 1
        self.a[end], self.a[marker] = self.a[marker], self.a[end]
        self.quick_sort(start, marker - 1)
        self.quick_sort(marker + 1, end)
