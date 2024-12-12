#include <iostream>
using namespace std;

struct node {
    public:
    string name;
    int prn;
    node* next

    node(int a , string b){
        name = b;
        prn = a;
        next = NULL;
    }
}

class a{
    head = NULL;
    tail = NULL;

    void add(int a, string b){
        node* newnode = new node(a, b);
        if (head == NULL){
            head = tail = newnode;
            head -> next = NULL;
            return
        }
        tail->next = newnode;
        tail = newnode; 
    }

    void delet (prn){
        node* curr = head;
        if (prn == head->data){
            temp  =head ;
            head = head -> next;
            delete temp
        }
        while (curr->next != NULL){
            if (curr->next->data == prn){
                temp = curr->next;
                curr->next = curr->next->next;
                delete temp;
            }
        }
    }
    // similarly for total and all other logics

};