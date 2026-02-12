# Databricks notebook source
datasets = [
    {
        "file_name" : "Orders"
    },
    {
        "file_name" : "Customers"
    },
    {
        "file_name" : "Products"
    }
        
]

# COMMAND ----------

dbutils.jobs.taskValues.set("output_datasets", datasets)