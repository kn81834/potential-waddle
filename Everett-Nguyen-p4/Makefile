GPP = g++
CFLAGS = -Wall -std=c++14 -g -O0 -pedantic-errors

all: launcher.o tokeit.o
	$(GPP) -o launcher launcher.o
	$(GPP) -o tokeit tokeit.o

launcher.o: launcher.cpp
	$(GPP) $(CFLAGS) -c launcher.cpp

tokeit.o: tokeit.cpp
	$(GPP) $(CFLAGS) -c tokeit.cpp

clean:
	rm -rf *.o launcher tokeit
	
