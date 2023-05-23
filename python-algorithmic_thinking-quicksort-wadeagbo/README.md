# Python-algorithmic_thinking-quicksort

Implement the quicksort presented in pseudo code below in Python in the `quicksort.py` file. Then run the `app.py` file to test your implementation. Write a unit test to confirm your sorting works.

```
BEGIN QuickSort(list, low=0, high=-1)
  IF high == -1
    high = LENGTH OF list -1
  ENDIF
  IF low < high
    pi = Partition(list, low, high)
    QuickSort(list, low, pi - 1)
    QuickSort(list, pi + 1, high)
  ENDIF
END QuickSort

BEGIN Partition(list, low, high)
  pivot = list[high]  
  i = low - 1
  FOR j FROM low TO high
    IF list[j] < pivot
      i++
      SWAP list[i] AND list[j]
    ENDIF
  ENDFOR
  SWAP list[i + 1] AND LIST[high]
  RETURN i + 1
END Partition
```

Source: https://www.geeksforgeeks.org/quick-sort/

Watch video: https://youtu.be/7h1s2SojIRw

Analysis of Quick sort algorithm: https://youtu.be/-qOVVRIZzao 
