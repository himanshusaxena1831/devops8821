try:
    f = open("data.txt")
    try:
        f.write("hello world")
    except:
        print("something went wrong when the file is open!")
    finally:
        f.close()
except:
    print("something went wrong")
