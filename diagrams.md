
# Student Performance Management System - Diagrams

## 1. System Architecture Diagram

```mermaid
flowchart TD
    A[User] --> B[Main Menu - main.py]
    B --> C[Student Management - student.py]
    B --> D[Performance Analysis - analysis.py]
    C --> E[Input Validation - validation.py]
    C --> F[Grade Calculation - marks.py]
    D --> F
    C --> G[Data Storage - storage.py]
    D --> G
    G --> H[(students.txt)]
    H --> G
    G --> C
    G --> D
```

## 2. System Workflow Diagram

```mermaid
flowchart TD
    A([Start]) --> B[Display Main Menu]
    B --> C{Select Option}
    C -->|1| D[Add Student]
    C -->|2| E[View Students]
    C -->|3| F[Search Student]
    C -->|4| G[Update Student]
    C -->|5| H[Delete Student]
    C -->|6| I[Generate Performance Report]
    D --> J[Save Records]
    G --> J
    H --> J
    J --> B
    E --> B
    F --> B
    I --> B
    C -->|7| K([Exit])
    C -->|Invalid| L[Display Error Message]
    L --> B
```

## 3. Data Storage Design

Each student record contains these fields:

| Field | Description |
|---|---|
| Name | Student's name |
| Roll Number | Unique student identifier |
| Marks | Marks obtained out of 100 |
| Grade | Grade calculated from marks |

The records are stored in `students.txt`.
Each line represents one student record.