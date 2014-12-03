# Compiler used
CC=g++
# Any flags to be continually reused go here
CFLAGS=-c

#all: aew0024_prj02

aew0024_prj02: commandline.o configuration.o reportT.o tool.o main.o
	$(CC) commandline.o configuration.o reportT.o tool.o main.o -o aew0024_prj02

commandline.o: commandline.cpp commandline.h
	$(CC) $(CFLAGS) commandline.cpp -o commandline.o

configuration.o: configuration.cpp configuration.h
	$(CC) $(CFLAGS) configuration.cpp -o configuration.o

reportT.o: reportT.cpp reportT.h
	$(CC) $(CFLAGS) reportT.cpp -o reportT.o

tool.o: tool.cpp tool.h
	$(CC) $(CFLAGS) tool.cpp -o tool.o
clean:
	rm -rf commandline.o configuration.o reportT.o tool.o main.o aew0024_prj02