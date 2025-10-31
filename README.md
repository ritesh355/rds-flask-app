# Flask App with AWS RDS (MySQL)

A simple Flask web application connected to an AWS RDS MySQL database, demonstrating real-world DevOps and Cloud integration.

---

## 🧠 Project Overview

This project shows how to:
- Host a web application on AWS EC2.
- Connect it securely to a managed MySQL database on AWS RDS.
- Display data from the database using a Flask REST API.

---

## ⚙️ Tech Stack
- **AWS EC2** – Web server
- **AWS RDS (MySQL)** – Managed database
- **Flask** – Web framework
- **Python** – Application language

---

## 🪜 Setup Instructions

## 1️⃣ Create RDS MySQL Database
### 🧪 Step 1: Open RDS Service
1. Sign in to the **AWS Management Console**.  
2. Search for **RDS** and open it.
  ![](images/rds1.png)
4. Click **Create database**.
   ![](images/rds2.png)

---

### 🧱 Step 2: Choose Database Creation Method
- **Method:** Standard create  
- **Engine type:** MySQL
- ![](images/rds3.png)
- **Version:** Latest supported version (e.g., MySQL 8.x)  

---

### ⚙️ Step 3: Choose a Template
- **Template:** Free tier (if not visible, select `Production` and use `db.t3.micro`) if in you setopu free option is avalable then go for it ..
- ![](images/rds4.png)  

---

### 🗝️ Step 4: Set DB Instance Details
- **DB instance identifier:** `myrds-db`  
- **Master username:** `admin`  
- **Master password:** Choose a secure password (e.g., `MyRDS@12345`)  
- Confirm password
- ![](images/rds5.png)

---

### 💾 Step 5: Configure Instance
- **DB instance class:** `db.t3.micro`  
- **Storage:** 20 GB (default)  
- **Storage autoscaling:** enabled (optional)
- ![](images/rds6.png)

---

### 🌐 Step 6: Connectivity
1. **VPC:** default VPC  
2. **Public access:** Yes  
3. **VPC security group:** Create new → `rds-sg`
   ![](images/rds7.png)
     ![](images/rds8.png)


---

### 🧰 Step 7: Additional Configuration
- **Initial database name:** `devops_lab`  
- **Backup retention:** 1 day  
- **Monitoring:** optional  
- **Deletion protection:** disable  
   ![](images/rds9.png)

Click **Create database** 🟢  
> Wait 5–10 minutes until status shows **Available**.

---

## 🔹 Step 8: Configure Security Group Access

### 1️⃣ EC2 Security Group
- Go to **EC2 → Instances → your instance → Security → Security groups**  
- Note the EC2 security group (e.g., `ec2-sg`)  
   ![](images/rds10.png)

### 2️⃣ RDS Security Group
- Go to **EC2 → Security Groups → rds-sg**  
- **Inbound rules:**  
  | Type          | Protocol | Port | Source           |
  |---------------|---------|------|-----------------|
  | MySQL/Aurora  | TCP     | 3306 | EC2 security group (`ec2-sg`) |
  |SSH            | TCP     |22 | enboundrule|

> This allows the EC2 instance to connect to RDS.
   ![](images/rds11.png)


---

## 🔗 Step 9: Connect to RDS

### For Ubuntu EC2:
1. Update packages:
```bash
sudo apt update
```
2. Install MySQL client:
```bash
sudo apt install mysql-client -y
```
   ![](images/ssh3.png)



3. Connect to your RDS instance:
```bash
mysql -h <RDS-ENDPOINT> -u admin -p
```
- Replace <RDS-ENDPOINT> with your RDS endpoint
-    ![](images/endpoint.png)

- Enter the password you created
-    ![](images/final.png)

- Engine: MySQL
- Instance type: `db.t3.micro` (Free Tier)
- Public access: Enabled
- Note down the endpoint, username, and password.

### 2️⃣ Launch EC2 Instance
- AMI: Ubuntu 22.04
- Security Group:
  - Allow **SSH (22)** from your IP
  - Allow **HTTP (80)** from anywhere
  - Allow **MySQL (3306)** from EC2 security group

### 3️⃣ Connect to EC2
```bash
ssh -i mykey.pem ubuntu@<EC2_PUBLIC_IP>
