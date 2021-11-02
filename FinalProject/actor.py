def main():
    infile = open('bestactor.txt', 'r')
    outfile = open('oscars.txt', 'w')
    getData(infile, outfile)
    infile = open('oscars.txt', 'r')
    display(infile)
    infile.close()

def getData(infile, outfile):
    for line in infile:
        info = line.rstrip('\n').split()
        sentence = info[0] + ' ' + info[1] + " won the Best Actor Oscar in " + info[2] + " for " + info[3] + '.'
        outfile.write(sentence + '\n')
    outfile.close()

def display(infile):
    line = infile.readline()
    while line:
        print(line.rstrip('\n'))
        line = infile.readline()

main()