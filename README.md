# Grocery generator

The code from this repository generates grocery purchases that are sent to an Apache Kafka topic.

## Steps to use this repository

1. Install dependencies: 
```bash
pip install -r requirements.txt
```

2. Configure your Apache Kafka cluster: rename config-example.py into config.py and set your Apache Kafka URI there. Also create a folder **Certificates** and add Apache Kafka certificates - ca.pem, service.cert and service.key into it. 

3. Create topics **CDC-input** and **input-events** in the Apache Kafka service

4. Run the script:
```bash
python makeData.py
```
