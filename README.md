# 🔢 Queueing Analytics Platform
**Mohamed · M3 · M.Sc. Queueing Engine Extended to Multi-Domain Service Analytics**

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 🌐 Live Demo
👉 **[Launch Platform](https://your-app-url.streamlit.app)**

---

## 📌 Overview

A multi-domain queueing analytics platform built on an original M.Sc. thesis engine.
One mathematical engine (M/M/S) powers 5 completely different service domains:

```
Manufacturing (M.Sc. Crown Project) → N-stage Job Shop · SimPy · Animation
Bank Queue                          → Customer teller queues
Healthcare Queue                    → Hospital ED/outpatient
Call Center Queue                   → SLA + Abandonment analysis
Airport Security Queue              → Flight-driven arrivals · Miss-flight risk
```

---

## 🏗️ Architecture

```
ONE ENGINE → MULTIPLE DOMAINS

queue_engine.py (M/M/S core)
    ↓
MMS(λ, μ, S) → {ρ, Lq, Wq, Ws, Ls, P0}
    ↓
Domain Templates (one per service):
  Bank · Healthcare · Call Center · Airport
```

---

## 📊 Domain Templates

| Domain | λ | μ | S | ρ | Records | Key KPI |
|--------|---|---|---|---|---------|---------|
| 🏭 Manufacturing | Jobs/hr | Machines/hr | N stages | Variable | 54,750 shifts | OEE · Bottleneck |
| 🏦 Bank | 30/hr | 12/hr | 3 tellers | 0.833 | 62,537 | Wait time · Cost |
| 🏥 Healthcare | 12/hr | 4/hr | 4 doctors | 0.750 | ~36K | Breach % · SLA |
| 📞 Call Center | 50/hr | 20/hr | 3 agents | 0.833 | 100,398 | SLA % · Abandon |
| ✈️ Airport | 80/hr | 30/hr | 5 checkpoints | 0.533 | 444,277 | Miss-flight risk |

---

## 🔢 Mathematical Foundation — M/M/S Model

```
ρ  = λ / (S × μ)           Server utilization
Lq = f(P₀, ρ, S)           Avg queue length
Wq = Lq / λ                Avg waiting time
Ws = Wq + 1/μ              Avg time in system
Ls = λ × Ws                Avg customers in system
```

**All KPIs update live with sidebar sliders — fully interactive.**

---

## 🗂️ Project Structure

```
📁 Queueing_Analytics_Platform/
├── Home.py                        ← Master Hub entry
├── queue_engine.py                ← Shared M/M/S engine
├── bank_dashboard.py
├── healthcare_dashboard.py
├── callcenter_dashboard.py
├── airport_dashboard.py
├── requirements.txt
├── packages.txt
├── pages/
│   ├── Manufacturing.py           ← Crown Project page
│   ├── Bank.py
│   ├── Healthcare.py
│   ├── CallCenter.py
│   └── Airport.py
└── data/
    ├── bank_queue_data.csv
    ├── healthcare_queue_data.csv
    ├── callcenter_queue_data.csv
    └── airport_queue_data.csv
```

---

## 🚀 How to Run

```bash
git clone https://github.com/mohamedsayed980/Queueing_Analytics_Platform.git
cd Queueing_Analytics_Platform
pip install -r requirements.txt
streamlit run Home.py
```

---

## 🛠️ Tech Stack

`Python` · `Streamlit` · `Pandas` · `NumPy` · `Matplotlib` · `Seaborn`
`Plotly` · `SciPy` · `SimPy` · `Statsmodels`

---

## 👑 Crown Project — Manufacturing Origin

The platform is built on a rebuilt M.Sc. thesis in job-shop capacity planning:

| Engine File | Lines | Tests |
|-------------|-------|-------|
| queue_engine.py | 1,638 | 19/21 ✅ |
| simpy_engine.py | 488 | 6/6 ✅ |
| distribution_fitting.py | 921 | 17/17 ✅ |
| animation_engine.py | 515 | Complete ✅ |
| live_simulation.py | 852 | 4/4 ✅ |

---

## 💡 Key Insight

> **The hardest version was built first (N-stage job shop).
> Every service template is a special case of what already exists.**

---

**Mohamed · M3 · M.Sc. Mechanical Engineering · Queueing Theory → Service Analytics**
