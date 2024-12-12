/*Department of Computer Engineering has student’s club named ‘Pinnacle Club’. Students of second, third and final year of department can be granted membership on request. Similarly, one may cancel the membership of club. First node is reserved for president of club and last node is reserved for secretary of club. Write C++ program to maintain club member’s information using singly linked list. Store student PRN and Name. Write functions to:
a) Add and delete the members as well as president or even secretary.
b) Compute total number of members of club.
c) Display members.
d) Two linked lists exists for two divisions. Concatenate two lists.*/


#include <iostream>
#include <string>
using namespace std;

struct node {
    public:
    int prn;
    string name;
    node* next;

    node (int a, string n){
        prn = a;
        name = n;
        next = NULL;
    }
};

class sll{

    private:
    node* head;
    node* tail;

    public:

    sll(){
        head = NULL;
        tail = NULL;
    }
    ~sll(){
        node* temp ;
        while (head != NULL){
            temp = head;
            head = head ->next;
            delete temp;
        }
    }

    void add (int prn, string name){
        node* newNode = new node (prn, name);
        if (head == NULL){
            head = tail = newNode;
        }
        else {
            tail -> next = newNode;
            tail = newNode;
        }
    }
    void display(){

        if (head == NULL){
            cout<<"empty"<<endl;
        }
        else {
            node* temp = head;

            while (temp!= NULL){
            cout<< temp->prn << endl;
            cout<< temp->name << endl;

            temp = temp->next;
            }
        }
    }
    int total(){
        if (head == NULL){
            cout<<"empty";
            return 0;
        }
        else {
            node* temp = head;
            int count = 0;
            while (temp!= NULL){
                count++;
                temp = temp->next;
            }
            cout<<count;
            return count;
        }
    }
    void delet(int prn){
        node* temp = head;
        if (head->prn == prn){
            node* temp1 = head;
            head = head->next;
            delete temp1;
            return;
        }
        while (temp != NULL){
            if (temp->next->prn == prn){
                node* curr = temp->next;
                temp->next = temp->next->next;
                delete curr;
            }
            temp=temp->next;
        }
    }



};

int main(){

    sll abc;
    abc.display();
    abc.add(1, "wdhimanshu");
    abc.add(2, "fhimanshu");
    abc.add(3, "ewfhimanshu");
    abc.display ();
    abc.delet(3);
    abc.total();


    return 0;
}