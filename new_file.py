def my_prnt(sometext):
    if sometext != "Ctrl+C":
        print(sometext)
    else: 
        raise Exception('The End')

try:
    while True:
        my_prnt(input())
except Exception as e:
    print(e)
except KeyboardInterrupt:
    print('The End')
