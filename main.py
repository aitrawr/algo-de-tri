import random
import time

def insertion_sort(arr, low, high):
       for i in range(low + 1, high + 1):
          key = arr[i]
          j = i - 1
          while j >= low and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
                arr[j + 1] = key
          
def merge(arr, l, m, r):
      n1 = m - l + 1
      n2 = r - m


      L = arr[l:l + n1]
      R = arr[m + 1:m + 1 + n2]

      i = j = 0
      k = l

      while i < n1 and j < n2:
            if L[i] <= R[j]:
               arr[k] = L[i]
               i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
             
      while i < n1:
             arr[k] = K[i]
             i += 1
             k += 1

      while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1


def merge_sort(arr, l=None, r=None):
      if l is None:
            l = 0 
      if r is None:
            r = len(arr) - 1

      if r - l + 1 <= 5:
            insertion_sort(arr, l, r)
      elif l < r:
            m = (l + r) // 2

            merge_sort(arr, l, m)
            merge_sort(arr, m + 1, r)

            merge(arr, l, m, r)
      


def generate_random_numbers(count):
     return [random.randint(0, 10000) for _ in range(count)] #numbers list

def display_sorted_array(arr):
        print("sorted array:")
        for element in arr:
             print(element, end=" ")
        print()

if __name__ == "__main__":
        random_numbers = generate_random_numbers(10000) #quantity of numbers
        print("Original array:", random_numbers)
        start_time = time.time()
        merge_sort(random_numbers)
        end_time = time.time()
        display_sorted_array(random_numbers)


        elapsed_time = end_time - start_time
        print(f"temp pri: {elapsed_time:.6f} secondes")
        
        
