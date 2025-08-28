# NamasteKart Order File Validation Pipeline (Python + AWS S3 + SQL Server)

## 📦 Project Overview

NamasteKart is an online retailer operating in Mumbai and Bangalore. This project automates the **validation, classification, logging, and notification** of daily order files that are uploaded to an AWS S3 bucket. Built using **modular Python**, it ensures that all incoming transaction files are processed against a set of business rules and stored accordingly.

## 🧭 Business Objective

Ensure all order files are:
- Validated using custom rules
- Automatically sorted into success and rejection buckets
- Logged with detailed rejection reasons
- Stored in SQL Server (valid records only)
- Communicated to the business team via daily email

## 📁 Folder & File Structure

- NamasteKart/
├── incoming_files/YYYYMMDD/
├── success_files/YYYYMMDD/
├── rejected_files/YYYYMMDD/

### 📄 Incoming Files contain:

- `order_id`
- `product_id`
- `order_date`
- `city`
- `quantity`
- `total_sales_amount`

### 📘 Product Master File contains:

- `product_id`
- `product_name`
- `price`

## ✅ Validation Rules

1. `product_id` must exist in the product master  
2. `total_sales_amount == product_price * quantity`  
3. `order_date` must not be in the future  
4. No field should be empty  
5. `city` must be either **Mumbai** or **Bangalore**

## 🚀 Expected Workflow

1. Read all order files from `incoming_files/YYYYMMDD/`  
2. Validate each file against the rules  
   - If **any row fails**, reject the entire file  
3. Write valid files to `success_files/YYYYMMDD/`  
4. Write rejected files to `rejected_files/YYYYMMDD/`  
   - Include `error_{filename}.csv` with `rejection_reason` column  
5. Send an email to the business team:
   - Summary of processed files
   - If no files found, send alternate message

### 🧱 Modular Python Design

- `pipeline_main.py`: Orchestrates validation, S3 handling, DB insert, and email
- `pipeline_utils.py`: S3 read/write, product loader, line-level validation, credentials
- `email_utils.py`: Sends email using Gmail SMTP over SSL
- `sql_server_connector.py`: Connects to local SQL Server using `pyodbc`
- `config.ini`: Stores credentials (AWS + Gmail)
- `orders_1.csv`, `orders_2.csv`: Sample input files
- `product_master.csv`: Product reference file

## 🎓 Skills Demonstrated

- AWS S3 file I/O with boto3
- Modular Python programming
- SQL Server data insertion using pyodbc
- File validation with custom business rules
- Email automation with smtplib
- Use of config files for credential security
- Real-world ETL pipeline simulation

## ▶️ How to Run

1. Fill in credentials in config.ini
2. Fill in your SQL instance and database details in sql_server_connector.py file
3. Update the bucket_name where the files will be stored, update from and to email addresses
4. Upload sample order files to incoming_files/YYYYMMDD/ in S3
5. Run: python pipeline_main.py
6. Check:
    - S3 folders for routed files
    - Email inbox for summary report
    - SQL Server for inserted records
