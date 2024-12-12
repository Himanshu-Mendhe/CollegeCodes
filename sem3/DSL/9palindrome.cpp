#include <iostream>
#include <string>
using namespace std;

#define MAX 30
int top = -1;

class stac{
    public:
    char arr[MAX];

    void push(int a){
        top ++;
        arr[top] = a;
        arr [top+1] ='\0';
    }
    char pop(){
        if (top ==-1){cout<<"underflow"<<endl;return;}
        cout<< arr[top]<<endl;
        return arr[top];
        top --;
        arr[top+1]='\0';
        
    }
    void display() {
        if (top == -1) {
            cout << "Stack is empty." << endl;
            return;
        }
        for (int i = 0; i <= top; i++) {
            cout << arr[i];
        }
        cout << endl;
    }

};



int main (){
    stac hii;

    string abc;
    cout<< "enter the string"<<endl;
    getline(cin,abc);
    for (int i = 0; i<abc.length(); i++){
        if (isalnum(abc[i] )){
            hii.push(tolower(abc[i]));
            cout<<abc[i];
        }
    }cout<<endl;

    hii.display();

    while (arr!='\0'){
        if (pop() !=  )
    }
     

    return 0;
}