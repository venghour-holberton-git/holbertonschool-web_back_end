#!/usr/bin/env python3
"""Provide some stats about Nginx logs stored in MongoDB."""

from pymongo import MongoClient


def main():
    """Print Nginx log statistics."""
    client = MongoClient("mongodb://127.0.0.1:27017/")
    collection = client.logs.nginx

    print("{} logs".format(collection.count_documents({})))

    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        count = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    status_checks = collection.count_documents({
        "method": "GET",
        "path": "/status"
    })

    print("{} status check".format(status_checks))


if __name__ == "__main__":
    main()