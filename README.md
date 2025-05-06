# FinOps Dashboard: Cloud Cost Visibility & Free Tier Usage Tracker

This project is a lightweight FinOps dashboard for tracking cloud usage (AWS/GCP) and alerting when usage is approaching or exceeding free-tier limits.

## 🚀 Objective
To detect free-tier breaches proactively and avoid unexpected billing from cloud service providers like AWS and GCP.

## 🛠️ Tech Stack
- Python (Data Fetching & Processing)
- SQLite (Lightweight Data Storage)
- Grafana (Visualization)
- AWS Cost Explorer / GCP Billing API

## 📊 Features
- Fetches daily cloud usage & cost
- Stores structured usage data in SQLite
- Displays service-wise cost breakdown in Grafana
- Flags services that approach/exceed free-tier limits

## 📁 Folder Structure
