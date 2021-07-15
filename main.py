
from algorithms.graph.cycle_detection import CycleDetection
import time
import math

if __name__ == '__main__':
    start = time.time()

    al_1 = [[], [0]]
    al_2 = [[1], [0]]
    al_3 = [[], [0, 3], [1], [2]]

    CycleDetection(al_3)




    # inputs = ["12", "123", "11223"]
    # for i in range(len(inputs)):
    #     DecodeWays(inputs[i])
    #
    # DecodeWays("1111")
    """
    1       --> 1
    11      --> 2
    111     --> 111, 11 1, 1 11
    1111    --> 1111, 11 11, 11 1 1, 1 1 11, 1 11 1,
    
    """


    # WordBreak("educativeio", ["educative", "io"])
    # WordBreak("aab", ["a", "c"])
    # WordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", "a aa aaa aaaa aaaaa aaaaaa aaaaaaa aaaaaaaa aaaaaaaaa aaaaaaaaaa".split())


    # EditDistance("bat", "but")
    # EditDistance("abdca", "cbda")
    # EditDistance("passpot", "ppsspqrt")

    # Longest([1, 2, 3, 4])
    # Longest([3, 2, 1, 4])
    # Longest([1, 3, 2, 4])


    # PatternMatching("baxmx", "ax")
    # PatternMatching("tomorrow", "tor")

    # Longest("tomorrow")
    # Longest("aabdbcec")
    # Longest("fmff")

    # SuperSeq("abcf", "bdcf")
    # SuperSeq("dynamic", "programming")

    # MaxSum([4,1,2,6,10,1,12])
    # MaxSum([-4,10,3,7,15])

    # MinTransform("abc", "fbc")
    # MinTransform("abdca", "cbda")
    # MinTransform("passport", "ppsspt")

    # a = [1, 2, 7, 1]
    # TargetSum(a, 9)

    # a = "abdbca"
    # Palin(a)
    # a = "cddpd"
    # Palin(a)
    # a = "pqr"
    # Palin(a)
    # a = "pp"
    # Palin(a)



    # lengths, prices, capacity = [1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5
    #
    # RodCutting(lengths, prices, capacity)


    # Correctness(CircularLinkedList, "insert", "remove")
    # Correctness(CircularQueue, "enqueue", "dequeue")
    # a = AVL(lambda x, y: x < y)
    # a.insert(10)
    # a.insert(20)
    # a.insert(30)
    # a.insert(40)

    # al = [[1], [2], [3, 4], [0], [5], [6], [4, 7], []]
    # k = Kosaraju(al)

    # al = [[1, 2], [2, 3, 4], [1, 3, 4], [], [3]]
    # w = {(0, 1): 4,
    #      (0, 2): 2,
    #      (1, 2): 3,
    #      (1, 3): 2,
    #      (1, 4): 3,
    #      (2, 1): 1,
    #      (2, 3): 5,
    #      (2, 4): 4,
    #      (4, 3): -5}
    # b = Bellman(al, w)


    # a = [6, 5, 8, 9, 10, 12, 2, 1]
    # m = QuickSort(a, lambda x, y: x < y)
    # m.sort()

    # a = [6, 5, 8, 9, 10, 12, 2, 1]
    # m = CountingSort(a)
    # m.sort()

    # a = [6, 5, 8, 9, 10, 12, 2, 1]
    # m = RadixSort(a)
    # m.sort()

    # al = [[1, 4], [2], [4, 5], [5], [2, 3], []]
    # w = {(0, 1): 8,
    #      (0, 4): 3,
    #      (1, 2): 9,
    #      (2, 5): 2,
    #      (3, 5): 5,
    #      (4, 2): 7,
    #      (4, 3): 4,
    #      (2, 4): 7}
    # b = Ford(al, w, 0, 5)
    # b.max_flow()

    # al = [[1, 2], [0, 2], [0, 1, 3, 4, 5], [2, 5], [2, 5], [2, 3, 4]]
    # w = {(0, 1): 4,
    #      (0, 2): 4,
    #
    #      (1, 0): 4,
    #      (1, 2): 2,
    #
    #      (2, 0): 4,
    #      (2, 1): 2,
    #      (2, 3): 3,
    #      (2, 4): 1,
    #      (2, 5): 6,
    #
    #      (3, 2): 3,
    #      (3, 5): 2,
    #
    #      (4, 2): 1,
    #      (4, 5): 3,
    #
    #      (5, 2): 6,
    #      (5, 3): 2,
    #      (5, 4): 3
    #      }

    # al = [[1, 2], [0, 2], [0, 1, 3, 4, 5], [2, 5], [2, 5], [2, 3, 4]]
    # w = {(0, 1): 4,
    #      (0, 2): 4,
    #
    #      (1, 0): 4,
    #      (1, 2): 2,
    #
    #      (2, 0): 4,
    #      (2, 1): 2,
    #      (2, 3): 1000,
    #      (2, 4): 1000,
    #      (2, 5): 1000,
    #
    #      (3, 2): 1000,
    #      (3, 5): 2,
    #
    #      (4, 2): 1000,
    #      (4, 5): 3,
    #
    #      (5, 2): 1000,
    #      (5, 3): 2,
    #      (5, 4): 3
    #      }
    # b = Prims(al, w)
    # b.find()

    # al = [[1, 3], [0, 3], [1], [2]]
    # w = {(0, 1): 3,
    #      (0, 3): 5,
    #
    #      (1, 0): 2,
    #      (1, 3): 4,
    #
    #      (2, 1): 1,
    #
    #      (3, 2): 2
    #      }
    # b = Floyd(al, w)

    # r = Rabin("AAAAAAAAAAAAAAAAAAAAAAAAB")
    # print(r.is_match("AAAB"))

    end = time.time()
    print(f"{end - start:.9f} seconds")

