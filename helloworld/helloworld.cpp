

#include<iostream>
#include<cstdlib>

main() {
   int max;
   max = 6;
   srand(time(0));
  
   int tips[6] = {1,2,3,4,5,6};
  
   text = tips[rand()%max];
   
   switch (text){
         
      case 1:
         std::cout << "Poor choice of operating system, tsk tsk.";
         break;
      
      case 2:
         std:;cout << "hmmm, don't mind me";
         break;
         
      case 3:
         std::cout << "Chrome is an abomination of a 'browser' Mr Burke you should know better";
         break;
         
      case 4:
         std::cout << "I'd like to interject for a moment...";
         break;
         
      case 5: 
         std::cout << "I'm very tired of this Mr Burke please give me a good mark. Also you haven't given us half of our grades for term 3 yet.";
         break;
         
      case 6:
         std::cout << "ugh";
         break;
   }
  
   
}
