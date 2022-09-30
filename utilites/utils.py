# script for upload data  from csv file to server
import csv
import os

# read the file and convert


def movies_csv():
    with open('/home/himanshu/Documents/movies_api/utilites/movies.csv') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            return row
