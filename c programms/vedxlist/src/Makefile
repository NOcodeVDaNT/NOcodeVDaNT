CC = gcc
CFLAGS = -Wall

all: vedxlist

vedxlist: vedxlist.o
	$(CC) $(CFLAGS) -o vedxlist vedxlist.o

vedxlist.o: vedxlist.c vedxlist.h
	$(CC) $(CFLAGS) -c vedxlist.c

clean:
	del *.o vedxlist
