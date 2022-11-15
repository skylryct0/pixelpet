#/bin/bash

echo "Hello world. Today we are going to play a game of Russian Roulette. But first, I will tell you that I spare all linux and bsd users so if u use macOS then skill issue on ur part"

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        echo "hail the almighty tux, my fellow linux master race. you may pass"
        
elif [[ "$OSTYPE" == "darwin"* ]]; then
       
       
elif [[ "$OSTYPE" == "cygwin" ]]; then
         "Windows peseant, but idk how to delete ur system32 with a bash script so ig ur safe" 
elif [[ "$OSTYPE" == "msys" ]]; then
         "Windows peseant, but idk how to delete ur system32 with a bash script so ig ur safe" 
elif [[ "$OSTYPE" == "win32" ]]; then
         "hmm, still a windows peseant." 
elif [[ "$OSTYPE" == "freebsd"* ]]; then
        # ...
else
        "wtf"
fi

