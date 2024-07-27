## what is broker ?

A message broker is **software that enables applications, systems and services to communicate with each other and exchange information**.

```mermaid
flowchart LR
	queue[[message_broker]]
	p1([p]) -- message --> queue --> c1([C])
	queue --> c2([C])
	queue --> c3([C])
	
	style queue fill:gold,color:black,stroke:black
	
```

Message brokers can **validate, store, route, and deliver messages to the appropriate destinations**. They serve as intermediaries between other applications, allowing senders to issue messages without knowing where the receivers are, whether or not they are active, or how many of them there are.

**RabbitMQ** is a message broker.