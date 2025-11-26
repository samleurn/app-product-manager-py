# from .query import Query

"""
CREATE EXTENSION IF NOT EXISTS "uuid-ossp"
"""
""" 
Query(sql).exe()
"""

""" 
CREATE TABLE IF NOT EXISTS product (
    id SERIAL NOT NULL PRIMARY KEY,
    code UUID NOT NULL,
    name VARCHAR(50) NOT NULL,
    specs TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    modified_at TIMESTAMP NOT NULL
)
"""

""" 
CREATE TABLE IF NOT EXISTS brand (
    id SERIAL NOT NULL PRIMARY KEY,
    code UUID NOT NULL,
    name VARCHAR(50) NOT NULL,
    created_at: TIMESTAMP NOT NULL,
    modified_at TIMESTAMP NOT NULL
)
"""
