import unittest
class CodeTest(unittest.TestCase):
    year = int(input("enter a yr:"))
    if year%4 == 0 :
        if year%100 == 0  :
            if year%400 == 0  :
                print("Leap Year")
            else : 
                print("Not a Leap year")
        else:
            print("Leap Year")
    else : 
        print("Not a Leap year")
        
if __name__ == '__main__':
    unittest.main()   