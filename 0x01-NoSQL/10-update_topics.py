#!/usr/bin/env python3
"""
updates the  school name and  topic
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    update many rows
    """
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
