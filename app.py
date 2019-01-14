import os
import random
import time

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from searchAndSort import *

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def reroute():
    return redirect("/sort", code=302)

@app.route("/sort", methods=["GET","POST"])
def sort():
    if request.method == "POST":

        type = request.form.get("genArr", False)
        unsortedArr = []

        if type == 'g':
            startRange = request.form.get("startRange", False)
            endRange = request.form.get("endRange", False)
            items = request.form.get("items", False)

            startRange = int(startRange)
            endRange = int(endRange)
            items = int(items)

            arr = []
            unsortedArr =[]
            for i in range(0,items):
                item = random.randint(startRange,endRange)
                arr.append(item)
                unsortedArr.append(item)

        else:
            fileName = request.form.get("file",False)
            file=open(fileName,'r')
            arr = file.read().splitlines()
            for i in range(len(arr)):
                try:
                    arr[i] == int(arr[i])
                except ValueError:
                    del arr[i]
                    continue

        ascdesc = request.form.get("ascdesc", False)
        sortType = request.form.get("submit", False)

        startTime = time.time()
        if sortType == "Merge Sort":
            if ascdesc == "Asc":
                sortedArr = mergeSortAsc(arr)
            else:
                sortedArr = mergeSortDesc(arr)
        elif sortType == "Bubble Sort":
            if ascdesc == "Asc":
                sortedArr = bubbleSortAsc(arr)
            else:
                sortedArr = bubbleSortDesc(arr)
        endTime = (time.time() - startTime)*1000

        return render_template("sort.html", arr = unsortedArr, sortedArr = sortedArr, endTime = endTime)
    else:
        return render_template("sort.html")

@app.route("/search", methods=["GET","POST"])
def search():
    if request.method == "POST":
        type = request.form.get("genArr", False)
        unsortedArr = []

        if type == 'g':
            startRange = request.form.get("startRange", False)
            endRange = request.form.get("endRange", False)
            items = request.form.get("items", False)

            startRange = int(startRange)
            endRange = int(endRange)
            items = int(items)

            arr = []
            unsortedArr =[]
            for i in range(0,items):
                item = random.randint(startRange,endRange)
                arr.append(item)
                unsortedArr.append(item)

        else:
            fileName = request.form.get("file",False)
            file=open(fileName,'r')
            arr = file.read().splitlines()
            for i in range(len(arr)-1):
                try:
                    arr[i] == int(arr[i])
                except ValueError:
                    del arr[i]
                    continue

        searchType = request.form.get("submit", False)
        searchNum = request.form.get("searchNum",False)
        searchNum = int(searchNum)

        startTime = time.time()
        if searchType == "bt":
            itemFound = binarySearchTree(arr,searchNum)
        elif searchType == "b":
            itemFound = binarySearch(arr,searchNum)
        elif searchType == "l":
            itemFound = linearSearch(arr,searchNum)
        endTime = (time.time() - startTime)*1000

        unsortedArr = arr

        return render_template("search.html", arr = unsortedArr, itemFound = itemFound, endTime = endTime)
    else:
        return render_template("search.html")



# @app.route("/sortSearch", methods=["GET","POST"])
# def sortSearch():
#     if request.method == "POST":
#
#         type = request.form.get("genArr", False)
#
#         if type == 'g':
#             startRange = request.form.get("startRange", False)
#             endRange = request.form.get("endRange", False)
#             items = request.form.get("items", False)
#
#             startRange = int(startRange)
#             endRange = int(endRange)
#             items = int(items)
#
#             arr = []
#             unsortedArr =[]
#             for i in range(0,items):
#                 item = random.randint(startRange,endRange)
#                 arr.append(item)
#                 unsortedArr.append(item)
#
#         else:
#             fileName = request.form.get("file",False)
#             file=open(fileName,'r')
#             arr = file.read().splitlines()
#             for i in range(len(arr)):
#                 arr[i] == int(arr[i])
#
#         unsortedArr = arr
#
#         searchType = request.form.get("search", False)
#         sortType = request.form.get("sort", False)
#         searchNum = request.form.get("searchNum",False)
#         searchNum = int(searchNum)
#
#         startTimeSort = time.time()
#         if sortType == "m":
#             sortedArr = mergeSortAsc(arr)
#         elif sortType == "b":
#             sortedArr = bubbleSortAsc(arr)
#         sortTime = (time.time() - startTimeSort)*1000
#
#         startTimeSearch = time.time()
#         if searchType == "bt":
#             itemFound = binarySearchTree(sortedArr,searchNum)
#         elif searchType == "b":
#             itemFound = binarySearchSorted(sortedArr,searchNum)
#         elif searchType == "l":
#             itemFound = linearSearch(sortedArr,searchNum)
#         searchTime = (time.time() - startTimeSearch)*1000
#
#
#         return render_template("sortSearch.html", arr = unsortedArr, sortedArr = sortedArr, itemFound = itemFound, sortTime = sortTime, searchTime = searchTime)
#     else:
#         return render_template("sortSearch.html")
