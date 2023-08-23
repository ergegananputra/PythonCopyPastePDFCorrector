'''
Copy Paste PDF Corrector
Program untuk membenarkan hasil Copy Paste dari PDF yang memiliki 
format paste salah (terdapat enter pada tengah kalimat)

Membuat heading Upper, Lower, dsb menjadi Title Heading.
'''

def isHeading(string: str, key:str ="_"):
    return True if string[0] == key else False

def main():
    caption : list = []
    strCaption = lambda arr: " ".join(arr)

    with open("input.txt", "r") as streamIn:
        with open("output.txt", "w") as streamOut:
            for line in streamIn.readlines():
                line : str

                if isHeading(line):
                    if len(caption) > 0:
                        streamOut.write(strCaption(caption))
                        streamOut.write("\n\n")
                        caption.clear()
                    
                    streamOut.write(line[1:].title())
                else:
                    caption += line.split()
            else:
                streamOut.write(strCaption(caption))
                

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Something Went Wrong \n\t{e}")
    else:
        print("Completed")
    finally:
        print("Terminated")