indian=["samosa", "paratha", "tea"]
italian=["pizza", "pasta", "fries"]
chinese=["chowmein", "spring roll", "chilli potato"]

dish=input("Enter the name of DIsh: ")
if dish in indian:
    print("Indian")
elif dish in italian:
    print("Italian")
elif dish in chinese:
    print("Chinese")
else:
    print("unrecognised dish")