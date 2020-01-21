#include <string>
#include <iostream>

//http://www.cplusplus.com/forum/general/11104/
#include <limits.h>
#include <unistd.h>

std::string getexepath()
  {
  char result[ PATH_MAX ];
  ssize_t count = readlink( "/proc/self/exe", result, PATH_MAX );
  return std::string( result, (count > 0) ? count : 0 );
  }
  
  
using namespace std;
string userDir = "/home/ugrads/everett";
int main(){
  bool userexit = true;
  
  while(userexit){
    
    
    cout << "1730sh:" << getexepath() << "$ "; 


    
    string stringy;
    getline(cin, stringy);
    if (stringy.compare("exit")){
      userexit = false;
    }
  }  
  
  

}
