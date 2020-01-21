#include <iostream>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/wait.h>
#include <fcntl.h>
#include <string>//check if i can use

using namespace std;

/*
 * Launcher gives user information on termination of a process
 */

int main() {

  string stringy;//input suff
  cin>>stringy;//assume onlyone input
  int pid= fork();
  
  //coverting to char*
  char *stringyHolder = new char[stringy.size()+1];
  stringy.copy(stringyHolder, stringy.size()+1);
  stringyHolder[stringy.size()] = '\0';

  if(0==pid){//in child
    cout << "waiting on child: " << getpid() << endl;
    execlp(stringyHolder, stringyHolder, (char *) NULL);//think child should close after this is executed
    perror("error exec");
  }
  else {
    int term;
    wait(&term);//wait on child to die
    if (WIFEXITED(term)){ //termination by exit
      cout << "teremination by exit" << endl;
      cout << "Exit code: " <<  WEXITSTATUS(term) << endl;
    }
    else if (WIFSIGNALED(term)) {//termination by signal
      cout << "termination by signal"<<endl;
      cout << "signal: " << WTERMSIG(term) << endl;
        //psignal(WTERMSIG(term), "Exit signal");
    }
  }
  
  return 0;
}
