#!/usr/bin/env bash
set -e

# Run Python version and capture execution time
echo "Running Python version..."
PY_TIME=$( (/usr/bin/time -f "%e" python3 project_python/ex1/main.py > /dev/null) 2>&1 )

# Run Rust version and capture execution time
echo "Running Rust version..."
RUST_TIME=$( (cd project_rust/ex1 && /usr/bin/time -f "%e" cargo run --release > /dev/null) 2>&1 )

# Display summary
printf "\nผลการทดสอบเวลา (seconds):\n"
echo "Python: ${PY_TIME}"
echo "Rust:   ${RUST_TIME}"

