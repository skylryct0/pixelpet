#pls install ctypes and rust as dependencies

import ctypes

rust = ctypes.CDLL("target/release/librust_lib.so")

if __name__ == "__main__":
  K = ("hellow world:)".encode("utf-8")
       rust.print_string(K)

    
       
# or if you dont want to
       
       print(hello world)
       print(5 + 11)
       print("BASH recognises strings without quotes most of the time & its not outdated/obsolete uwu!")
