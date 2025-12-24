#1) poem.txt contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in your python program and find out words with maximum occurance.

#Ans1
words=[]
with open("C:/Users/Lakshya/Desktop/Python Projects/Sample/poem.txt", "r") as f:
    for line in f:
        words_ln=line.split()
        words=words + words_ln
word_count={}
for word in words:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1
print(word_count)

word_occurances=list(word_count.values())
print("Max no of occurrences:", max(word_occurances))

for k,v in word_count.items():
    if v==max(word_occurances):
        print(k)

#2) stocks.csv contains stock price, earnings per share and book value. You are writing a stock market application that will process this file and create a new file with financial metrics such as pe ratio and price to book ratio. These are calculated as,
#pe ratio = price / earnings per share
#price to book ratio = price / book value
#Your input format (stocks.csv) is,

#Company Name	Price	Earnings Per Share	Book Value
#Reliance	1467	66	653
#Tata Steel	391	89	572
#Output.csv should look like this,

#Company Name	PE Ratio	PB Ratio
#Reliance	22.23	2.25
#Tata Steel	4.39	0.68

#Ans2)

with open("C:/Users/Lakshya/Desktop/Python Projects/Sample/stocks.csv", "r") as f1:
    with open ("C:/Users/Lakshya/Desktop/Python Projects/Sample/stocks_out.csv", "w") as f2:
        next(f1)
        f2.write("Company Name,PE Ratio,PB Ratio\n")
        for line in f1:
            sep=line.split(",")
            print(sep)
            sep[1]=int(sep[1])
            sep[2]=int(sep[2])
            sep[3]=int(sep[3])
            f2.write(f"{sep[0]},{round(sep[1]/sep[2],2)},{round(sep[1]/sep[3],2)}\n")






