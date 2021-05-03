##### SCRIPT STARTS HERE #####
#!usr/bin/bash python

import argparse

def arg_parser():
    """ Parse command line arguments

    Outputs:
        arguments {object} -- object containing command line arguments
    """
    
    parser = argparse.ArgumentParser()
    parser.add_argument("title", help="Title of the book you read")
    parser.add_argument("author", help="Author name of the book you read")
    parser.add_argument("readNum", help="Number of times you read the book", type=int)
    parser.add_argument("-d", "--description", help="Print out that you have no recent reading activity")
    
    return(parser.parse_args())

def main():
    args = arg_parser()
    
    print("I have read {} by {} {} times.".format(args.title, args.author, args.readNum))
    
    if args.description:
        print("The book was {}.".format(args.description))
        
if __name__ == "__main__":
    main()
    
