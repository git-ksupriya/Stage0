# test script for stage0
import BubbleSort

def test_bubble():
    a=[[],[5,3,2,4,7,1],[5,5,2,2,2,7,0],[5,6,3,3,3]]
    for i in a:
        b=BubbleSort.bubblesort(i)
        i.sort()
        print(i,b,' timsort, bubblesort ')
        if i!=b:
            print("Error for: ",i)
            return False 
    print("All Correct")
    return True


test_bubble()
