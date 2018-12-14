def print_list(items, header=None):
        if header != None:
                print(header)
        for item in items:
                print(str(items))
        print()

name = input("whats your name?")
smile = input("Wanna a free random fact " + name + "? [Yes,No]  ")
if smile =="yes":
        print("Hell yh, here is the selection of catgories to choose from")      
        catgories = ["dark humor","animals","fruits","weird"]
        print_list(catgories, "catagory")
        ask = input("which fact do you wanna know?")
        if ask == "dark humor":
                sure = input("You sure there " + name + "? yes or no")
                if sure == "yes":
                        print("well then ok...")
                        input("Do you know there is a solution to both over population and world hunger?")
                        print("The solution is cannibalism (￣▽￣)ノ")
                else:
                        print("Good beter safe than sorry (*^▽^*)")
        if ask == "animals":
                Print("Did you know that snails can sleep for three years, i know right !!I WANT THIS ABILITY!! (ﾉಥ益ಥ）ﾉ﻿ ┻━┻")

        if ask == "fruits":
                print("Did you know that grapes EXPLODE when put into the microwave!!! (ʘᗩʘ’)")
        if ask == "weird":
                print(" A duck’s quack doesn’t echo, and nobody can figure out why.")
if smile =="no":
        print("Why not whats  the harm ¯\_(ツ)_/¯? Oh well naybe another time")

