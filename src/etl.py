import os
from utils.test_utils import say_caca
from tasks.extract import extract
from tasks.transform import transform

def main():
    extract()
    transform()

if __name__ == '__main__':
    main()

