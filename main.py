import os
import pygame
import funtions.text_funtions as text
import sys    

if __name__ == "__main__":
    if sys.argv[1].lower() == "text":
        import funtions.text_funtions as text
        text.text_game()
        
    elif sys.argv[1].lower() == "gui":
        pass
    
    elif sys.argv[1].lower() == "help":
        print("text - to run text based version.")
        print("gui  - to run gui based version.")
    else:
        print("Not a valid option.Please run the 'help' command for assistance.")