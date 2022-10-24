import ctypes

rust = ctypes.CDLL("target/release/librust_lib.so")

if __name__ == "__main__":
  K = ("hellow world:)".encode("utf-8")
       rust.print_string(K)
