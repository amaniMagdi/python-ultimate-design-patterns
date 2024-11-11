# python-ultimate-design-patterns
In this repo we will design and build maintainable, extensible and robust python packages, each package is a type of design pattern with its UML diagram.
#### 1- Behavioral Design Patterns:

 - **Observer**

> Is a behavioral design pattern that lets you define a subscription
> mechanism to notify multiple objects about any events that happen to
> the object they’re observing. The repo contains below codes.
> 	 - online market place example.
> 	 - newsletter example.

- **Strategy**

> Is a behavioral design pattern that lets you define a family of algorithms,
> put each of them into a separate class, and make their objects interchangeable.
> Below code examples are included:
> 	 - e-commerce
> 	 - notification service
>  	- message_formatter

- **Template Method**

> Is a behavioral design pattern that defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps of the algorithm without changing its structure.
> Below code examples are included:
> 	 - cv_report_generation
> 	 - message_formatter
>  	- video_preset

- **Memento**

> Is a behavioral design pattern that lets you save and restore the previous state of an object without revealing the details of its implementation.
> It separates dependency between **History**, **Object State** and **Context**.
> Below code examples are included:
> 	 - text_editor
> 	 - canvas

- **Visitor**

> Is a behavioral design pattern that allows adding new behaviors to existing class hierarchy without altering any existing code.
> Below code examples are included:
> 	 - schedule_management
> 	 - document_processing_system

- **Iterator**
> Is a behavioral design pattern that lets you traverse elements of a collection without exposing its underlying representation.
>  - employee_hierarchy_iterator
>  - profiles_iterator

- **Chain of Responsibility**
> Is behavioral design pattern that allows passing request along the chain of potential handlers until one of them handles request.
> Below code examples are included:
> - middleware_handler (Strategy + Template Method + Chain of Responsibility are applied in this exercise)
> - data_processing_chain_handler

- **State** 
> Is a behavioral design pattern that allows an object to change the behavior when its internal state changes.
> Below code examples are included:
>  - order_management
>  - project_management

- **Mediator**
> Is a behavioral design pattern that lets you reduce chaotic dependencies between objects. The pattern restricts direct communications between the objects and forces them to collaborate only via a mediator object.
> Below code examples are included:
>  - chat_mediator
>  - air_traffic_controller_mediator

- **Command**
> Is behavioral design pattern that converts requests or simple operations into objects.
> Below code examples are included:
>  - smart_home_application
>  - text_editor
