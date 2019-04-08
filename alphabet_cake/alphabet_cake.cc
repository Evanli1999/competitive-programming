#include <iostream>
#include <string>

char** cake;
int* columnCounts;
int tests, R, C;

void printSolution() {
	char toPrint = 0;
	for(int i = 0; i < R; i++) {
		for(int j = 0; j < C; j++) {
			if(cake[i][j] != 0) {
				toPrint = cake[i][j];
				printf("%c", toPrint);
			} else {
				printf("%c", toPrint);
			}
		}
		printf("\n");
	}
}

void printArray() {
	for(int i = 0; i < R; i++) {
		for(int j = 0; j < C; j++) {
			printf("%c ", cake[i][j]);
		}
		printf("\n");
	}
}

void printCounts() {
	for(int i = 0; i < C; i++) {
		printf("%d ", columnCounts[i]);
	}
	printf("\n");
}

int countInRange(int y, int x, int h, int w) {
	int count = 0;
	for(int i = 0; i < h; i++) {
		for(int j = 0; j < w; j++) {
			if(cake[y+i][x+j])
				count++;
		}
	}
	return count;
}

void recur(int x1, int x2) { //x1 is start, x2 is the last column of partition
	//printf("recur <%d,%d>\n", x1, x2);

	int maxCol = 0;
	int maxCount = 0;
	int numColumnsNonZero = 0;

	for(int i = x1; i <= x2; i++) {
		if(columnCounts[i] != 0) {
			numColumnsNonZero++;
			if(columnCounts[i] > maxCount || numColumnsNonZero == 2) {
				maxCol = i;
			}
		}
	}

	if(numColumnsNonZero == 1) {
		char fill = 0;
		int startAt = 0;
		for(int i = 0; i < R; i++) {
			if(cake[i][maxCol] != 0) {
				fill = cake[i][maxCol];
				for(int j = startAt; j <= i; j++)
					cake[j][x1] = fill;
				startAt = i+1;
			}
		}

		for(int i = startAt; i < R; i++) {
			cake[i][x1] = fill;
		}
	} else {
		recur(x1, maxCol-1);

		for(int i = maxCol+1; i <= x2; i++) {
			if(columnCounts[i] != 0) {
				recur(maxCol, maxCol);
				if(maxCol != x2) {
					recur(maxCol+1, x2);
				}
				return;
			}
		}
		recur(maxCol, x2);
	}
	return;
}

int main() {
	std::cin >> tests;
	for(int i = 0; i < tests; i++) {
		std::cin >> R >> C;
		cake = new char*[R];
		columnCounts = new int[C];

		for(int i = 0; i < C; i++)
			columnCounts[i] = 0;

		for(int i = 0; i < R; i++) {
			cake[i] = new char[C];
		}

		std::string row;
		for(int i = 0; i < R; i++) {
			std::cin >> row;
			for(int j = 0; j < C; j++) {
				if(row.at(j) != '?') {
					cake[i][j] = row.at(j);
					columnCounts[j]++;
				} else {
					cake[i][j] = 0;
				}
			}
		}

		recur(0, C-1);
		printf("Case #%d:\n", i+1);
		printSolution();

		for(int i = 0; i < R; i++) {
			delete[](cake[i]);
		}
		delete[] cake;
		delete[] columnCounts;
	}
	return 0;
}
