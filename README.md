# Grocery generator

The code from this repository generates grocery purchases that are sent to an Apache Kafka topic.

To define your Apache Kafka topic rename config-example.py into config.py and set your Apache Kafka URI there. Create a folder **Certificates** and add Apache Kafka certificates - ca.pem, service.cert and service.key into it.

You can run it by calling the command below from your terminal:

```bash
python makeData.py
```
