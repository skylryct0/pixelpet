

#include<iostream>
#include<cstdlib>

main() {
   int max;
   max = 6;
   srand(time(0));
  
   int tips[6] = {"Is that really what you should be doing?", "Questionable selection of operating systems", "Don't mind me", "Chrome is an abomination of a \'browser\'", "my favourite distro is artix", "UwU compile your kernel fwom source to squeeze extra performance"};
   cout << tips[rand()%max];
}
