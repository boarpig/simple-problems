one:
	gcc lists1.c --std=c99 -Wall -o lists1.o

two:
	gcc lists2.c --std=c99 -Wall -lm -o lists2.o

all: one two

clean:
	rm *.o
