



class MergeSort:
    def __init__(self, a, comp):
        self.a = a
        self.comp = comp

    def sort(self):
        self.a = self.merge_sort(0, len(self.a) - 1)
        print(self.a)

    def merge_sort(self, start, end):
        if start == end:
            return [self.a[start]]

        mid = (start + end) // 2
        left = self.merge_sort(start, mid)
        right = self.merge_sort(mid + 1, end)

        a = []
        l_index = 0
        r_index = 0

        while l_index < len(left) or r_index < len(right):
            if l_index >= len(left):
                a.append(right[r_index])
                r_index += 1
            elif r_index >= len(right):
                a.append(left[l_index])
                l_index += 1
            elif self.comp(right[r_index], left[l_index]):
                a.append(right[r_index])
                r_index += 1
            else:
                a.append(left[l_index])
                l_index += 1
        return a