def find_minmax(list_a):
       middle = len(list_a) // 2
       
       if(len(list_a) % 2 == 0):
              for i in range(1, middle):
                     if(list_a[0] > list_a[i]):
                            tmp1 = list_a[0]
                            list_a[0] = list_a[i]
                            list_a[i] = tmp1
                     if(list_a[middle] < list_a[middle + i]):
                            tmp2 = list_a[middle]
                            list_a[middle] = list_a[middle + i]
                            list_a[middle + i] = tmp2
       if(len(list_a) % 2 != 0):
              for i in range(1, middle + 1):
                     if(list_a[0] > list_a[i]):
                            tmp1 = list_a[0]
                            list_a[0] = list_a[i]
                            list_a[i] = tmp1
                     if(list_a[middle] < list_a[middle + i]):
                            tmp2 = list_a[middle]
                            list_a[middle] = list_a[middle + i]
                            list_a[middle + i] = tmp2
       return list_a[0], list_a[middle]