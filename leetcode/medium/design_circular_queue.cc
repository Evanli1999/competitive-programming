#include <iostream>
#include <string>

using std::cout;
using std::endl;
using std::string;

class MyCircularQueue {
public:
    int cap, num_elements, front;
    int* queue;

    /** Initialize your data structure here. Set the size of the queue to be k. */
    MyCircularQueue(int k): cap(k), num_elements(0), front(0), queue(new int[k]) {}

    /** Insert an element into the circular queue. Return true if the operation is successful. */
    bool enQueue(int value) {
        if(num_elements == cap) { return false; }
        this->queue[(front + num_elements) % cap] = value;
        num_elements++;
        return true;
    }

    /** Delete an element from the circular queue. Return true if the operation is successful. */
    bool deQueue() {
        if(num_elements == 0) { return false; }
        front = (front + 1) % cap;
        num_elements--;
        return true;
    }

    /** Get the front item from the queue. */
    int Front() {
        if(num_elements == 0) { return -1; }
        return this->queue[front];
    }

    /** Get the last item from the queue. */
    int Rear() {
        if(num_elements == 0) { return -1; }
        return this->queue[(front + num_elements - 1) % cap];
    }

    /** Checks whether the circular queue is empty or not. */
    bool isEmpty() {
        return num_elements == 0;
    }

    /** Checks whether the circular queue is full or not. */
    bool isFull() {
        return num_elements == cap;
    }
};

int main() {
}
