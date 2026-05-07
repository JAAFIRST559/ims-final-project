# 🚨 Incident Management System (IMS)

A high-throughput, resilient **Incident Management System (IMS)** designed to ingest, process, and manage failure signals from distributed systems in real time.

This project simulates **production-grade Site Reliability Engineering (SRE)** workflows, including:
- Signal aggregation  
- Incident lifecycle management  
- Root Cause Analysis (RCA) enforcement  

---

## 🎯 Problem Statement

Modern distributed systems generate massive volumes of failure signals (e.g., errors, latency spikes, timeouts). The system addresses the following challenges:

- Handle **10,000+ signals per second**
- Prevent system overload via **backpressure handling**
- Group related failures using **debouncing**
- Track incidents through a **strict lifecycle**
- Enforce **mandatory RCA before closure**

---

## 🏗️ System Architecture

```text
                ┌──────────────┐
                │  Ingestion   │
                │   API        │
                └──────┬───────┘
                       ↓
                ┌──────────────┐
                │ Async Queue  │
                │ (Backpressure)│
                └──────┬───────┘
                       ↓
                ┌──────────────┐
                │   Workers    │
                └───┬────┬─────┘
                    ↓    ↓
        ┌──────────────┐  ┌──────────────┐
        │   MongoDB    │  │ PostgreSQL   │
        │ (Raw Signals)│  │ (Work Items) │
        └──────────────┘  └──────────────┘
                    ↓
                ┌──────────────┐
                │    Redis     │
                │ (Cache +     │
                │ Debouncing)  │
                └──────────────┘
                    ↓
                ┌──────────────┐
                │   React UI   │
                └──────────────┘
```

---

## ⚙️ Tech Stack

| Layer              | Technology                  |
|-------------------|---------------------------|
| Backend           | FastAPI (Async Python)    |
| Frontend          | React                     |
| NoSQL             | MongoDB (Signals)         |
| SQL               | PostgreSQL (Work Items, RCA) |
| Cache             | Redis                     |
| Containerization  | Docker Compose            |

---

## 🚀 Key Features

### 🔥 High-Throughput Signal Ingestion
- Handles burst traffic up to **10,000 signals/sec**
- Fully **asynchronous processing** for non-blocking ingestion

### ⚡ Debouncing Logic (Signal Aggregation)
- Signals from the same component within **10 seconds → 1 Work Item**
- Prevents alert flooding
- Implemented using **Redis TTL keys**

### 🔄 Incident Lifecycle Engine

Implements a strict **state machine**:

```text
OPEN → INVESTIGATING → RESOLVED → CLOSED
```

- ✔ Enforces valid transitions  
- ❌ Prevents invalid state jumps  

### 🧠 Mandatory RCA Enforcement
- Incidents **cannot be CLOSED without RCA**
- Ensures accountability and structured post-mortem analysis

### 🧮 MTTR Calculation

```text
MTTR = RCA_End_Time - First_Signal_Time
```

### 🚦 Rate Limiting
- Protects system from overload
- Prevents cascading failures

### 🔁 Retry Logic (Resilience)
- Automatic retries for failed database writes
- Improves reliability under transient failures

### 📊 Observability
- `/health` endpoint for system monitoring
- Logs **signals/sec every 5 seconds**
- Enables throughput visibility

---

## 🧠 Backpressure Handling (Critical SRE Concept)

To maintain stability under heavy load:

- Incoming signals are buffered using an **async queue**
- Workers process signals independently
- Ingestion is decoupled from persistence

**Result:** System remains stable even when downstream systems (e.g., databases) are slow.

---

## 🗄️ Data Strategy

| Data Type     | Storage     | Reason                              |
|--------------|------------|-------------------------------------|
| Raw Signals  | MongoDB    | High volume, flexible schema        |
| Work Items   | PostgreSQL | Strong consistency, transactions    |
| Cache/Debounce | Redis    | Fast access, TTL support            |

---

## ▶️ Setup Instructions

```bash
docker compose up --build
```

---

## 🔌 API Endpoints

| Endpoint         | Method | Description          |
|-----------------|--------|----------------------|
| `/health`       | GET    | Health check         |
| `/ingest`       | POST   | Ingest signal        |
| `/incidents`    | GET    | List incidents       |
| `/incident/{id}`| GET    | Incident details     |
| `/rca/{id}`     | POST   | Submit RCA           |

---

## 🧪 Sample Input

```json
{
  "component_id": "RDBMS_01",
  "error": "connection timeout",
  "timestamp": "2026-05-01T10:00:00Z"
}
```

---

## 🖥️ Frontend Features

- 📊 Live incident dashboard  
- 🔍 Incident detail view (with raw signals)  
- 📝 RCA submission form  

---

## 📈 Performance Considerations

- Async I/O for high concurrency  
- Redis caching for hot-path reads  
- Debouncing reduces database writes  
- Queue-based processing ensures scalability  

---

## 🔒 Security Considerations

- Input validation using **Pydantic**  
- Environment-based configuration  
- Rate limiting to prevent abuse  

---

## 🔮 Future Enhancements

- Kafka for distributed ingestion  
- Auto-scaling worker pool  
- Alert integrations (Slack / Email)  
- Advanced monitoring dashboards  

---

## 📎 Repository

👉 https://github.com/your-username/ims-project

---

## 🏁 Conclusion

This system demonstrates key **real-world SRE principles**, including:

- High-throughput system design  
- Resilient architecture  
- Incident lifecycle enforcement  
- Observability and reliability
