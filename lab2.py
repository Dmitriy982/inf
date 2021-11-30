import random
import os

if __name__=='__main__':

    A = random.randint(0,100)
    B = random.randint(0,100)
    alice= random.randint(0,100)
    bob= random.randint(0,100)

    gen_alice = int(pow(B, alice, A))
    gen_bob = int(pow(B, bob, A))

    ka = int(pow(gen_bob, alice, A))
    kb = int(pow(gen_alice, bob, A))
    print("Alice private key: \t", alice)
    print("Bob private key: \t", bob)
    print("New key Alice: \t", gen_alice)
    print("New key Bob: \t", gen_bob)

    print("Secret key: \t", ka, kb)
    os.system("PAUSE")