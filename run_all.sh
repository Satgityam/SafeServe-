#!/bin/bash

echo "🧪 Compiling C++ Transaction Simulator..."
g++ simulator/transaction_simulator.cpp -o simulator/sim
./simulator/sim

echo "🧠 Running Python Fraud Detection Engine..."
python3 engine/fraud_engine.py

echo "📊 Launching Streamlit Dashboard..."
streamlit run dashboard/app.py
